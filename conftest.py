from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest

from utilities import ReadConfigurations


# @pytest.fixture()
# def browser():
#     options = Options()
#     options.add_argument("--no-sandbox")
#     options.add_argument("--headless")
#     driver = webdriver.Chrome(options=options)
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.close()

@pytest.fixture()
def setup(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    global driver
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")
    driver.maximize_window()
    app_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
