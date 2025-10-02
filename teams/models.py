from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Position(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'


class Team(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    leader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='teams'
    )
    members = models.ManyToManyField(
        User,
        through='TeamMembership',
        related_name='teams'
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
    join_date = models.DateField(
        auto_now_add=True,
        editable=False
        )
    experience = models.CharField(
        max_length=50,
        choices=[
            ('trainee', 'Trainee'),
            ('jun', 'Junior'),
            ('mid', 'Middle'),
            ('sen', 'Senior'),
            ('lead', 'Team Lead'),
        ],
        default='trainee'
    )
    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
        )
    position = models.ForeignKey(
        Position,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='members'
    )

    def __str__(self) -> str:
        return f'{self.member.full_name} from {self.team.name} team.'

    class Meta:
        unique_together = [['member', 'team']]
        ordering = ['-join_date']
