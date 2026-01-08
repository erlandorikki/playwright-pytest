import pytest
import re
from playwright.sync_api import Page, expect

@pytest.mark.login
@pytest.mark.parametrize(
    "username,password,should_succeed",
    [
        ("standard_user", "secret_sauce", True),          # Valid
        ("invalid_user", "secret_sauce", False),          # Invalid username
        ("standard_user", "wrong_password", False),       # Invalid password
        ("", "", False),                                  # username & password Kosong
    ]
)
def test_login(page: Page, username, password, should_succeed):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

    if should_succeed:
        expect(page).to_have_url(re.compile(r".*inventory\.html"))
        expect(page.locator(".inventory_list")).to_be_visible()
    else:
        expect(page.locator('[data-test="error"]')).to_be_visible()
