from rest_framework import serializers
from django.contrib.auth import get_user_model

from teams.models import Team, TeamMembership, Position
from users.serializers import UserSerializer


User = get_user_model()


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
        read_only_fields = ('id',)


class TeamsSerializer(serializers.ModelSerializer):
    leader = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True
    )
    leader_info = UserSerializer(read_only=True)

    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'created_at',
            'leader',
            'leader_info',
        )
        read_only_fields = (
            'id',
            'created_at'
        )


class TeamMembershipSerializer(serializers.ModelSerializer):
    member = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True
        )
    member_info = UserSerializer(read_only=True)
    team = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        write_only=True
    )
    team_name = serializers.StringRelatedField(read_only=True)
    position = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TeamMembership
        fields = (
            'id',
            'join_date',
            'experience',
            'position',
            'member',
            'member_info',
            'team',
            'team_name',
            'position',
        )
        read_only_fields = ('id', 'join_date',)
