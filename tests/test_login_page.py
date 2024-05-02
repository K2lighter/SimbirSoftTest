import pytest
from pages.login_page import LoginPage


@pytest.mark.login_page
def test_button_customer_is_displayed(browser):
    lp = LoginPage(browser)
    lp.open(lp.url)
    assert lp.button_customer_is_displayed()
    print("Кнопка customer отображается")


@pytest.mark.login_page
def test_button_manager_is_displayed(browser):
    lp = LoginPage(browser)
    lp.open(lp.url)
    assert lp.button_manager_is_displayed()
    print("Кнопка manager отображается")
