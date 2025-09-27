from django.urls import path

from users.views import UsersDetailView, UsersListView


urlpatterns = [
    path('', UsersListView.as_view(), name='users-list'),
    path('<int:pk>/', UsersDetailView.as_view(), name='user-detail'),
]
