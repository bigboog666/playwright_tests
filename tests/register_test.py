import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage

@pytest.mark.parametrize("name", ["John Doe"])
def test_register_new_user(page, name):
    home = HomePage(page)
    register = RegisterPage(page)

    # Переходим на главную страницу
    home.goto()

    # Проверяем, что логотип виден
    assert home.home_logo.is_visible()

    # Переходим на страницу регистрации
    home.click_sign_up_login()

    # Генерируем уникальный email для каждого теста
    import time
    random_email = f"test{int(time.time())}@mail.com"

    # Регистрируем нового пользователя
    register.register_new_user(name, random_email)

    # Проверяем, что открылась страница с подтверждением
    assert page.locator('h2:has-text("Enter Account Information")').is_visible()