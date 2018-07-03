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


class AssuntoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assunto.objects.all()
    serializer_class = AssuntoSerializer
    name = 'assunto-detail'


class AtividadeList(generics.ListCreateAPIView):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
    name = 'atividade-list'
    permission_classes = (
        IsDonoAtividade,
        permissions.IsAuthenticated,
    )


class AtividadeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
    name = 'atividade-detail'


class AnotacaoList(generics.ListCreateAPIView):
    queryset = Anotacao.objects.all()
    serializer_class = AnotacaoSerializer
    name = 'anotacao-list'


class AnotacaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anotacao.objects.all()
    serializer_class = AnotacaoSerializer
    name = 'anotacao-detail'


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
