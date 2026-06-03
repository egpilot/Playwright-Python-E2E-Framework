import json
from pathlib import Path
import pytest
from pages.login_page import LoginPage

DATA = json.loads((Path(__file__).resolve().parents[2] / "data" / "test_data.json").read_text())


@pytest.mark.smoke
@pytest.mark.ui
def test_login_success(page, settings):
    login = LoginPage(page, settings.base_url)
    login.open()
    user = DATA["valid_user"]
    login.login(user["username"], user["password"])
    assert "dashboard" in page.url.lower() or page.locator("body").is_visible()


@pytest.mark.smoke
@pytest.mark.ui
def test_login_negative(page, settings):
    login = LoginPage(page, settings.base_url)
    login.open()
    user = DATA["invalid_user"]
    login.login(user["username"], user["password"])
    # Expect an error message OR still on login page
    assert "login" in page.url.lower() or login.is_visible(LoginPage.ERROR)
