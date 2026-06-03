"""API client fixtures."""
import pytest
from utils.api_client import APIClient


@pytest.fixture(scope="session")
def api_client(settings):
    return APIClient(settings.api_base_url, timeout=30)


@pytest.fixture(scope="session")
def authenticated_api(api_client, settings):
    token = api_client.authenticate(settings.username, settings.password)
    if token:
        api_client.set_token(token)
    return api_client
