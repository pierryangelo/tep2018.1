from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import UserSerializer, CommentSerializer
from .serializers import PostSerializer, AddressSerializer
from .serializers import UserSummarySerializer
from .models import User, Post, Address, Comment


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserSummaryViewSet(viewsets.ModelViewSet):
    serializer_class = UserSummarySerializer
    queryset = User.objects.all()


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    @action(detail=True)
    def get_address(self, request, pk=None):
        address = self.get_address()
        return Response(address.data)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # def get_queryset(self):
    #     return User.objects.filter(posts=self.kwargs['user_pk'])
