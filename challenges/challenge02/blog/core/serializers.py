from rest_framework import serializers

from .models import Post, User, Comment, Address


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='post-detail',
    )

    addresses = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='address-detail',
    )

    class Meta:
        model = User
        fields = (
            'url',
            'id',
            'name',
            'email',
            'posts',
            'addresses',
        )


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = (
            'url',
            'id',
            'title',
            'body',
        )

class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Address
        fields = (
            'url',
            'id',
            'street',
            'suite',
            'city',
            'zipcode',
        )