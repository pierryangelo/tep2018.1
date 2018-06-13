from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Post, User, Address, Comment


class IdentityCustomField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'pk': obj.user.pk,
            'post_pk': obj.pk
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)


class PostSerializer(serializers.HyperlinkedModelSerializer):

    url = IdentityCustomField(
        view_name='user-post'
    )

    comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comment-detail',
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


class UserSerializer(serializers.HyperlinkedModelSerializer):

    posts = UserPostRelatedField(
        many=True,
        read_only=True,
        view_name='user-post',
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

#
# class UserSummarySerializer(serializers.HyperlinkedModelSerializer):
#     total_comments = serializers.SerializerMethodField(method_name='total_comments')
#     total_posts = serializers.SerializerMethodField(method_name='total_posts')
#
#     def total_posts(self, o):
#         return o.posts.all().count()
#
#     def total_comments(self, o):
#         c = 0
#         for p in o.posts.all():
#             c += p.comments.all().count()
#         return c
#
#     class Meta:
#         model = User
#         fields = ('url', 'id', 'name', 'total_posts', 'total_comments')


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
