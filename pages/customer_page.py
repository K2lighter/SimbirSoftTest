from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CustomerPage(Base):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    drop_down_your_name_locator = '//select[@id="userSelect"]'
    login_button_locator = '//button[@class="btn btn-default"]'
    check_text_locators = '//span[text() = "Harry Potter"]'

    def get_drop_down_your_name(self):
        """
        DROPDOWN: Your Name
        """
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.drop_down_your_name_locator)))

    def get_login_button(self):
        """
        Кнопка: Login
        """
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button_locator)))

    def get_check_text(self):
        """Проверочный текст"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_text_locators)))

    # Actions

    def click_drop_down_your_name(self):
        """
        Нажимаем drop_down your_name
        """
        self.get_drop_down_your_name().click()

    def select_harry_potter(self):
        """
        Выбираем пользователя: Harry Potter
        """
        self.get_drop_down_your_name().send_keys(Keys.DOWN * 2)
        self.get_drop_down_your_name().send_keys(Keys.ENTER)

    def click_login_button(self):
        """
        Нажимаем кнопку Login
        """
        self.get_login_button().click()

    # Methods

    def select_user_page(self):
        """
        Выбираем пользователя
        """
        self.driver.get(self.url)
        self.click_drop_down_your_name()
        self.select_harry_potter()
        self.click_login_button()
        self.check_text(self.get_check_text(), "Harry Potter")
