"""Basic sanity test: open DuckDuckGo and type 'automation' in the search bar."""

import pytest



@pytest.mark.smoke
@pytest.mark.ui
def test_duckduckgo_search_automation(page_with_screenshot):
    page = page_with_screenshot

    page.goto(
        "https://duckduckgo.com/",
        wait_until="domcontentloaded"
    )

    search = page.locator(
        "input[name='q']"
    ).first

    search.wait_for(
        state="visible",
        timeout=15000
    )

    # write like a human being
    search.press_sequentially(
        "automation",
        delay=120
    )

    assert search.input_value() == "automation"

    search.press("Enter")

    page.wait_for_load_state("domcontentloaded")

    assert (
        "automation" in page.url.lower()
        or "automation" in page.title().lower()
    )

    page.wait_for_timeout(5000)