from django.shortcuts import get_object_or_404

from rest_framework import viewsets, generics
from rest_framework.response import Response


from .serializers import UserSerializer, CommentSerializer
from .serializers import PostSerializer, AddressSerializer
from .models import User, Post, Address, Comment


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

