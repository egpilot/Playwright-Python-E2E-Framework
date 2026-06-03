"""Explicit-wait helpers built on Playwright."""
from playwright.sync_api import Page, Locator, TimeoutError as PWTimeout
from utils.logger import get_logger

log = get_logger("waits")


def wait_for_visible(page: Page, selector: str, timeout: int = 15000) -> Locator:
    loc = page.locator(selector)
    loc.wait_for(state="visible", timeout=timeout)
    return loc


def wait_for_hidden(page: Page, selector: str, timeout: int = 15000) -> None:
    page.locator(selector).wait_for(state="hidden", timeout=timeout)


def wait_for_url_contains(page: Page, fragment: str, timeout: int = 15000) -> None:
    try:
        page.wait_for_url(lambda url: fragment in url, timeout=timeout)
    except PWTimeout:
        log.error("URL did not contain %r within %sms (current=%s)", fragment, timeout, page.url)
        raise
