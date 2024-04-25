from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class LoginPage(Base):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    button_customer_login_locator = '//button[@class="btn btn-primary btn-lg"]'
    check_text_locator = '//label[text() = "Your Name :"]'

    def get_customer_login(self):
        """
        Кнопка: customer_login
        """
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_customer_login_locator)))

    def get_check_text(self):
        """
        Проверочный текст
        """
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_text_locator)))

    # Actions

    def click_customer_login_button(self):
        """
        Нажатие на кнопку: customer_login
        """
        self.get_customer_login().click()
        print("Нажали кнопку 'customer login'")

    # Methods
    def login_page_actions(self):
        self.driver.get(self.url)
        self.get_current_url()
        self.click_customer_login_button()
        self.check_text(self.get_check_text(), 'Your Name :')
