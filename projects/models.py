from django.db import models

from teams.models import Team


class Project(models.Model):
    name = models.CharField(
        max_length=75,
        null=False,
        blank=False
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    deadline = models.DateField(
        blank=True,
        null=True,
        db_index=True
    )
    status = models.TextField(
        blank=False,
        null=False,
        max_length=40,
        choices=[
            ('plan', 'Planning'),
            ('dev', 'Development'),
            ('test', 'Testing'),
            ('review', 'Review'),
            ('done', 'Done'),
        ],
        default='plan',
        db_index=True
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_index=True,
        related_name='projects'
    )

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['deadline', '-created_at']

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'Current status for {self.name} is {self.status}'


class Task(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=75
    )
    content = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(
        null=True,
        blank=True,
        db_index=True
    )
    status = models.CharField(
        max_length=40,
        choices=[
            ('todo', 'To Do'),
            ('progress', 'In Progress'),
            ('done', 'Done'),
        ],
        default='todo',
        db_index=True
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        db_index=True,
        related_name='tasks'
    )

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'{self.name} part of {self.project.name} project.'

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ["deadline", "-created_at"]
