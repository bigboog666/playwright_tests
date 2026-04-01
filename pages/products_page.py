from playwright.sync_api import Page, Locator, expect


class ProductsPage:
    URL = "https://automationexercise.com/products"

    def __init__(self, page: Page):
        self.page = page
        self.products_list: Locator = page.locator('.product-image')
        self.first_product: Locator = page.locator('.product-image').first
        self.product_details: Locator = page.locator('#productDetails')
        self.quantity_input: Locator = page.locator('input#quantity')
        self.add_to_cart_button: Locator = page.locator('button[data-qa="addToCart"]')
        self.cart_count: Locator = page.locator('.header-right b')
        self.view_cart_button: Locator = page.locator('a[href="/view_cart"]')
        self.product_title: Locator = page.locator('h2').first
        self.products_link: Locator = page.locator('a[href="/products"]')
        self.product_card: Locator = page.locator('.single-products')

    def goto(self) -> "ProductsPage":
        """Navigate to the products page via home page."""
        self.page.goto("https://automationexercise.com")
        self.products_link.click()
        return self

    def is_products_visible(self) -> bool:
        """Check if products are visible."""
        try:
            expect(self.product_card.first).to_be_visible(timeout=5000)
            return True
        except AssertionError:
            return False

    def get_products_count(self) -> int:
        """Get the number of products displayed."""
        return self.product_card.count()

    def click_first_product(self):
        """Click on the first product to view details."""
        self.first_product.click()

    def set_quantity(self, quantity: int):
        """Set product quantity."""
        self.quantity_input.fill(str(quantity))

    def add_to_cart(self):
        """Add product to cart."""
        self.add_to_cart_button.click()

    def get_cart_count(self) -> str:
        """Get the cart count text."""
        return self.cart_count.inner_text()

    def click_view_cart(self):
        """Navigate to cart page."""
        self.view_cart_button.click()

    def is_product_details_visible(self) -> bool:
        """Check if product details are visible."""
        try:
            expect(self.product_details).to_be_visible(timeout=3000)
            return True
        except AssertionError:
            return False
