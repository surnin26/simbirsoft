import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import MainPageLocators

first_name = "Surnin"
last_name = "Daniil"
email = "cyrnin@gmail.com"
male = "Male"
mobile = "7988888888"
subjects = "SDET"
file = r"D:\4 Gallery\Desktop\Silicilium\surninAutotests\files\file.png"
address = "Russia, Moscow city, Galicina street, 5/5"


class MainPage(BasePage):

    def fill_field(self, locator, text):
        field = self.browser.find_element(*locator)
        field.click()
        field.send_keys(text)

    @allure.step("Заполнение полей ввода")
    def fill(self):
        self.fill_field(MainPageLocators.FIRST_NAME, first_name)
        self.fill_field(MainPageLocators.LAST_NAME, last_name)
        self.fill_field(MainPageLocators.EMAIL, email)
        self.click_button(MainPageLocators.INPUT_MALE)
        self.fill_field(MainPageLocators.INPUT_MOBILE, mobile)
        self.click_button(MainPageLocators.DATE_OF_BIRTH)
        [self.click_button(MainPageLocators.MONTH_BACK) for _ in range(9)]
        [self.click_button(MainPageLocators.MONTH_NEXT) for _ in range(5)]
        self.click_button(MainPageLocators.MONTH_ENTER)
        self.click_button(MainPageLocators.MONTH_CHOICE)
        self.click_button(MainPageLocators.YEAR_CHOICE)
        self.click_button(MainPageLocators.DATE_ENTER)
        self.fill_field(MainPageLocators.SUBJECTS, subjects)
        self.click_button(MainPageLocators.HOBBIES)
        self.find(MainPageLocators.UPLOAD_FILE).send_keys(file)
        self.find(MainPageLocators.CURRENT_ADDRESS).send_keys(address)
        self.down()
        self.click_for_xpath(MainPageLocators.STATE)
        self.click_for_xpath(MainPageLocators.ENTER_STATE)
        self.click_for_xpath(MainPageLocators.CITY)
        self.click_for_xpath(MainPageLocators.ENTER_CITY)

    @allure.step("Клик по Submit")
    def submit(self):
        self.browser.execute_script("document.body.style.zoom='70%'")
        submit_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )
        try:
            element = self.browser.find_element(By.ID, "submit")
            element.click()
            submit_button.click()
        except Exception:
            self.browser.execute_script("arguments[0.click();", submit_button)
        time.sleep(8)
