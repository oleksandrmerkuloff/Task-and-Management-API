from rest_framework import generics

from tasks.models import Project, Task, Comment
from tasks.serializers import ProjectSerializer, TaskSerializer
from tasks.serializers import CommentSerializer


class ProjectsView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TasksView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


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
