import pytest
from pages.contact_us_page import ContactUsPage


class TestContactUs:
    """Tests for the Contact Us functionality."""

    def test_contact_form_visible(self, page):
        """Test that contact form is visible on the contact us page."""
        contact = ContactUsPage(page)
        contact.goto()

        assert contact.name_input.is_visible(), "Name input should be visible"
        assert contact.email_input.is_visible(), "Email input should be visible"
        assert contact.message_input.is_visible(), "Message input should be visible"
        assert contact.submit_button.is_visible(), "Submit button should be visible"

    def test_contact_form_empty_fields_validation(self, page):
        """Test that empty fields show validation."""
        contact = ContactUsPage(page)
        contact.goto()

        # Try to submit without filling fields
        contact.submit_button.click()

        # HTML5 validation should prevent submission
        # Check that we're still on the contact page
        assert page.url == "https://automationexercise.com/contact_us"
