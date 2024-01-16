import time

from .pages.locators import MainPageLocators
from .pages.main_page import MainPage

link = "https://demoqa.com/automation-practice-form"

first_name = "Surnin"
last_name = "Daniil"
email = "cyrnin@gmail.com"
male = "Male"
mobile = "7988888888"


def test_fill_form_registration(browser):
    page = MainPage(browser, link)
    page.open()
    page.fill_field(MainPageLocators.FIRST_NAME, "Surnin")
    page.fill_field(MainPageLocators.LAST_NAME, "Daniil")
    page.fill_field(MainPageLocators.EMAIL, "cyrnin@gmail.com")
    page.click_button(MainPageLocators.INPUT_MALE)
    page.fill_field(MainPageLocators.INPUT_MOBILE, "7988888888")
    page.click_button(MainPageLocators.DATE_OF_BIRTH)
    [page.click_button(MainPageLocators.MONTH_BACK) for _ in range(3)]
    [page.click_button(MainPageLocators.MONTH_NEXT) for _ in range(5)]
    page.click_button(MainPageLocators.MONTH_ENTER)
    page.click_button(MainPageLocators.MONTH_CHOICE)
    page.click_button(MainPageLocators.YEAR_CHOICE)
    page.click_button(MainPageLocators.DATE_ENTER)
    time.sleep(5)
