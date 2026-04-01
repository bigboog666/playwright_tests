import pytest
from playwright.sync_api import Page, Browser, BrowserContext


@pytest.fixture(scope="session")
def browser_context(browser: Browser) -> BrowserContext:
    """Create a single browser context for all tests."""
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        ignore_https_errors=True
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    """Create a new page in the shared context for each test."""
    page = context.new_page()
    page.set_default_timeout(60000)  # 60 second timeout
    yield page
    page.close()