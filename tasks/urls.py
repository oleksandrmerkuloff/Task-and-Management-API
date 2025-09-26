from django.urls import path

from tasks import views as v


urlpatterns = [
    path('', v.ProjectsListView.as_view(), name='projects-list'),
    path('<int:pk>', v.ProjectDetailView.as_view(), name='project-detail'),

    path('<int:pk>/tasks', v.TasksListView.as_view(), name='tasks-list'),
    path('tasks/<int:pk>', v.TaskDetailView.as_view(), name='task-detail'),
    # path('tasks/<int:id>/members', view, name='task-members'),
    # path('tasks/<int:id>/members/<int:user_id>', view, name='remove-member'),

    path(
        'tasks/<int:task_id>/comments',
        v.CommentsListView.as_view(),
        name='comments-list'
        ),
    path(
        'comments/<int:id>',
        v.CommentsDetailView.as_view(),
        name='comments-detail'
        ),
]
