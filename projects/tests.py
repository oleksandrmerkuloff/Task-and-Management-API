from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from teams.models import Team
from projects.models import Project, Task


User = get_user_model()


class ProjectAPITestCase(APITestCase):
    def setUp(self):
        # Create admin
        self.admin = User.objects.create_superuser(
            email="admin@test.com",
            first_name='Admin',
            last_name='Tester',
            password="adminpass"
        )

        # Create leader
        self.leader = User.objects.create_user(
            email="leader@test.com",
            first_name='Leader',
            last_name='Tester',
            password="leaderpass"
        )

        # Create member
        self.member = User.objects.create_user(
            email="member@test.com",
            first_name='Base',
            last_name='Tester',
            password="memberpass"
        )

        # Create outsider
        self.outsider = User.objects.create_user(
            email="outsider@test.com",
            first_name='NonAuth',
            last_name='Tester',
            password="outsiderpass"
        )

        # Create team
        self.team = Team.objects.create(name="Dev Team", leader=self.leader)
        self.team.members.add(self.member)

        # Create project
        self.project = Project.objects.create(
            name="Cool Project",
            description="Test project",
            team=self.team,
            status="plan"
        )

        # Endpoints
        self.projects_url = reverse("projects-list")
        self.project_detail_url = reverse("project-detail", kwargs={"project_id": self.project.id})
        self.tasks_url = reverse("tasks-list", kwargs={"project_id": self.project.id})

    def authenticate(self, user):
        self.client.force_authenticate(user=user)

    def test_admin_can_create_project(self):
        self.authenticate(self.admin)
        response = self.client.post(self.projects_url, {
            "name": "Admin Project",
            "description": "Created by admin",
            "team": self.team.id,
            "status": "plan"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_non_admin_cannot_create_project(self):
        self.authenticate(self.leader)
        response = self.client.post(self.projects_url, {
            "name": "Not Allowed",
            "description": "Leader tries to create",
            "team": self.team.id,
            "status": "plan"
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_team_member_can_view_project_detail(self):
        self.authenticate(self.member)
        response = self.client.get(self.project_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_outsider_cannot_view_project_detail(self):
        self.authenticate(self.outsider)
        response = self.client.get(self.project_detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_leader_can_update_project(self):
        self.authenticate(self.leader)
        response = self.client.patch(self.project_detail_url, {"status": "dev"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.project.refresh_from_db()
        self.assertEqual(self.project.status, "dev")

    def test_member_cannot_update_project(self):
        self.authenticate(self.member)
        response = self.client.patch(self.project_detail_url, {"status": "dev"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_leader_can_create_task(self):
        self.authenticate(self.leader)
        response = self.client.post(self.tasks_url, {
            "name": "Leader Task",
            "content": "Leader creates a task",
            "status": "todo",
            "project": self.project.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_member_can_create_task(self):
        self.authenticate(self.member)
        response = self.client.post(self.tasks_url, {
            "name": "Member Task",
            "content": "Member creates a task",
            "status": "todo",
            "project": self.project.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_outsider_cannot_create_task(self):
        self.authenticate(self.outsider)
        response = self.client.post(self.tasks_url, {
            "name": "Outsider Task",
            "content": "Should fail",
            "status": "todo",
            "project": self.project.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
