from rest_framework import generics


from projects.models import Project, Task
from projects.serializers import ProjectSerializer, TaskSerializer
from projects.permissions import ProjectPermission, TaskPermission


class ProjectsListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [ProjectPermission]

    def perform_create(self, serializer):
        serializer.save(
            team=self.kwargs['team']
        )


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [ProjectPermission]


class TasksListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [TaskPermission]

    def perform_create(self, serializer):
        serializer.save(
            project=self.kwargs['project']
        )


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [TaskPermission]
