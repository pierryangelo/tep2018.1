from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions, filters

from core.models import User, Assunto, Disciplina, PlanoDeEstudo, Atividade, Anotacao
from core.serializers import UsuarioSerializer, AssuntoSerializer, DisciplinaSerializer, \
    PlanoDeEstudoSerializer, AtividadeSerializer, AnotacaoSerializer

from core.permissions import *


class UsuarioList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    name = 'user-list'
    permission_classes = (
        IsAdminOrNothing,
        permissions.IsAuthenticated
    )


class UsuarioDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    name = 'user-detail'
    permission_classes = (
        IsProfileOwnerOrIsAdmin,
        permissions.IsAuthenticated,
    )


class PlanoDeEstudoList(generics.ListCreateAPIView):
    queryset = PlanoDeEstudo.objects.all()
    serializer_class = PlanoDeEstudoSerializer
    name = 'planodeestudo-list'
    permission_classes = (
        IsProfessorAndPlanOwnerOrAdmin,
        permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):
        serializer.save(professor=self.request.user)


class PlanoDeEstudoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlanoDeEstudo.objects.all()
    serializer_class = PlanoDeEstudoSerializer
    name = 'planodeestudo-detail'
    permission_classes = (
        IsProfessorAndPlanOwnerOrAdmin,
        permissions.IsAuthenticated
    )


class DisciplinaList(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    name = 'disciplina-list'

    filter_fields = ('nome',)
    search_fields = ('^nome',)
    ordering_fields = ('nome',)

    # Professores podem cadastrar novas disciplinas, entretanto alunos
    # só podem visualizá-las.
    permission_classes = (
        IsProfessorOrAdminOrReadOnly,
        permissions.IsAuthenticated
    )

    # Só permite cadastrar disciplinas nos planos os quais é dono.
    def perform_create(self, serializer):
        if self.request.user != serializer.validated_data['plano'].professor:
            raise ValidationError('Você não é dono do plano de estudos!')
        serializer.save()


class DisciplinaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    name = 'disciplina-detail'

    # Somente professores donos de susas disciplinas podem removê-las.
    permission_classes = (
        IsProfessorOwnerOfSubjectOrAdmin,
        permissions.IsAuthenticated
    )


class AssuntoList(generics.ListCreateAPIView):
    queryset = Assunto.objects.all()
    serializer_class = AssuntoSerializer
    name = 'assunto-list'
    permission_classes = (
        IsProfessorOrAdminOrReadOnly,
        permissions.IsAuthenticated
    )

    # Professores só podem cadastrar assuntos vinculados
    # às disciplinas as quais são donos.
    def perform_create(self, serializer):
        if self.request.user != serializer.validated_data['disciplina'].plano.professor:
            raise ValidationError('Você não pode cadastrar um assunto vinculado a uma disciplina que você não cadastrou!')
        serializer.save()


class AssuntoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assunto.objects.all()
    serializer_class = AssuntoSerializer
    name = 'assunto-detail'

    filter_fields = ('nome',)
    search_fields = ('^nome',)
    ordering_fields = ('nome',)

    # Professores só podem apagar os assuntos das disciplinas de que é autor.
    permission_classes = (
        IsProfessorOwnerOfSubjectOfDisciplineOrAdmin,
        permissions.IsAuthenticated
    )


class AtividadeList(generics.ListCreateAPIView):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
    name = 'atividade-list'
    permission_classes = (
        IsProfessorOrAdminOrReadOnly,
        permissions.IsAuthenticated
    )

    # Não pode cadastrar uma atividade de um plano de aula que não lhe pertence.
    def perform_create(self, serializer):
        if self.request.user != serializer.validated_data['assunto'].disciplina.plano.professor:
            raise ValidationError('Você não pode cadastrar um assunto vinculado a uma disciplina que você não cadastrou!')
        serializer.save()


    # Se o usuário logado for professor, retorna as atividades deste professor,
    # caso estudante, analogamente.
    def get_queryset(self):
        if self.request.user.is_anonymous:
            return None

        user = self.request.user

        if user.is_professor:
            return Atividade.objects.filter(assunto__disciplina__plano__professor=user)

        if user.is_aluno:
            return Atividade.objects.filter(estudante=user)

        return None


class AtividadeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
    name = 'atividade-detail'
    permission_classes = (
        StudentsCanDeleteTheirActivities,
        permissions.IsAuthenticated
    )

    def perform_update(self, serializer):
        if not (serializer.validated_data['estudante']
                and serializer.validated_data['inicio']
                and serializer.validated_data['fim']
                and serializer.validated_data['assunto']) \
                and self.request.user == serializer.validated_data['estudante'] \
                and serializer.validated_data['is_realizada']:
            serializer.save()
        serializer.save()


class AnotacaoList(generics.ListCreateAPIView):
    queryset = Anotacao.objects.all()
    serializer_class = AnotacaoSerializer
    name = 'anotacao-list'
    permission_classes = (
        IsNoteOwner,
        permissions.IsAuthenticated
    )

    # Aluno só pode fazer anotacões em suas atividades.
    def perform_create(self, serializer):
        if self.request.user != serializer.validated_data['atividade'].estudante:
            raise ValidationError('Você não pode fazer uma anotação em uma atividade que não lhe pertence!')
        serializer.save()

    # Retorna somente as anotações do aluno requisitante.
    def get_queryset(self):
        if self.request.user.is_anonymous:
            return None

        user = self.request.user
        return Anotacao.objects.filter(atividade__estudante=user)


class AnotacaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anotacao.objects.all()
    serializer_class = AnotacaoSerializer
    name = 'anotacao-detail'
    permission_classes = (
        IsNoteOwner,
        permissions.IsAuthenticated
    )


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'usuarios': reverse(UsuarioList.name, request=request),
            'planos': reverse(PlanoDeEstudoList.name, request=request),
            'disciplinas': reverse(DisciplinaList.name, request=request),
            'disciplina-assuntos': reverse(AssuntoList.name, request=request),
            'atividades': reverse(AtividadeList.name, request=request),
            'atividade-anotacoes': reverse(AnotacaoList.name, request=request)
        })
