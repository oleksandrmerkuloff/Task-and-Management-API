from rest_framework import generics

from teams.models import Team, TeamMembership
from teams.serializers import TeamsSerializer, TeamMembershipSerializer
from teams.permissions import TeamPermission, MembershipPermission


class TeamsListView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamsSerializer
    permission_classes = [TeamPermission]

    def perform_create(self, serializer):
        serializer.save(leader=self.request.user)


class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamsSerializer
    permission_classes = [TeamPermission]
    lookup_url_kwarg = 'team_id'


class TeamMembersView(generics.ListCreateAPIView):
    serializer_class = TeamMembershipSerializer
    permission_classes = [MembershipPermission]

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        return TeamMembership.objects.filter(team_id=team_id)

    def perform_create(self, serializer):
        team_id = self.kwargs['team_id']
        serializer.save(team_id=team_id)


class TeamMemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembership
    permission_classes = [MembershipPermission]
