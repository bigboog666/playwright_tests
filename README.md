# Playwright Tests

Автоматизированные end-to-end тесты для сайта [Automation Exercise](https://automationexercise.com) с использованием Playwright и pytest.

## Возможности

- **Page Object Model** — чистая и поддерживаемая архитектура тестов
- **Тестирование пользовательского цикла** — регистрация, вход, выход, удаление аккаунта
- **Тесты товаров и корзины** — проверка функциональности корзины
- **Тесты контактной формы** — валидация формы обратной связи

## Структура проекта

```
playwright_tests/
├── pages/              # Page Object классы
│   ├── home_page.py
│   ├── login_page.py
│   ├── register_page.py
│   ├── account_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── contact_us_page.py
├── tests/              # Тестовые файлы
│   ├── test_user_lifecycle.py
│   ├── test_login.py
│   ├── test_register.py
│   ├── test_products_cart.py
│   └── test_contact_us.py
├── conftest.py         # Фикстуры pytest
├── pytest.ini          # Конфигурация pytest
└── README.md
```

## Требования

- Python 3.11+
- Playwright
- pytest

## Установка

```bash
# Установка зависимостей
pip install playwright pytest
playwright install
```

## Запуск тестов

```bash
# Запустить все тесты
pytest

# Запустить конкретный файл с тестами
pytest tests/test_login.py

# Запустить с подробным выводом
pytest -v

# Запустить в режиме с отображением браузера
pytest --headed

# Запустить в замедленном режиме (для отладки)
pytest --slowmo=1000
```

## Конфигурация

По умолчанию тесты используют размер окна браузера 1280x720 (настроено в `conftest.py`).
