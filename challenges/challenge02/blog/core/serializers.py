from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Post, Address, Comment, Profile


class PostIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.profile.pk,
            'post_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)


class ProfilePostCommentRelatedField(serializers.HyperlinkedRelatedField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.post.profile.pk,
            'post_pk': obj.post.pk,
            'comment_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'profile__pk': view_kwargs['pk'],
            'post__pk': view_kwargs['post_pk'],
            'pk': view_kwargs['comment_pk']
        }
        return self.get_queryset().get(**lookup_kwargs)


class PostSerializer(serializers.HyperlinkedModelSerializer):

    url = PostIdentityField(
        view_name='profile-post-detail'
    )

    comments = ProfilePostCommentRelatedField(
        many=True,
        read_only=True,
        view_name='profile-post-comment-detail',
    )

    class Meta:
        model = Post
        fields = (
            'url',
            'profile',
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
            'profile',
            'id',
            'title',
            'body',
            'total_comments',
        )


class ProfilePostsTotalCommentsIdentity(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.pk,
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)


class ProfilePostsTotalCommentsSerializer(serializers.HyperlinkedModelSerializer):
    url = ProfilePostsTotalCommentsIdentity(view_name='profile-comment-detail')
    posts = PostCommentTotalSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('url', 'id', 'posts')


class AddressIdentityField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.profile.pk,
            'address_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)


class AddressSerializer(serializers.HyperlinkedModelSerializer):

    url = AddressIdentityField(
        view_name='profile-address-detail'
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


class ProfilePostRelatedField(serializers.HyperlinkedRelatedField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.profile.pk,
            'post_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'profile__pk': view_kwargs['pk'],
            'pk': view_kwargs['post_pk']
        }
        return self.get_queryset().get(**lookup_kwargs)


class ProfileAddressRelatedField(serializers.HyperlinkedRelatedField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.profile.pk,
            'address_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'profile__pk': view_kwargs['pk'],
            'pk': view_kwargs['address_pk']
        }
        return self.get_queryset().get(**lookup_kwargs)


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    posts = ProfilePostRelatedField(
        many=True,
        read_only=True,
        view_name='profile-post-detail',
    )

    addresses = ProfileAddressRelatedField(
        many=True,
        read_only=True,
        view_name='profile-address-detail',
    )

    class Meta:
        model = Profile

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
            'pk': obj.post.profile.pk,
            'post_pk': obj.post.pk,
            'comment_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    url = CommentIdentityField(
        view_name='profile-post-comment-detail'
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


class ProfileSummarySerializer(ProfileSerializer):

    url = ProfilePostsTotalCommentsIdentity(view_name='profile-summary-detail')

    total_posts = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()

    def get_total_posts(self, obj):
        return obj.posts.all().count()

    def get_total_comments(self, obj):
        total = 0
        for post in obj.posts.all():
            total += post.comments.all().count()
        return total

    class Meta:
        model = Profile
        fields = (
            'url',
            'id',
            'name',
            'total_posts',
            'total_comments',
        )