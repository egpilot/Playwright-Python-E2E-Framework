from pages.base_page import BasePage


class CheckoutPage(BasePage):
    url_path = "/checkout"

    NAME = "#full-name"
    ADDRESS = "#address"
    CARD = "#card-number"
    PLACE_ORDER = "button[data-testid='place-order']"
    CONFIRMATION = "[data-testid='order-confirmation']"

    def fill_details(self, name: str, address: str, card: str) -> None:
        self.fill(self.NAME, name)
        self.fill(self.ADDRESS, address)
        self.fill(self.CARD, card)

    def place_order(self) -> None:
        self.click(self.PLACE_ORDER)

    def confirmation_text(self) -> str:
        return self.text_of(self.CONFIRMATION)
