from rest_framework import serializers

from tasks.models import Project, Task, Comment


class ProjectSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)
    team = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'creator']


class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    members = serializers.StringRelatedField(many=True, read_only=True)
    creator = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'project', 'creator']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    task = TaskSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'user', 'task']
