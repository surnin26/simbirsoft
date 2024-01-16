class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def search_element(self):
        pass

    def click_button(self, locator):
        element = self.browser.find_element(*locator)
        element.click()
