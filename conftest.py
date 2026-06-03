"""Root conftest: CLI options, fixture wiring, failure hooks."""
import os
import pytest

# Re-export fixtures
from fixtures.browser_fixture import (  # noqa: F401
    settings,
    playwright_instance,
    browser,
    context,
    page,
)
from fixtures.api_fixture import api_client, authenticated_api  # noqa: F401


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default=os.getenv("TEST_ENV", "qa"),
                     help="Environment: dev | qa | prod")
    parser.addoption("--browser-name", action="store", default=None,
                     help="Browser: chromium | firefox | webkit")
    # parser.addoption("--headed", action="store_true", default=False,
    #                  help="Run in headed mode")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Expose test result on the request.node for fixtures to inspect."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture
def page_with_screenshot(page, request):
    yield page

    page.screenshot(
        path=f"screenshots/{request.node.name}.png",
        full_page=True
    )
