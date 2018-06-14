from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Post, User, Address, Comment


class PostIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.user.pk,
            'post_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)


class UserPostCommentRelatedField(serializers.HyperlinkedRelatedField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.post.user.pk,
            'post_pk': obj.post.pk,
            'comment_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'user__pk': view_kwargs['pk'],
            'post__pk': view_kwargs['post_pk'],
            'pk': view_kwargs['comment_pk']
        }
        return self.get_queryset().get(**lookup_kwargs)


class PostSerializer(serializers.HyperlinkedModelSerializer):

    url = PostIdentityField(
        view_name='user-post-detail'
    )

    comments = UserPostCommentRelatedField(
        many=True,
        read_only=True,
        view_name='user-post-comment-detail',
    )

    class Meta:
        model = Post
        fields = (
            'url',
            'user',
            'id',
            'title',
            'body',
            'comments',
        )


class PostCommentTotalSerializer(PostSerializer):
    total_comments = serializers.SerializerMethodField()

    # if not specified in attribute method_name in SerializerMethodField,
    # the convention says we must add 'get_' prefix.
    def get_total_comments(self, obj):
        return obj.comments.all().count()

    class Meta:
        model = Post
        fields = (
            'url',
            'user',
            'id',
            'title',
            'body',
            'total_comments',
        )


class UserPostsTotalCommentsSerializer(serializers.HyperlinkedModelSerializer):

    posts = PostCommentTotalSerializer(many=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'posts')


class AddressIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.user.pk,
            'address_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)


class AddressSerializer(serializers.HyperlinkedModelSerializer):

    url = AddressIdentityField(
        view_name='user-address-detail'
    )

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


class UserPostRelatedField(serializers.HyperlinkedRelatedField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.user.pk,
            'post_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'user__pk': view_kwargs['pk'],
            'pk': view_kwargs['post_pk']
        }
        return self.get_queryset().get(**lookup_kwargs)


class UserAddressRelatedField(serializers.HyperlinkedRelatedField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.user.pk,
            'address_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'user__pk': view_kwargs['pk'],
            'pk': view_kwargs['address_pk']
        }
        return self.get_queryset().get(**lookup_kwargs)


class UserSerializer(serializers.HyperlinkedModelSerializer):

    posts = UserPostRelatedField(
        many=True,
        read_only=True,
        view_name='user-post-detail',
    )

    addresses = UserAddressRelatedField(
        many=True,
        read_only=True,
        view_name='user-address-detail',
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


class CommentIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.post.user.pk,
            'post_pk': obj.post.pk,
            'comment_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    url = CommentIdentityField(
        view_name='user-post-comment-detail'
    )

    class Meta:
        model = Comment
        fields = (
            'url',
            'id',
            'name',
            'email',
            'body',
        )
