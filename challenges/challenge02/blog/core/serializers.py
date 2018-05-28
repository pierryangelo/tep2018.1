from rest_framework import serializers
from rest_framework_nested.relations import NestedHyperlinkedRelatedField
from rest_framework_nested import routers

from .models import Post, User, Address, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='user-detail',
    )

    addresses = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='user-addresses-detail',
    )


    class Meta:
        model = User

        fields = (
            'url',
            'id',
            'name',
            'email',
            'posts',
            # 'addresses',
        )


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # comments = serializers.NestedHyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='post-comment-detail',
    # )

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