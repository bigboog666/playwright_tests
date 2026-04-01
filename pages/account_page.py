from playwright.sync_api import Page, Locator, expect


class AccountPage:
    """Page object for logged-in user account page."""

    def __init__(self, page: Page):
        self.page = page
        self.delete_account_button: Locator = page.locator('a[data-qa="delete-account"]')
        self.continue_button: Locator = page.locator('a[href="/"]')
        self.account_deleted_label: Locator = page.locator('h2[data-qa="account-deleted"]')
        self.logged_in_as: Locator = page.locator('header a[href="/logout"]').first

    def click_delete_account(self):
        """Click the delete account button."""
        self.delete_account_button.click()

    def click_continue(self):
        """Click the continue button after deletion."""
        self.continue_button.click()

    def is_account_deleted_visible(self) -> bool:
        """Check if account deleted message is visible."""
        try:
            expect(self.account_deleted_label).to_be_visible(timeout=5000)
            return True
        except AssertionError:
            return False

    def is_logged_in(self) -> bool:
        """Check if user is logged in."""
        try:
            expect(self.logged_in_as).to_be_visible(timeout=3000)
            return True
        except AssertionError:
            return False
