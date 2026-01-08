import pytest
from playwright.sync_api import Page, expect

@pytest.mark.logout
def test_successful_logout(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Logout
    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")

    # Verify back to login
    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator("#login-button")).to_be_visible()

@pytest.mark.logout
def test_access_inventory_after_logout(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Logout
    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")

    # Try access inventory page manually
    page.goto("https://www.saucedemo.com/inventory.html")

    # Should redirect to login
    expect(page.locator("#login-button")).to_be_visible()
