import time
import allure
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    @allure.step("Открытие страницы")
    def open(self):
        self.browser.execute_script("document.body.style.zoom='70%'")
        self.browser.get(self.url)

    def click_button(self, locator):
        element = self.browser.find_element(*locator)
        element.click()

    def down(self):
        element = self.browser.find_element(By.CSS_SELECTOR, "body")
        element.send_keys(Keys.PAGE_DOWN)

    def find(self, locator):
        element = WebDriverWait(self.browser, 30).until(ec.visibility_of_element_located(locator))
        return element

    def click_for_xpath(self, xpath):
        element = WebDriverWait(self.browser, 5).until(ec.visibility_of_element_located(xpath))
        time.sleep(0.1)
        actions = ActionChains(self.browser)
        time.sleep(0.1)
        actions.move_to_element(element).click().perform()
        time.sleep(0.1)

