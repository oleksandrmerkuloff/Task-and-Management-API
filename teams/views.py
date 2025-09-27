from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView


from teams.models import Team, TeamMembership
from teams.serializers import TeamMembership, TeamMembershipSerializer
from teams.serializers import TeamMembershipCreateSerializer, TeamSerializer


class TeamListCreateView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamMembershipListCreateView(ListCreateAPIView):
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembershipCreateSerializer


class TeamMembershipDetailView(RetrieveUpdateDestroyAPIView):
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembershipCreateSerialize
