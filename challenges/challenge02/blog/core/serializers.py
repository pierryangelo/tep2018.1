from rest_framework import serializers
from rest_framework_nested.relations import NestedHyperlinkedRelatedField

from .models import Post, User, Address, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='posts-detail',
    )

    addresses = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='addresses-detail',
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


class UserSummarySerializer(serializers.HyperlinkedModelSerializer):
    total_comments = serializers.SerializerMethodField(method_name='total_comments')
    total_posts = serializers.SerializerMethodField(method_name='total_posts')

    def total_posts(self, o):
        return o.posts.all().count()

    def total_comments(self, o):
        c = 0
        for p in o.posts.all():
            c += p.comments.all().count()
        return c

    class Meta:
        model = User
        fields = ('id', 'name', 'total_posts', 'total_comments')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comments-detail',
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