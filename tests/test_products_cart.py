import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


class TestProducts:
    """Tests for the Products page functionality."""

    def test_products_page_visible(self, page):
        """Test that products page loads correctly."""
        home = HomePage(page)
        products = ProductsPage(page)

        home.goto()
        page.locator('a[href="/products"]').click()

        assert products.is_products_visible(), "Products should be visible"
        assert products.get_products_count() > 0, "Should have at least one product"

    def test_products_count(self, page):
        """Test that multiple products are displayed."""
        home = HomePage(page)
        products = ProductsPage(page)

        home.goto()
        page.locator('a[href="/products"]').click()

        count = products.get_products_count()
        assert count >= 8, f"Should have at least 8 products, found {count}"

    def test_product_search_visible(self, page):
        """Test that search functionality is visible."""
        home = HomePage(page)

        home.goto()
        page.locator('a[href="/products"]').click()

        search_input = page.locator('input#search_product')
        assert search_input.is_visible(), "Search input should be visible"


class TestProductDetails:
    """Tests for product details view."""

    def test_product_details_view(self, page):
        """Test viewing product details."""
        home = HomePage(page)
        products = ProductsPage(page)

        home.goto()
        page.locator('a[href="/products"]').click()
        products.click_first_product()

        assert products.is_product_details_visible(), "Product details should be visible"

    def test_add_product_to_cart(self, page):
        """Test adding a product to cart."""
        home = HomePage(page)
        products = ProductsPage(page)

        home.goto()
        page.locator('a[href="/products"]').click()
        products.click_first_product()
        products.add_to_cart()

        # Check cart count increased
        cart_text = products.get_cart_count()
        assert "1" in cart_text, f"Cart should have 1 item, got {cart_text}"


class TestCart:
    """Tests for cart functionality."""

    def test_view_cart_page(self, page):
        """Test viewing the cart page."""
        home = HomePage(page)
        products = ProductsPage(page)
        cart = CartPage(page)

        home.goto()
        page.locator('a[href="/products"]').click()
        products.click_first_product()
        products.add_to_cart()
        products.click_view_cart()

        assert cart.has_products(), "Cart should have products"
        assert cart.get_cart_items_count() > 0, "Should have at least one item in cart"

    def test_delete_item_from_cart(self, page):
        """Test deleting an item from cart."""
        home = HomePage(page)
        products = ProductsPage(page)
        cart = CartPage(page)

        # Add product to cart
        home.goto()
        page.locator('a[href="/products"]').click()
        products.click_first_product()
        products.add_to_cart()
        products.click_view_cart()

        # Delete the item
        cart.delete_item()

        # Verify cart is empty
        assert cart.is_empty_cart_message_visible(), "Empty cart message should be visible"
