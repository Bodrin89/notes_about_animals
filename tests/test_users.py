import pytest
from django.urls import reverse

from config.settings import LOGGER


@pytest.mark.django_db
class TestUser:

    url_signup = reverse('apps.users:create-user')
    url_login = reverse('apps.users:login-user')
    url_logout = reverse('apps.users:logout-user')


    def test_signup(self, client, user):
        """Тест создания нового пользователя и его авторизацию"""
        data = {'username': 'user.username',
                'email': user.email,
                'password': user.password,
                'password_repeat': user.password}

        response = client.post(self.url_signup, data=data)
        response_login = client.post(self.url_login, data={'username': 'user.username', 'password': user.password})
        assert response.status_code == 201
        assert response.data == {'id': response.data['id'], 'username': data['username'], 'email': data['email']}

        assert response_login.status_code == 200
        assert response_login.data == {'id': response_login.data['id'],
                                       'username': data['username'],
                                       'email': data['email']}

    def test_logout(self, client, user):
        response = client.post(self.url_logout)
        assert response.status_code == 200
        assert response.data == {"detail": "Logged out successfully."}
