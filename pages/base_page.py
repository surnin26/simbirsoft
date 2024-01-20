from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


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

    def down(self):
        element = self.browser.find_element(By.CSS_SELECTOR, "body")
        element.send_keys(Keys.PAGE_DOWN)

