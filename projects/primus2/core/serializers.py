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


class AnotacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anotacao
        fields = (
            'id',
            'atividade',
            'descricao',
        )


class AtividadeSerializer(serializers.HyperlinkedModelSerializer):
    anotacoes = AnotacaoSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Atividade
        fields = (
            'url',
            'id',
            'criada',
            'inicio',
            'fim',
            'is_realizada',
            'assunto',
            'anotacoes',
        )


class PlanoDeEstudoSerializer(serializers.HyperlinkedModelSerializer):
    atividades = AtividadeSerializer(
        many=True,
        read_only=True
    )

    usuario = serializers.SlugRelatedField(
        queryset=Usuario.objects.all(),
        slug_field='username',
    )

    class Meta:
        model = PlanoDeEstudo
        fields = (
            'url',
            'id',
            'usuario',
            'nome',
            'atividades',
            'is_publico',
        )


class AssuntoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assunto
        fields = (
            'url',
            'id',
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

