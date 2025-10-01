from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from tasks.models import Project, Task, Comment
from tasks.serializers import ProjectSerializer, TaskSerializer
from tasks.serializers import CommentSerializer


class ProjectsListView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all().order_by('created_at')

    def perform_create(self, serializer):
        serializer.save(
            creator=self.request.user,
            team=self.kwargs['team']
        )


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser]


class TasksListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProjectTasksListView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser,]

    def get_queryset(self):
        project_id = self.kwargs['pk']
        return Task.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        serializer.save(
            creator=self.request.user,
            project_id=self.kwargs['pk']
        )


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser,]


class CommentsListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return Comment.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            task_id=self.kwargs['task_id']
        )


class CommentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
