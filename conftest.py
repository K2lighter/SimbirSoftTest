from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    driver = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()

