from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser


from teams.models import Team, TeamMembership
from teams.serializers import TeamsSerializer, TeamMembershipSerializer
from teams.serializers import TeamMembershipCreateSerializer


class TeamsListView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TeamDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamsSerializer


class TeamMembersView(ListCreateAPIView):
    serializer_class = TeamMembershipSerializer
    permission_classes = [IsAdminUser,]

    def get_queryset(self):
        team_id = self.kwargs['pk']
        return TeamMembership.objects.filter(team_id=team_id)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TeamMembershipCreateSerializer
        return TeamMembershipSerializer

    def perform_create(self, serializer):
        team_id = self.kwargs['pk']
        serializer.save(team_id=team_id)
