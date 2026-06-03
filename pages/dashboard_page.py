from pages.base_page import BasePage


class DashboardPage(BasePage):
    url_path = "/dashboard"

    HEADER = "h1[data-testid='dashboard-header']"
    USER_MENU = "[data-testid='user-menu']"
    ADD_TO_CART = "button[data-testid='add-to-cart']"
    CART_COUNT = "[data-testid='cart-count']"

    def is_loaded(self) -> bool:
        return self.is_visible(self.HEADER)

    def add_to_cart(self) -> None:
        self.click(self.ADD_TO_CART)

    def cart_count(self) -> str:
        return self.text_of(self.CART_COUNT)
