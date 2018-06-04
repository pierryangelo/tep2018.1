from rest_framework import serializers
from rest_framework_nested.relations import NestedHyperlinkedRelatedField
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer, NestedHyperlinkedIdentityField

from .models import Post, User, Address, Comment


class CommentSerializer(NestedHyperlinkedModelSerializer):
    url = NestedHyperlinkedIdentityField(view_name='comments-detail',
                                         parent_lookup_kwargs={'post_pk': 'post__pk'})

    class Meta:
        model = Comment

        fields = (
            'url',
            'id',
            'name',
            'email',
            'body',
        )


class PostSerializer(NestedHyperlinkedModelSerializer):

    url = NestedHyperlinkedIdentityField(view_name='posts-detail',
                                         parent_lookup_kwargs={'user_pk': 'user__pk'})

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
            'title',
            'body',
            'comments'
        )


class AddressSerializer(NestedHyperlinkedModelSerializer):
    url = NestedHyperlinkedIdentityField(view_name='addresses-detail',
                                         parent_lookup_kwargs={'user_pk': 'user__pk'})
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

    url = serializers.HyperlinkedIdentityField(view_name='quick-detail')

    total_comments = serializers.SerializerMethodField()
    total_posts = serializers.SerializerMethodField()

    def get_total_posts(self, obj):
        return obj.posts.count()

    def get_total_comments(self, obj):
        total_comments = 0
        for p in obj.posts.all():
            total_comments += p.total_comments

        return total_comments


    class Meta:
        model = User
        fields = ('url', 'id', 'name', 'total_posts', 'total_comments')

