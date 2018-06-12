from rest_framework import serializers

from .models import Post, User, Address, Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment

        fields = (
            'id',
            'name',
            'email',
            'body',
        )


class PostSerializer(serializers.HyperlinkedModelSerializer):

    comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comments-detail'
    )

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'body',
            'comments'
        )


class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Address

        fields = (
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
        view_name='posts-detail',
    )

    addresses = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='addresses-detail',
    )

    class Meta:
        model = User

        fields = (
            'id',
            'name',
            'email',
            'posts',
            'addresses',
        )


class UserSummarySerializer(serializers.HyperlinkedModelSerializer):

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

