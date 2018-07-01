from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Usuario
from core.models import PlanoDeEstudo
from core.models import Disciplina
from core.models import Assunto
from core.models import Atividade
from core.models import Anotacao


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class PlanoDeEstudoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanoDeEstudo
        fields = '__all__'


class AssuntoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assunto
        fields = (
            'url',
            'disciplina',
            'nome',
            'descricao',
        )


class DisciplinaSerializer(serializers.HyperlinkedModelSerializer):
    assuntos = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='assunto-detail'
    )

    class Meta:
        model = Disciplina
        fields = "__all__"


class AtividadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Atividade
        fields = '__all__'
