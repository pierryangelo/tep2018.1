from rest_framework import serializers
from rest_framework_nested.relations import NestedHyperlinkedRelatedField
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer, NestedHyperlinkedIdentityField

from .models import Post, User, Address, Comment


class PostSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {'user_pk': 'user__pk'}

    url = serializers.HyperlinkedIdentityField(view_name='posts-detail')

    comments = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comments-detail',
        parent_lookup_kwargs={'post_pk': 'post__pk'}
    )

    class Meta:
        model = Post
        fields = (
            'url',
            'user',
            'id',
            'title',
            'body',
            'comments'
        )


class AddressSerializer(NestedHyperlinkedModelSerializer):
    url = NestedHyperlinkedIdentityField(view_name='addresses-detail')
    parent_lookup_kwargs = {'user_pk': 'user__pk'}

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


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='users-detail')
    posts = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='posts-detail',
        parent_lookup_kwargs={'user_pk': 'user__pk'}
    )

    addresses = NestedHyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='addresses-detail',
        parent_lookup_kwargs={'user_pk': 'user__pk'}
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
        fields = ('url', 'id', 'name', 'total_posts', 'total_comments')


class CommentSerializer(NestedHyperlinkedModelSerializer):
    url = NestedHyperlinkedIdentityField(view_name='comments-detail')

    class Meta:
        model = Comment
        parent_lookup_kwargs = {'post_pk': 'post__pk'}
        fields = (
            'url',
            'id',
            'name',
            'email',
            'body',
        )
