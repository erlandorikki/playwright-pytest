import pytest
import re
from playwright.sync_api import Page, expect

@pytest.mark.checkout
@pytest.mark.parametrize(
    "first_name,last_name,postal_code,should_succeed",
    [
        ("Rikki", "Erlando", "12345", True),       # Positive: Valid
        ("", "Erlando", "12345", False),          # Negative: first name kosong
        ("Rikki", "", "12345", False),         # Negative: last name kosong
        ("Rikki", "Erlando", "", False),            # Negative: postal code kosong
        ("", "", "", False),                   # Negative: semua field kosong
    ]
)
def test_checkout_flow(page: Page, first_name, last_name, postal_code, should_succeed):
    # Login
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url(re.compile(r".*inventory\.html"))

    # Tambah produk pertama ke cart
    page.locator("button[id^='add-to-cart']").first.click()
    page.locator(".shopping_cart_link").click()
    expect(page).to_have_url(re.compile(r".*cart\.html"))

    # Lanjutkan ke checkout step 1
    page.locator("#checkout").click()
    expect(page).to_have_url(re.compile(r".*checkout-step-one\.html"))

    # Isi form checkout
    page.locator("#first-name").fill(first_name)
    page.locator("#last-name").fill(last_name)
    page.locator("#postal-code").fill(postal_code)
    page.locator("#continue").click()

    if should_succeed:
        # Berhasil lanjut ke step 2
        expect(page).to_have_url(re.compile(r".*checkout-step-two\.html"))
        expect(page.locator(".summary_info")).to_be_visible()
    else:
        # Muncul error di halaman checkout step 1
        expect(page.locator(".error-message-container")).to_be_visible()
