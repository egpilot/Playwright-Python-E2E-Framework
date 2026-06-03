"""Basic sanity test: open Google and type 'automation' in the search bar."""
import pytest


@pytest.mark.smoke
@pytest.mark.ui
def test_google_search_automation(page):
    page.goto("https://www.google.com", wait_until="domcontentloaded")

    # Accept consent banner if shown (EU)
    for label in ["I agree", "Accept all", "Reject all"]:
        btn = page.get_by_role("button", name=label)
        if btn.count() > 0:
            try:
                btn.first.click(timeout=2000)
                break
            except Exception:
                pass

    search = page.locator("textarea[name='q'], input[name='q']").first
    search.wait_for(state="visible", timeout=15000)
    search.fill("automation")
    assert search.input_value() == "automation"

    search.press("Enter")
    page.wait_for_load_state("domcontentloaded")
    assert "automation" in page.url.lower() or "automation" in page.title().lower()
