from pages.base_page import BasePage


class LoginPage(BasePage):
    url_path = "/login"

    # Centralized locators
    USERNAME = "#username"
    PASSWORD = "#password"
    SUBMIT = "button[type='submit']"
    ERROR = "[data-testid='login-error']"

    def login(self, username: str, password: str) -> None:
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def get_error(self) -> str:
        return self.text_of(self.ERROR)
