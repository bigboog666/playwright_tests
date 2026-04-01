import pytest
from playwright.sync_api import Page, BrowserContext


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    page.set_default_timeout(60000)  # 60 second timeout
    yield page
    page.close()

@pytest.fixture(scope="session")
def browser_context(browser):
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        ignore_https_errors=True
    )
    yield context
    context.close()