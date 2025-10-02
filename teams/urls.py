from django.urls import path

from teams import views as v


urlpatterns = [
    path('', v.TeamsListView.as_view(), name='teams-list'),
    path('<int:team_id>/', v.TeamDetailView.as_view(), name='team-detail'),
    path(
        '<int:team_id>/members/',
        v.TeamMembersView.as_view(),
        name='team-members'
        ),
    path(
        '<int:team_id>/members/<int:user_id>/',
        v.TeamMemberDetailView.as_view(),
        name='member-detail',
    )
]
