from rest_framework import serializers

from .models import Post, User, Address, Comment


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
