from playwright.sync_api import Page, Locator, expect


class CartPage:
    URL = "https://automationexercise.com/view_cart"

    def __init__(self, page: Page):
        self.page = page
        self.cart_items: Locator = page.locator('.cart_description')
        self.quantity_input: Locator = page.locator('input#quantity')
        self.update_button: Locator = page.locator('button[data-qa="cart-update"]')
        self.delete_product: Locator = page.locator('a[data-qa="delete-item"]')
        self.checkout_button: Locator = page.locator('a[href="/checkout"]')
        self.empty_cart_message: Locator = page.locator('p').filter(has_text="Cart is empty")
        self.cart_link: Locator = page.locator('a[href="/view_cart"]')

    def goto(self) -> "CartPage":
        """Navigate to the cart page via home page."""
        self.page.goto("https://automationexercise.com")
        self.cart_link.click()
        return self

    def is_product_in_cart(self, product_name: str) -> bool:
        """Check if a specific product is in the cart."""
        locator = self.page.locator('.cart_description', has_text=product_name)
        try:
            expect(locator).to_be_visible(timeout=3000)
            return True
        except AssertionError:
            return False

    def get_cart_items_count(self) -> int:
        """Get the number of items in cart."""
        return self.cart_items.count()

    def update_quantity(self, quantity: int):
        """Update product quantity."""
        self.quantity_input.fill(str(quantity))
        self.update_button.click()

    def delete_item(self):
        """Delete item from cart."""
        self.delete_product.click()

    def is_empty_cart_message_visible(self) -> bool:
        """Check if empty cart message is visible."""
        try:
            expect(self.empty_cart_message).to_be_visible(timeout=3000)
            return True
        except AssertionError:
            return False

    def click_checkout(self):
        """Proceed to checkout."""
        self.checkout_button.click()

    def has_products(self) -> bool:
        """Check if cart has any products."""
        return self.get_cart_items_count() > 0
