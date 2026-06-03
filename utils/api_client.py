"""Thin wrapper around requests for API testing and auth helpers."""
from typing import Any, Optional
import requests
from utils.logger import get_logger

log = get_logger("api_client")


class APIClient:
    def __init__(self, base_url: str, timeout: int = 30) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def set_token(self, token: str, scheme: str = "Bearer") -> None:
        self.session.headers.update({"Authorization": f"{scheme} {token}"})

    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def request(self, method: str, path: str, **kwargs: Any) -> requests.Response:
        url = self._url(path)
        log.info("%s %s", method.upper(), url)
        resp = self.session.request(method, url, timeout=self.timeout, **kwargs)
        log.info("-> %s", resp.status_code)
        return resp

    def get(self, path: str, **kw: Any) -> requests.Response:
        return self.request("GET", path, **kw)

    def post(self, path: str, **kw: Any) -> requests.Response:
        return self.request("POST", path, **kw)

    def put(self, path: str, **kw: Any) -> requests.Response:
        return self.request("PUT", path, **kw)

    def delete(self, path: str, **kw: Any) -> requests.Response:
        return self.request("DELETE", path, **kw)

    def authenticate(
        self, username: str, password: str, path: str = "/auth/login"
    ) -> Optional[str]:
        """Generic username/password auth returning a bearer token."""
        resp = self.post(path, json={"username": username, "password": password})
        if resp.ok:
            token = resp.json().get("token") or resp.json().get("access_token")
            if token:
                self.set_token(token)
                return token
        return None
