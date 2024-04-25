from datetime import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    '''current url method'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'current url {get_url}')

    '''assert text method'''

    def check_text(self, actual, expect):
        value_text = actual.text
        assert value_text == expect
        print(f'Actual result is equal to expected result - TEXT: {expect}')


