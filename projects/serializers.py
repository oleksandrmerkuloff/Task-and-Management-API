from rest_framework import serializers

from projects.models import Project, Task
from teams.serializers import TeamsSerializer
from teams.models import Team


class ProjectSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        write_only=True
    )
    team_info = TeamsSerializer(read_only=True)

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'description',
            'created_at',
            'updated_at',
            'deadline',
            'status',
            'team',
            'team_info',
        )
        read_only_fields = ('id', 'created_at', 'updated_at')


class TaskSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        write_only=True
    )

    project_info = ProjectSerializer(read_only=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'name',
            'content',
            'created_at',
            'deadline',
            'status',
            'project',
            'project_info',
        )
        read_only_fields = ('id', 'created_at')
