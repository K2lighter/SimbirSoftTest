import pytest

from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
from pages.account_page import AccountPage
from pages.transactions_page import TransactionsPage
import allure

"""
1.чтобы запустить сервер
скачать и запустить
java -jar selenium-server-4.20.0.jar standalone
2. для запуска теста pytest -s -v 

3. для получения allure отчета:
pytest -s -v --alluredir allure-results
allure serve allure-results

"""


@allure.description("test_smoke_v1")
@pytest.mark.smoke
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

# allure serve allure-results
