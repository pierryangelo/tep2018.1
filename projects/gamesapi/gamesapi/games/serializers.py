from django.utils import timezone

from rest_framework import serializers
from .models import Game, GameCategory, Player, PlayerScore


class Validations:
    @staticmethod
    def score_must_be_greater_than_zero(value):
        if value is None:
            raise serializers.ValidationError("The is score can't be empty.")

        if value < 0:
            raise serializers.ValidationError("Score must be a non-negative number.")

    @staticmethod
    def score_date_cant_be_in_the_future(date_time):
        if date_time > timezone.now():
            raise serializers.ValidationError("Score can't be in the future.")



class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='game-detail',
    )

    class Meta:
        model = GameCategory
        fields = (
            'url',
            'pk',
            'name',
            'games'
        )


class GameSerializer(serializers.HyperlinkedModelSerializer):
    game_category = serializers.SlugRelatedField(
        queryset=GameCategory.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Game
        fields = (
            'url',
            'name',
            'game_category',
            'release_date',
            'played'
        )


class PlayerScoreSerializer(serializers.HyperlinkedModelSerializer):

    game = serializers.SlugRelatedField(
        queryset=Game.objects.all(),
        slug_field='name'
    )
    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(),
        slug_field='name'
    )

    score = serializers.IntegerField(
        validators=[Validations.score_must_be_greater_than_zero])
    score_date = serializers.DateTimeField(
        validators=[Validations.score_date_cant_be_in_the_future])

    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'player',
            'game',
        )


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores = PlayerScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = (
            'url',
            'name',
            'gender',
            'scores',
        )

