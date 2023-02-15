

class Base():

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url: " + get_url)

    def assert_word(self, text_on_page, expected_result):
        # print(text_on_page.text)
        assert text_on_page.text == expected_result
        print("Assert is OK")

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result, print("URL is INCORRECT")
        print("URL check is OK")

    """Screenshots method"""
    def get_screenshot(self):
        import datetime
        now_date = datetime.datetime.utcnow().strftime("%d.%m.%Y - %H:%M")
        screenshot_name = "screenshot " + now_date + ".png"
        self.driver.save_screenshot("/Users/zordex/PycharmProjects/test_automation/screens/" + screenshot_name)