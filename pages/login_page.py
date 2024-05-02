import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    button_customer_login_locator = '//button[@class="btn btn-primary btn-lg"]'
    button_manager_locator = "//button[text()='Bank Manager Login']"
    check_text_locator = '//label[text() = "Your Name :"]'

    def get_customer_login(self):
        """Кнопка: customer_login"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_customer_login_locator)))

    def get_manager(self):
        """Кнопка: manager_login"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_manager_locator)))

    def get_check_text(self):
        """Проверочный текст"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_text_locator)))

    # Actions
    def button_customer_is_displayed(self):
        """Проверка на видимость кнопки - customer"""
        return self.get_customer_login().is_displayed()

    def button_manager_is_displayed(self):
        """Проверка на видимость кнопки - manager"""
        return self.get_customer_login().is_displayed()

    def click_customer_login_button(self):
        """Кликнули кнопку: customer_login"""
        self.get_customer_login().click()
        print("Кликнули кнопку 'customer login'")

    # Methods
    def login_page_actions(self):
        with allure.step("login_page_actions"):
            Logger.add_start_step(method="login_page_actions")
            self.open(self.url)
            self.get_current_url()
            self.button_is_displayed()
            self.click_customer_login_button()
            self.check_text(self.get_check_text(), 'Your Name :')
            Logger.add_end_step(url=self.driver.current_url, method="login_page_actions")
