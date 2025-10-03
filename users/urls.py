from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)

from users.views import UsersDetailView, UsersListView, RegisterView


urlpatterns = [
    path('', UsersListView.as_view(), name='users-list'),
    path('<int:pk>/', UsersDetailView.as_view(), name='user-detail'),
    path('register/', RegisterView.as_view(), name='registration'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh-token')
]
