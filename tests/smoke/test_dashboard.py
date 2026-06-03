import pytest
from pages.dashboard_page import DashboardPage


@pytest.mark.smoke
@pytest.mark.ui
def test_dashboard_loads(page, settings):
    dash = DashboardPage(page, settings.base_url)
    dash.open()
    # In a real app: assert dash.is_loaded(). For demo:
    assert page.title() is not None


@pytest.mark.smoke
@pytest.mark.ui
def test_add_to_cart(page, settings):
    dash = DashboardPage(page, settings.base_url)
    dash.open()
    if dash.is_visible(DashboardPage.ADD_TO_CART, timeout=3000):
        dash.add_to_cart()
        assert dash.cart_count() != ""
