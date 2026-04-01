from playwright.sync_api import Page, Locator, expect


class ContactUsPage:
    def __init__(self, page: Page):
        self.page = page
        self.contact_form: Locator = page.locator('form#contact-form')
        self.name_input: Locator = page.locator('input[name="name"]')
        self.email_input: Locator = page.locator('input[name="email"]')
        self.message_input: Locator = page.locator('textarea[name="message"]')
        self.upload_file: Locator = page.locator('input[name="upload_file"]')
        self.submit_button: Locator = page.locator('input[type="submit"]')
        self.success_alert: Locator = page.locator('.alert-success')
        self.contact_link: Locator = page.locator('a[href="/contact_us"]')

    def goto(self) -> "ContactUsPage":
        """Navigate to the contact us page via home page."""
        self.page.goto("https://automationexercise.com")
        self.contact_link.click()
        return self

    def fill_contact_form(self, name: str, email: str, message: str):
        """Fill the contact form with provided data."""
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.message_input.fill(message)
        return self

    def submit(self):
        """Submit the contact form."""
        self.submit_button.click()

    def is_success_message_visible(self) -> bool:
        """Check if success message is visible."""
        try:
            expect(self.page.locator('.alert-success').last).to_be_visible(timeout=5000)
            return True
        except AssertionError:
            return False

    def get_success_message(self) -> str:
        """Get the success message text."""
        return self.page.locator('.alert-success').last.inner_text()
