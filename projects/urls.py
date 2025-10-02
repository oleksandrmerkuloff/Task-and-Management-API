from django.urls import path

from projects import views as v


urlpatterns = [
    path('', v.ProjectsListView.as_view(), name='projects-list'),
    path(
        '<int:project_id>/',
        v.ProjectDetailView.as_view(),
        name='project-detail'
        ),
    path(
        '<int:project_id>/tasks/',
        v.TasksListView.as_view(),
        name='tasks-list'
    ),
    path(
        '<int:project_id>/tasks/<int:task_id>/',
        v.TaskDetailView.as_view(),
        name='task-detail'
    ),
]
