from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
from pages.account_page import AccountPage
from pages.transactions_page import TransactionsPage
import allure


@allure.description("test_smoke_v1")
def test_smoke_v1(browser):
    """
    Дымовое тестирование
    """
    login = LoginPage(browser)
    login.login_page_actions()

    customer = CustomerPage(browser)
    customer.select_user()

    account = AccountPage(browser)
    account.input_deposit_value()
    account.input_withdrawal_value()
    account.transaction_button()

    tran = TransactionsPage(browser)
    tran.finish_check()

# allure serve test_results/tests/test_smoke.py
