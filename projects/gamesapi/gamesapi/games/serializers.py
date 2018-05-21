from rest_framework import serializers
from .models import Game, GameCategory, Player, PlayerScore


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


