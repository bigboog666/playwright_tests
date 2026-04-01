import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_login_invalid_credentials(page):
    """Test that login fails with invalid credentials."""
    home = HomePage(page)
    login = LoginPage(page)

    # Переходим на страницу логина через главную
    home.goto()
    home.click_sign_up_login()

    # Вводим неверные данные
    login.login("wrong@email.com", "wrongpass")

    # Проверяем, что появилась ошибка
    error = login.get_login_error()
    assert error != "", "Should show error message for invalid credentials"
    assert "incorrect" in error.lower(), f"Error should mention incorrect credentials: {error}"


def test_login_form_visible(page):
    """Test that login form is visible on the login page."""
    home = HomePage(page)
    login = LoginPage(page)

    # Переходим на страницу логина через главную
    home.goto()
    home.click_sign_up_login()

    # Проверяем, что форма логина видима
    assert login.login_email.is_visible(), "Email input should be visible"
    assert login.login_password.is_visible(), "Password input should be visible"
    assert login.login_button.is_visible(), "Login button should be visible"