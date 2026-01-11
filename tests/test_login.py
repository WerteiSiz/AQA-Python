import allure
import pytest

from pages.login_page import LoginPage


@allure.feature("Login")
def test_successful_login(page, base_url):
    lp = LoginPage(page, base_url)
    lp.open()
    lp.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html", timeout=5000)
    assert "/inventory.html" in page.url
    page.locator("#inventory_container").first.wait_for(state="visible", timeout=5000)
    assert page.locator("#inventory_container").first.is_visible()


@allure.feature("Login")
def test_wrong_password_shows_error(page, base_url):
    lp = LoginPage(page, base_url)
    lp.open()
    lp.login("standard_user", "wrong_password")
    assert lp.is_error_visible(timeout=5000)


@allure.feature("Login")
def test_locked_out_user_shows_error(page, base_url):
    lp = LoginPage(page, base_url)
    lp.open()
    lp.login("locked_out_user", "secret_sauce")
    assert lp.is_error_visible(timeout=5000)


@allure.feature("Login")
def test_empty_fields_shows_error(page, base_url):
    lp = LoginPage(page, base_url)
    lp.open()
    lp.login(None, None)
    assert lp.is_error_visible(timeout=5000)


@allure.feature("Login")
def test_performance_glitch_user(page, base_url):
    lp = LoginPage(page, base_url)
    lp.open()
    lp.login("performance_glitch_user", "secret_sauce")
    # allow longer time for this special user
    page.wait_for_url("**/inventory.html", timeout=15000)
    assert "/inventory.html" in page.url
    page.locator("#inventory_container").first.wait_for(state="visible", timeout=10000)
    assert page.locator("#inventory_container").first.is_visible(timeout=10000)
