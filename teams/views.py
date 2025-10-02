from rest_framework import generics

from teams.models import Team, TeamMembership
from teams.serializers import TeamsSerializer, TeamMembershipSerializer


class TeamsListView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamsSerializer

    def perform_create(self, serializer):
        serializer.save(leader=self.request.user)


class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamsSerializer


class TeamMembersView(generics.ListCreateAPIView):
    serializer_class = TeamMembershipSerializer

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        return TeamMembership.objects.filter(team_id=team_id)

    def perform_create(self, serializer):
        team_id = self.kwargs['team_id']
        serializer.save(team_id=team_id)


class TeamMemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembership
