from rest_framework import serializers

from .models import Post, User, Comment, Address, Comment


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
    comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comment-detail',
    )

    class Meta:
        model = Post
        fields = (
            'url',
            'id',
            'title',
            'body',
            'comments'
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

class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'url',
            'id',
            'name',
            'email',
            'body',
        )