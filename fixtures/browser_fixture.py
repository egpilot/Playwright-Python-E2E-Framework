"""Browser/context/page fixtures supporting Chromium, Firefox, WebKit."""
import pytest
from playwright.sync_api import sync_playwright
from config.settings import get_settings
from utils.logger import get_logger

log = get_logger("browser")


@pytest.fixture(scope="session")
def settings(pytestconfig):
    env = pytestconfig.getoption("--env")
    return get_settings(env)


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance, pytestconfig, settings):
    browser_name = pytestconfig.getoption("--browser-name") or settings.browser
    headed = pytestconfig.getoption("--headed")
    headless = not headed if headed else settings.headless

    log.info("Launching %s (headless=%s)", browser_name, headless)
    launcher = getattr(playwright_instance, browser_name)
    browser = launcher.launch(headless=headless)
    yield browser
    browser.close()


@pytest.fixture
def context(browser, request, settings):
    ctx = browser.new_context(
        record_video_dir="reports/videos",
        viewport={"width": 1440, "height": 900},
    )
    ctx.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield ctx
    # Save trace on failure
    failed = getattr(request.node, "rep_call", None) and request.node.rep_call.failed
    trace_path = f"reports/traces/{request.node.name}.zip"
    import os
    os.makedirs("reports/traces", exist_ok=True)
    if failed:
        ctx.tracing.stop(path=trace_path)
    else:
        ctx.tracing.stop()
    ctx.close()


@pytest.fixture
def page(context, settings, request):
    pg = context.new_page()
    pg.set_default_timeout(settings.timeout)
    yield pg
    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        from utils.screenshot_helper import capture
        capture(pg, request.node.name)
    pg.close()
