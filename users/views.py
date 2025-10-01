from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    )
from rest_framework.permissions import IsAdminUser, AllowAny

from users.serializers import UserSerializer, RegisterSerializer
from users.models import CustomUser


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny,]


class UsersListView(ListCreateAPIView):
    queryset = CustomUser.objects.all().order_by('email')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser,]


class UsersDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser,]
