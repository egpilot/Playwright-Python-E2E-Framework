"""BasePage with shared interactions, explicit waits, logging."""
from __future__ import annotations
from playwright.sync_api import Page, Locator
from utils.logger import get_logger

log = get_logger("page")


class BasePage:
    """All page objects inherit from BasePage."""

    url_path: str = "/"

    def __init__(self, page: Page, base_url: str = "") -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")

    # ------------ navigation ------------
    def open(self, path: str | None = None) -> None:
        target = (self.base_url + (path or self.url_path)) if not (path or "").startswith("http") else path
        log.info("Navigating to %s", target)
        self.page.goto(target, wait_until="domcontentloaded")

    # ------------ interactions ------------
    def find(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def click(self, selector: str, timeout: int = 15000) -> None:
        log.info("Click %s", selector)
        self.page.locator(selector).click(timeout=timeout)

    def fill(self, selector: str, value: str, timeout: int = 15000) -> None:
        log.info("Fill %s", selector)
        self.page.locator(selector).fill(value, timeout=timeout)

    def type_text(self, selector: str, value: str, delay: int = 50) -> None:
        log.info("Type into %s", selector)
        self.page.locator(selector).type(value, delay=delay)

    def text_of(self, selector: str, timeout: int = 15000) -> str:
        return self.page.locator(selector).inner_text(timeout=timeout)

    def is_visible(self, selector: str, timeout: int = 5000) -> bool:
        try:
            self.page.locator(selector).wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False

    def press(self, selector: str, key: str) -> None:
        self.page.locator(selector).press(key)

    def title(self) -> str:
        return self.page.title()

    def current_url(self) -> str:
        return self.page.url
