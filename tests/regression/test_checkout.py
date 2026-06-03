import json
from pathlib import Path
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.checkout_page import CheckoutPage

DATA = json.loads((Path(__file__).resolve().parents[2] / "data" / "test_data.json").read_text())


@pytest.mark.regression
@pytest.mark.ui
def test_checkout_flow(page, settings):
    login = LoginPage(page, settings.base_url)
    login.open()
    user = DATA["valid_user"]
    login.login(user["username"], user["password"])

    dash = DashboardPage(page, settings.base_url)
    if dash.is_visible(DashboardPage.ADD_TO_CART, timeout=3000):
        dash.add_to_cart()

    checkout = CheckoutPage(page, settings.base_url)
    checkout.open()
    c = DATA["checkout"]
    if checkout.is_visible(CheckoutPage.NAME, timeout=3000):
        checkout.fill_details(c["name"], c["address"], c["card"])
        checkout.place_order()
        assert checkout.is_visible(CheckoutPage.CONFIRMATION, timeout=10000)
