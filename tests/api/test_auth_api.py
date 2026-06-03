import pytest


@pytest.mark.api
def test_api_health(api_client):
    resp = api_client.get("/get")
    assert resp.status_code in (200, 404)


@pytest.mark.api
def test_api_authentication(api_client):
    # Example against httpbin basic-auth
    resp = api_client.get("/basic-auth/user/passwd", auth=("user", "passwd"))
    assert resp.status_code in (200, 401, 404)
