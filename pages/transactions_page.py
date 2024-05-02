import csv

import allure

from utilities.fibonacci import my_fibo
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class TransactionsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    transaction_balance_credit_locator = (By.XPATH, '//tr[@id="anchor0"]/child::td[2]')
    transaction_type_credit_locator = (By.XPATH, '//tr[@id="anchor0"]/child::td[3]')
    transaction_date_credit_locator = (By.XPATH, '//tr[@id="anchor0"]/child::td[1]')

    transaction_balance_debit_locator = (By.XPATH, '//tr[@id="anchor1"]/child::td[2]')
    transaction_date_debit_locator = (By.XPATH, '//tr[@id="anchor1"]/child::td[1]')
    transaction_type_debit_locator = (By.XPATH, '//tr[@id="anchor1"]/child::td[3]')

    # Getters

    def get_transaction_type_credit(self):
        """Получить тип transaction_credit"""
        return self.find(self.transaction_type_credit_locator)

    def get_transaction_credit_balance(self):
        """Получить баланс transaction_credit"""
        return self.find(self.transaction_balance_credit_locator)

    def get_transaction_credit_date(self):
        """Получить дату transaction_credit"""
        return self.find(self.transaction_date_credit_locator)

    def get_transaction_debit_balance(self):
        """Получить баланс transaction_debit"""
        return self.find(self.transaction_balance_debit_locator)

    def get_transaction_debit_date(self):
        """Получить дату transaction_debit"""
        return self.find(self.transaction_date_debit_locator)

    def get_transaction_type_debit(self):
        """Получить тип transaction_debit"""
        return self.find(self.transaction_type_debit_locator)

    # Actions
    def finish_check(self):
        with allure.step("finish_check"):
            Logger.add_start_step(method="finish_check")
            self.get_current_url()
            date_credit = self.get_transaction_credit_date().text
            date_debit = self.get_transaction_debit_date().text
            balance_credit = self.get_transaction_credit_balance().text
            balance_debit = self.get_transaction_debit_balance().text
            type_operation_credit = self.get_transaction_type_credit().text
            type_operation_debit = self.get_transaction_type_debit().text
            self.check_text(self.get_transaction_credit_balance(), str(my_fibo))
            self.check_text(self.get_transaction_debit_balance(), str(my_fibo))
            self.check_url('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx')
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="finish_check")

        with open("transaction.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow([date_credit, balance_credit, type_operation_credit])
            writer.writerow([date_debit, balance_debit, type_operation_debit])
