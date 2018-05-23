from rest_framework import serializers

from .models import Post, User, Comment, Address


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # posts = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=False,
    #     view_name='post-detail',
    # )
    #
    # addresses = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=False,
    #     view_name='address-detail',
    # )

    class Meta:
        model = User
        fields = (
            'url',
            'pk',
            'name',
            'email',
            # 'posts',
            # 'addresses',
        )