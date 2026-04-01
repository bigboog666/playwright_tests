from playwright.sync_api import Page, Locator, expect


class LoginPage:
    URL = "https://automationexercise.com/login"

    def __init__(self, page: Page):
        self.page = page
        self.login_email: Locator = page.locator('input[data-qa="login-email"]')
        self.login_password: Locator = page.locator('input[data-qa="login-password"]')
        self.login_button: Locator = page.locator('button[data-qa="login-button"]')
        self.logged_in_user: Locator = page.locator('header a[href="/logout"]').first
        self.login_error: Locator = page.locator('.login-form p').first

    def goto(self) -> "LoginPage":
        """Navigate to the login page."""
        self.page.goto(self.URL)
        return self

    def login(self, email: str, password: str) -> "LoginPage":
        """Log in with email and password."""
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()
        return self

    def is_logged_in(self) -> bool:
        """Check if user is logged in."""
        try:
            expect(self.logged_in_user).to_be_visible(timeout=5000)
            return True
        except AssertionError:
            return False

    def get_login_error(self) -> str:
        """Get login error message if any."""
        try:
            expect(self.login_error).to_be_visible(timeout=2000)
            return self.login_error.inner_text()
        except AssertionError:
            return ""