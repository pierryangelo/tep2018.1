from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from rest_framework import permissions
from rest_framework.response import Response
from .permissions import *

from .serializers import ProfileSerializer, CommentSerializer
from .serializers import PostSerializer, AddressSerializer
from .serializers import ProfilePostsTotalCommentsSerializer, ProfileSummarySerializer
from .models import Profile, Post, Address, Comment


class ProfilePostTotalCommentList(generics.ListAPIView):
    serializer_class = ProfilePostsTotalCommentsSerializer
    queryset = Profile.objects.all()


class ProfilePostTotalCommentDetail(generics.RetrieveAPIView):
    serializer_class = ProfilePostsTotalCommentsSerializer
    queryset = Profile.objects.all()


class ProfileList(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    http_method_names = ['get', 'options']
    permission_classes = (IsAuthenticated,)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


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
    permission_classes = (permissions.IsAuthenticated,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class ProfilePostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    lookup_url_kwarg = 'pk'
    queryset = Post.objects.none()

    def get_queryset(self):
        profile_pk = self.kwargs.get(self.lookup_url_kwarg)
        profile_posts = Post.objects.filter(profile__pk=profile_pk)
        return profile_posts


class ProfilePostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsPostOwner, IsAuthenticated)

    def get_object(self):
        profile_pk = self.kwargs.get('pk')
        post_pk = self.kwargs.get('post_pk')
        profile_post = Post.objects.get(id=post_pk, profile__id=profile_pk)
        self.check_object_permissions(self.request, profile_post)
        return profile_post


class ProfilePostCommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.none()

    def get_queryset(self):
        profile_pk = self.kwargs.get('pk')
        post_pk = self.kwargs.get('post_pk')
        profile_post_comments = Comment.objects.filter(post__profile__pk=profile_pk, post__pk=post_pk)
        return profile_post_comments


class ProfilePostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_object(self):
        profile_pk = self.kwargs.get('pk')
        post_pk = self.kwargs.get('post_pk')
        comment_pk = self.kwargs.get('comment_pk')
        profile_post_comment = Comment.objects.get(id=comment_pk, post__id=post_pk, post__profile__id=profile_pk)
        return profile_post_comment


class ProfileAddressList(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    lookup_url_kwarg = 'pk'
    queryset = Address.objects.none()

    def get_queryset(self):
        profile_pk = self.kwargs.get(self.lookup_url_kwarg)
        profile_addresses = Address.objects.filter(profile__pk=profile_pk)
        return profile_addresses


class ProfileAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def get_object(self):
        profile_pk = self.kwargs.get('pk')
        address_pk = self.kwargs.get('address_pk')
        profile_address = Address.objects.get(id=address_pk, profile__pk=profile_pk)
        return profile_address


class ProfileSummaryList(generics.ListAPIView):
    serializer_class = ProfileSummarySerializer
    queryset = Profile.objects.all()


class ProfileSummaryDetail(generics.RetrieveAPIView):
    serializer_class = ProfileSummarySerializer
    queryset = Profile.objects.all()


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })
