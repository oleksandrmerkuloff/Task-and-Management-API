from rest_framework import serializers

from teams.models import Team, TeamMembership
from users.serializers import UserSerializer


class TeamMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=True)

    class Meta:
        model = TeamMembership
        fields = '__all__'
        read_only_fields = ('id',)


class TeamSerializer(serializers.ModelSerializer):
    memberships = TeamMembershipSerializer(read_only=True, many=True)

    class Meta:
        model = Team
        fields = '__all__'


class TeamMembershipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembership
        fields = ["id", "team", "user", "role"]
