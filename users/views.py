from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from users.serializers import UserSerializer
from users.models import CustomUser


class UsersListView(ListCreateAPIView):
    queryset = CustomUser.objects.all().order_by('email')
    serializer_class = UserSerializer


class UsersDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
