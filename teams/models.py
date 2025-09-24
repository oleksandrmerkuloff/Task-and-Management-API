from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Team(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    logo = models.ImageField(
        upload_to='None'  # add path
    )
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='teams'
    )
    members = models.ManyToManyField(
        User,
        through='TeamMembership',
    )

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class TeamMembership(models.Model):
    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
        )
    join_date = models.DateField(
        auto_now_add=True,
        editable=False
        )
    role = models.CharField(
        max_length=50,
        choices=[
            ('member', 'Member')  # Add more roles later
        ],
        default='member'
    )

    class Meta:
        unique_together = [['member', 'team']]
