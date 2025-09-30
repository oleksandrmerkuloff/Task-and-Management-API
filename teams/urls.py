from django.urls import path

from teams import views as v


urlpatterns = [
    path('', v.TeamsListView.as_view(), name='teams-list'),
    path('<int:pk>/', v.TeamDetailView.as_view(), name='team-detail'),
    path('<int:pk>/members/', v.TeamMembersView.as_view(), name='team-members'),
]
