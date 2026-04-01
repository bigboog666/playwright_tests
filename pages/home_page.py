from playwright.sync_api import Page, Locator

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        # Локатор кнопки "Signup / Login"
        self.sign_up_login_button: Locator = page.locator('a[href="/login"]')
        # Локатор логотипа главной страницы
        self.home_logo: Locator = page.locator('img[src="/static/images/home/logo.png"]')

    # Метод перехода на главную страницу
    def goto(self):
        self.page.goto("https://automationexercise.com")

    # Метод клика по кнопке "Signup / Login"
    def click_sign_up_login(self):
        self.sign_up_login_button.click()