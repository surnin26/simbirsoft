from .base_page import BasePage


class MainPage(BasePage):

    def fill_field(self, locator, text):
        field = self.browser.find_element(*locator)
        field.click()
        field.send_keys(text)
