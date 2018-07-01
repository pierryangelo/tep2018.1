from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions, filters

from core.models import Usuario, Assunto, Disciplina, PlanoDeEstudo, Atividade, Anotacao
from core.serializers import UsuarioSerializer, Assunto, AssuntoSerializer, DisciplinaSerializer, \
    PlanoDeEstudoSerializer, AtividadeSerializer, AnotacaoSerializer


class UsuarioList(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    name = 'usuario-list'


class UsuarioDetail(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    name = 'usuario-detail'


class PlanoDeEstudoList(generics.ListCreateAPIView):
    queryset = PlanoDeEstudo.objects.all()
    serializer_class = PlanoDeEstudoSerializer
    name = 'planodeestudo-list'

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class PlanoDeEstudoDetail(generics.ListCreateAPIView):
    queryset = PlanoDeEstudo.objects.all()
    serializer_class = PlanoDeEstudoSerializer
    name = 'planodeestudo-detail'


class AssuntoList(generics.ListCreateAPIView):
    queryset = Assunto.objects.all()
    serializer_class = AssuntoSerializer
    name = 'assunto-list'


class AssuntoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assunto.objects.all()
    serializer_class = AssuntoSerializer
    name = 'assunto-detail'


class DisciplinaList(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    name = 'disciplina-list'


class DisciplinaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    name = 'disciplina-detail'


class AtividadeList(generics.ListCreateAPIView):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
    name = 'atividade-list'


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