from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class AccountPage(Base):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    deposit_button_locator = '//button[@ng-click="deposit()"]'
    amount_placeholder_locator = '//input[@placeholder="amount"]'
    deposit_submit_locator = '//button[@type="submit"]'

    def get_deposit_button(self):
        """
        Кнопка: deposit_button
        """
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.deposit_button_locator)))

    def get_amount_placeholder(self):
        """
        Кнопка: amount_placeholder
        """
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.amount_placeholder_locator)))

    def get_deposit_submit(self):
        """
        Кнопка: deposit_submit
        """
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.deposit_submit_locator)))

    # Actions

    def click_deposit_button(self):
        """
        Нажимаем deposit_button
        """
        self.get_deposit_button().click()

    def input_fibo_value(self, fibo):
        """
        Вставляем в поле amount вычисленное значение fibonacci
        """
        self.get_amount_placeholder().send_keys(fibo)

    def click_deposit_submit(self):
        """
        Нажимаем кнопку deposit_submit
        """
        self.get_deposit_submit().click()

    # Methods

    def input_deposit_value(self):
        """
        Вносим депозит
        """
        self.driver.get(self.url)
        sleep(1)
        self.click_deposit_button()
        sleep(1)
        # self.input_fibo_value(my_fibo)
        # # self.click_deposit_submit()
