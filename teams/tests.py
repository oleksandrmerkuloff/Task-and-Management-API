from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

from teams.models import Team


User = get_user_model()


class TeamAPITestCase(APITestCase):
    def setUp(self):
        # Admin user
        self.admin = User.objects.create_superuser(
            email="admin@example.com",
            first_name='Admin',
            last_name='Tester',
            password="adminpass",
        )  # type: ignore

        # Regular user (will be leader)
        self.leader = User.objects.create_user(
            email="leader@example.com",
            first_name='Leader',
            last_name='Tester',
            password="leaderpass",
        )  # type: ignore

        # Another user (team member)
        self.member = User.objects.create_user(
            email="member@example.com",
            first_name='Member',
            last_name='Tester',
            password="memberpass",
        )  # type: ignore

        # Outsider
        self.outsider = User.objects.create_user(
            email="outsider@example.com",
            first_name='Outsider',
            last_name='Tester',
            password="outsiderpass",
        )  # type: ignore

        # Create a team with leader + member
        self.team = Team.objects.create(name="Dev Team", leader=self.leader)
        self.team.members.add(self.member)

    def test_admin_can_create_team(self):
        self.client.force_authenticate(user=self.admin)
        url = reverse("teams-list")
        data = {"name": "New Team", "leader": self.leader.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)

    def test_non_admin_cannot_create_team(self):
        self.client.force_authenticate(user=self.member)
        url = reverse("teams-list")
        data = {"name": "Hacker Team", "leader": self.member.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_team_leader_can_update_team(self):
        self.client.force_authenticate(user=self.leader)
        url = reverse("team-detail", args=[self.team.id])
        data = {"name": "Updated Dev Team", "leader": self.leader.id}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.team.refresh_from_db()
        self.assertEqual(self.team.name, "Updated Dev Team")

    def test_member_cannot_update_team(self):
        self.client.force_authenticate(user=self.member)
        url = reverse("team-detail", args=[self.team.id])
        data = {"name": "Illegal Update"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_outsider_cannot_view_team_detail(self):
        self.client.force_authenticate(user=self.outsider)
        url = reverse("team-detail", args=[self.team.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_team_member_can_view_team_detail(self):
        self.client.force_authenticate(user=self.member)
        url = reverse("team-detail", args=[self.team.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.team.id)
