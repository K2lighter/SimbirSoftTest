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
        print(f'Actual result is equal to expected - the text matches: {expect}')

    '''screenshot method'''

    def get_screenshot(self):
        # now_date = datetime.now().strftime("%Y.%m.%d %H.%M.%S")
        now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('/home/k2lighter/PycharmProjects/SimbirSoft_Test_Task/screen/' + name_screenshot)

    '''check url method'''

    def check_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result, "URL doesn't match"
        print('Actual result is equal to expected : URL matches' )
