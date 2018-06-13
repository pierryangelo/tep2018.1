from rest_framework import generics
from rest_framework.response import Response

from .serializers import UserSerializer, CommentSerializer
from .serializers import PostSerializer, AddressSerializer
from .models import User, Post, Address, Comment


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class AddressList(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class UserPosts(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        user_pk = self.kwargs.get(self.lookup_url_kwarg)
        user_posts = Post.objects.filter(user__pk=user_pk)
        return user_posts


class UserPost(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user_pk = self.kwargs.get('pk')
        post_pk = self.kwargs.get('post_pk')
        user_post = Post.objects.filter(id=post_pk, user__pk=user_pk)
        return user_post
