from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Team(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    logo = models.ImageField(
        upload_to='teams/logos/'
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
        ordering = ['name', '-created_at']

    def __str__(self) -> str:
        return self.name.title()

    def __repr__(self) -> str:
        amount_of_member = len(self.members.all()) + 1
        return f'{self.name.title()} includes {amount_of_member} members'


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
            ('trainee', 'Trainee'),
            ('manager', 'Manager'),
            ('jun', 'Junior'),
            ('mid', 'Middle'),
            ('sen', 'Senior'),
            ('lead', 'Team Lead'),
            ('arch', 'Architect')
        ],
        default='trainee'
    )

    class Meta:
        unique_together = [['member', 'team']]
        ordering = ['-join_date']

    def __str__(self) -> str:
        team_name = self.team.name
        return f'{self.member.full_name} joined to the {team_name} on {self.role} position'
