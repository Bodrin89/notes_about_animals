import pytest
from django.core.cache import cache
from rest_framework.test import APIClient


@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture
def get_auth_client(client: APIClient, user) -> APIClient:
    client.force_authenticate(user)
    return client


@pytest.fixture
def not_owner_auth_client(client: APIClient, user_not_owner_factory) -> APIClient:
    client.force_authenticate(user_not_owner_factory())
    return client


@pytest.fixture
def clear_cache():
    cache.clear()
