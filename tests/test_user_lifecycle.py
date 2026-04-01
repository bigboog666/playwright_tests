import pytest
import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.account_page import AccountPage


class TestUserLifecycle:
    """Tests for complete user lifecycle: register, login, delete."""

    @pytest.fixture
    def test_user(self):
        """Generate unique test user credentials."""
        timestamp = int(time.time())
        return {
            "name": f"Test User {timestamp}",
            "email": f"testuser{timestamp}@mail.com",
            "password": "SecurePass123!"
        }

    def test_full_registration_flow(self, page, test_user):
        """Test complete registration flow."""
        home = HomePage(page)
        register = RegisterPage(page)

        # Go to signup
        home.goto()
        home.click_sign_up_login()

        # Register new user
        register.register_new_user(test_user["name"], test_user["email"])

        # Check we're on the signup page
        assert page.locator('h2:has-text("Enter Account Information")').is_visible()

    def test_register_and_delete_account(self, page, test_user):
        """Test registering and then deleting account."""
        home = HomePage(page)
        register = RegisterPage(page)
        account = AccountPage(page)

        # Register
        home.goto()
        home.click_sign_up_login()
        register.register_new_user(test_user["name"], test_user["email"])

        # Complete registration
        page.locator('input[data-qa="signup-password"]').fill(test_user["password"])
        page.locator('button[data-qa="signup-button"]').click()

        # Verify logged in
        assert account.is_logged_in(), "User should be logged in after registration"

        # Delete account
        account.click_delete_account()
        assert account.is_account_deleted_visible(), "Account deleted message should appear"

        # Continue to home
        account.click_continue()
        assert home.home_logo.is_visible(), "Should be on home page"

    def test_login_after_registration(self, page, test_user):
        """Test logging in after registration."""
        home = HomePage(page)
        register = RegisterPage(page)
        login = LoginPage(page)
        account = AccountPage(page)

        # Register new user
        home.goto()
        home.click_sign_up_login()
        register.register_new_user(test_user["name"], test_user["email"])

        # Complete registration
        page.locator('input[data-qa="signup-password"]').fill(test_user["password"])
        page.locator('button[data-qa="signup-button"]').click()

        # Logout
        page.locator('header a[href="/logout"]').click()

        # Login again
        home.click_sign_up_login()
        login.login(test_user["email"], test_user["password"])

        # Verify logged in
        assert account.is_logged_in(), "User should be logged in"

    def test_logout_functionality(self, page, test_user):
        """Test logout functionality."""
        home = HomePage(page)
        register = RegisterPage(page)
        login = LoginPage(page)

        # Register and login
        home.goto()
        home.click_sign_up_login()
        register.register_new_user(test_user["name"], test_user["email"])
        page.locator('input[data-qa="signup-password"]').fill(test_user["password"])
        page.locator('button[data-qa="signup-button"]').click()

        # Logout
        page.locator('header a[href="/logout"]').click()

        # Verify logged out - should see login button
        login_button = page.locator('a[href="/login"]')
        assert login_button.is_visible(), "Login button should be visible after logout"
