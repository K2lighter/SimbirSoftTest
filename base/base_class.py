from datetime import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        print(f"текущая url - {url}")

    def get_current_url(self):
        """current url method"""
        get_url = self.driver.current_url
        print(f'current url {get_url}')

    def check_text(self, actual, expect):
        """assert text method"""
        value_text = actual.text
        assert value_text == expect
        print(f'Actual result is equal to expected - the text matches: {expect}')

    def get_screenshot(self):
        """screenshot method"""
        # now_date = datetime.now().strftime("%Y.%m.%d %H.%M.%S")
        now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('/home/k2lighter/PycharmProjects/SimbirSoft_Test_Task/screen/' + name_screenshot)

    def check_url(self, result):
        """check url method"""
        get_url = self.driver.current_url
        assert get_url == result, "URL doesn't match"
        print('Actual result is equal to expected : URL matches')
