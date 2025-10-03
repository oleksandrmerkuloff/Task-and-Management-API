from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase


CustomUser = get_user_model()


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.admin = CustomUser.objects.create_superuser(
            email='admin@example.com',
            first_name='Admin',
            last_name='User',
            password='adminpass'
        )  # type: ignore

        self.user = CustomUser.objects.create_user(
            email='user@example.com',
            first_name='Regular',
            last_name='User',
            password='userpass'
        )  # type: ignore

        self.register_url = reverse('registration')
        self.users_list_url = reverse('users-list')
        self.user_detail_url = reverse('user-detail', args=[self.user.id])
        self.refresh_url = reverse('refresh-token')

    def authenticate(self, email, password):
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {
            'email': email,
            'password': password,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_user_can_register_and_get_tokens(self):
        payload = {
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'password': 'newpass123'
        }
        response = self.client.post(self.register_url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertTrue(CustomUser.objects.filter(email='newuser@example.com').exists())

    def test_admin_can_list_users(self):
        self.authenticate('admin@example.com', 'adminpass')
        response = self.client.get(self.users_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_regular_user_cannot_list_users(self):
        self.authenticate("user@example.com", "userpass")
        response = self.client.get(self.users_list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_view_user_detail(self):
        self.authenticate('admin@example.com', 'adminpass')
        response = self.client.get(self.user_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'user@example.com')

    def test_regular_user_cannot_view_other_user_detail(self):
        self.authenticate('user@example.com', 'userpass')
        response = self.client.get(self.user_detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_update_user(self):
        self.authenticate('admin@example.com', 'adminpass')
        response = self.client.patch(self.user_detail_url, {'email': 'updated@example.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'updated@example.com')

    def test_regular_user_cannot_update_other_user(self):
        self.authenticate('user@example.com', 'userpass')
        response = self.client.patch(self.user_detail_url, {'email': 'hack@example.com'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_refresh_token(self):
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {
            'email': 'user@example.com',
            'password': 'userpass'
        })
        refresh = response.data['refresh']
        response = self.client.post(self.refresh_url, {'refresh': refresh})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
