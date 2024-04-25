from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
from pages.account_page import AccountPage


def test_smoke_v1(browser):
    """
    Дымовое тестирование
    """
    login = LoginPage(browser)
    login.login_page_actions()

    customer = CustomerPage(browser)
    customer.select_user_page()

    account = AccountPage(browser)
    account.input_deposit_value()

