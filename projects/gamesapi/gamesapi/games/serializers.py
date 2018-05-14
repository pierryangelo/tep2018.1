from rest_framework import serializers
from rest_framework import status
from .models import Game


class GameSerializer(serializers.ModelSerializer):

    def validate_name(self, value):
        """
        Não permite nomes iguais
        """
        for game in Game.objects.all():
            if game.name == value:
                raise serializers.ValidationError("Esse nome já existe!",
                                                  code=status.HTTP_400_BAD_REQUEST)
        return value


    def validate(self, data):
        """
        Não permite campos vazios
        """
        for k in data:
            if not data[k]:
                raise serializers.ValidationError("Os campos não podem ser vazios!",
                                                  code=status.HTTP_400_BAD_REQUEST)
        return data

    class Meta:
        model = Game
        fields = ('id', 'name', 'release_date', 'game_category')


        # extra_kwargs = {
        #     'name': {'required': True},
        #     'release_date': {'required': True},
        #     'game_category': {'required': True}
        # }
