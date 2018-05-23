from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import generics

from .serializers import UserSerializer
from .models import User


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'users': reverse(UserList.name,
                                 request=request),
            }
        )


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
