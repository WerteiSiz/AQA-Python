from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page, base_url: str = "https://www.saucedemo.com"):
        self.page = page
        self.base_url = base_url
        self.username_selector = "#user-name"
        self.password_selector = "#password"
        self.login_btn_selector = "#login-button"
        self.error_selector = "h3[data-test='error'], .error-message-container h3, .error-message-container"

    def open(self) -> None:
        self.page.goto(self.base_url)

    def login(self, username: str | None, password: str | None) -> None:
        if username is not None:
            self.page.fill(self.username_selector, username)
        if password is not None:
            self.page.fill(self.password_selector, password)
        self.page.click(self.login_btn_selector)

    def is_error_visible(self, timeout: int = 2000) -> bool:
        try:
            self.page.locator(self.error_selector).first.wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False

    def get_error_text(self) -> str | None:
        try:
            return self.page.locator(self.error_selector).first.text_content()
        except Exception:
            return None
