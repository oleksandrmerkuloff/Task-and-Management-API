from django.db import models
from django.contrib.auth import get_user_model

from teams.models import Team


User = get_user_model()


class Project(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateField(
        blank=True,
        null=True,
        db_index=True
    )
    status = models.CharField(
        max_length=40,
        choices=[
            ('plan', 'Planning'),
            ('dev', 'Development'),
            ('test', 'Testing'),
            ('review', 'Review'),
            ('done', 'Done')
        ],
        default='plan'
    )
    creator = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='projects'
        )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['deadline', '-created_at']

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'{self.name} has status {self.status}'


class Task(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=100
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    deadline = models.DateField(
        blank=True,
        null=True,
        db_index=True
    )
    status = models.CharField(
        max_length=40,
        choices=[
            ('todo', 'To Do'),
            ('in_progress', 'In Progress'),
            ('done', 'Done')
            ],
        default='todo'
    )
    creator = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='created_tasks'
    )
    members = models.ManyToManyField(
        User,
        related_name='assigned_tasks'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks',
        db_index=True
        )

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'{self.name} created by: {self.creator}'

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ["deadline", "-created_at"]


class Comment(models.Model):
    content = models.CharField(
        blank=False,
        null=False,
        max_length=150
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
        )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments'
        )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
        )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'Comment created by {self.user.full_name}'
