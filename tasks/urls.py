from django.urls import path

from tasks import views as v


urlpatterns = [
    path('', v.ProjectsView.as_view(), name='projects-list'),
    path('tasks/', v.TasksView.as_view(), name='task-list'),
    path(
        'tasks/<int:task_id>/comments/',
        v.CommentsListView.as_view(),
        name='comments-list'
        ),
    path(
        'comments/<int:pk>/',
        v.CommentsDetailView.as_view(),
        name='comment-detail'
        )
]
