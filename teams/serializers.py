from rest_framework import serializers

from teams.models import Team, TeamMembership
from users.serializers import UserSerializer


class TeamsSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'owner', 'members')


class TeamMembershipSerializer(serializers.ModelSerializer):
    member = UserSerializer(read_only=True)
    team = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TeamMembership
        fields = '__all__'
        read_only_fields = ('id', 'join_date', 'team')


class TeamMembershipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembership
        fields = ['id', 'member', 'role']
