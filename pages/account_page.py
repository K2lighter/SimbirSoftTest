import allure

from utilities.fibonacci import my_fibo
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
from time import sleep

class AccountPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    deposit_button_locator = '//button[@ng-click="deposit()"]'
    amount_placeholder_locator = '//input[@placeholder="amount"]'
    deposit_submit_locator = '//button[@type="submit"]'
    check_text_locator = '//span[@class="error ng-binding"]'
    check_balance_locator = '//strong[@class="ng-binding"][2]'

    withdrawal_button_locator = '//button[@ng-click="withdrawl()"]'
    amount_withdrawal_locator = '//input[@placeholder="amount"]'
    withdrawal_submit_locator = '//button[text()="Withdraw"]'

    transaction_locator = '//button[@ng-class="btnClass1"]'
    check_amount_locator = '//*[text()="Amount"]'

    text_to_be_present_in_element_d = "Amount to be Deposited :"
    text_to_be_present_in_element_w = "Amount to be Withdrawn :"
    text_to_be_present_in_element_tran = "Transaction successful"

    # Getters

    def get_deposit_button(self):
        """ Кнопка: deposit_button"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.deposit_button_locator)))

    def get_amount_deposit(self):
        """Кнопка: amount_placeholder"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.amount_placeholder_locator)))

    def get_deposit_submit(self):
        """Кнопка подтверждения deposit_submit"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.deposit_submit_locator)))

    def get_check_text(self):
        """Проверочный текст"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_text_locator)))

    def get_balance(self):
        """Баланс"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_balance_locator)))

    def get_withdrawal_button(self):
        """Кнопка withdrawl_button"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.withdrawal_button_locator)))

    def get_amount_withdrawal(self):
        """Поле amount_withdrawal"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.amount_withdrawal_locator)))

    def get_withdrawal_submit(self):
        """Кнопка подтверждения withdrawal_submit"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.withdrawal_submit_locator)))

    def get_transaction_button(self):
        """Кнопка transaction"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.transaction_locator)))

    def get_check_amount(self):
        """Текст успешной операции"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_amount_locator)))

    def get_check_text_to_be_present_in_element(self, text):
        """Ожидание, пока не появится поверочный текст на странице"""
        return WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), text))

    # Actions

    def click_deposit_button(self):
        """Нажатие кнопки deposit_button"""
        self.get_deposit_button().click()
        print("Кликнули кнопку 'deposit'")

    def input_fibo_deposit(self, fibo):
        """Вносим в поле amount_deposit вычисленное значение fibonacci"""
        self.get_amount_deposit().send_keys(fibo)
        print("Вносим значение fibonacci в поле deposit")

    def click_deposit_submit(self):
        """Нажатие кнопки deposit_submit"""
        self.get_deposit_submit().click()
        print("Кликнули кнопку подтверждения 'deposit'")

    def click_withdrawal_button(self):
        """Нажатие кнопки withdrawal_button"""
        self.get_withdrawal_button().click()
        print("Кликнули кнопку 'withdrawal'")
    def input_fibo_withdrawal(self, fibo):
        """Вносим в поле amount_withdrawal вычисленное значение fibonacci"""
        self.get_amount_withdrawal().send_keys(fibo)
        print("Вносим значение fibonacci в поле withdrawal")

    def click_withdrawal_submit(self):
        """Нажатие кнопки withdrawal_submit"""
        self.get_withdrawal_submit().click()
        print("Кликнули кнопку подтверждения 'withdrawal'")

    def click_transaction_button(self):
        """Нажатие кнопки transaction_button"""
        self.get_transaction_button().click()
        print("Кликнули кнопку 'transaction'")

    # Methods

    def input_deposit_value(self):
        """
        Пополнение счета (Deposit) на сумму равную вычисленному в п.4 числу
        """
        with allure.step("input_deposit_value"):
            # Logger.add_start_step(method="input_deposit_value")
            self.get_current_url()
            self.click_deposit_button()
            self.get_check_text_to_be_present_in_element(self.text_to_be_present_in_element_d)
            self.input_fibo_deposit(my_fibo)
            self.click_deposit_submit()
            self.check_text(self.get_check_text(), 'Deposit Successful')
            self.check_text(self.get_balance(), str(my_fibo))
            # Logger.add_end_step(url=self.driver.current_url, method="input_deposit_value")

    def input_withdrawal_value(self):
        """
        Списание со счета (Withdrawal) на сумму равную вычисленному в п.4 числу;
        """
        with allure.step("Input_withdrawal_value"):
            # Logger.add_start_step(method="input_withdrawal_value")
            self.click_withdrawal_button()
            self.get_check_text_to_be_present_in_element(self.text_to_be_present_in_element_w)
            self.input_fibo_withdrawal(my_fibo)
            self.click_withdrawal_submit()
            self.check_text(self.get_check_text(), 'Transaction successful')
            self.check_text(self.get_balance(), str(int(my_fibo) - int(my_fibo)))
            # Logger.add_end_step(url=self.driver.current_url, method="input_withdrawal_value")
    def transaction_button(self):
        """Нажатие кнопки transaction_button"""
        with allure.step("End transaction"):
<<<<<<< HEAD
            # Logger.add_start_step(method="transaction_button")
=======
            Logger.add_start_step(method="transaction_button")
>>>>>>> refs/remotes/origin/main
            sleep(1)
            self.get_check_text_to_be_present_in_element(self.text_to_be_present_in_element_tran)
            self.click_transaction_button()
            self.check_text(self.get_check_amount(), 'Amount')
<<<<<<< HEAD
            # Logger.add_end_step(url=self.driver.current_url, method="transaction_button")
=======
            Logger.add_end_step(url=self.driver.current_url, method="transaction_button")
>>>>>>> refs/remotes/origin/main
