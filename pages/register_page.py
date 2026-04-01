from playwright.sync_api import Page, Locator

class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.name_input: Locator = page.locator('input[data-qa="signup-name"]')
        self.email_input: Locator = page.locator('input[data-qa="signup-email"]')
        self.sign_up_button: Locator = page.locator('button[data-qa="signup-button"]')

    # Метод регистрации нового пользователя
    def register_new_user(self, name: str, email: str):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.sign_up_button.click()