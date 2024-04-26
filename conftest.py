from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()


