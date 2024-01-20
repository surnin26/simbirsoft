import time

from pages.locators import MainPageLocators
from pages.main_page import MainPage

link = "https://demoqa.com/automation-practice-form"

first_name = "Surnin"
last_name = "Daniil"
email = "cyrnin@gmail.com"
male = "Male"
mobile = "7988888888"
subjects = "Хочу стать SDET"
file = r"D:\4 Gallery\Desktop\Silicilium\surninAutotests\files\file.png"
address = "Russia, Moscow city, Galicina street, 5/5"


def test_fill_form_registration(browser):
    page = MainPage(browser, link)
    page.open()
    page.fill_field(MainPageLocators.FIRST_NAME, first_name)
    page.fill_field(MainPageLocators.LAST_NAME, last_name)
    page.fill_field(MainPageLocators.EMAIL, email)
    page.click_button(MainPageLocators.INPUT_MALE)
    page.fill_field(MainPageLocators.INPUT_MOBILE, mobile)
    page.click_button(MainPageLocators.DATE_OF_BIRTH)
    [page.click_button(MainPageLocators.MONTH_BACK) for _ in range(3)]
    [page.click_button(MainPageLocators.MONTH_NEXT) for _ in range(5)]
    page.click_button(MainPageLocators.MONTH_ENTER)
    page.click_button(MainPageLocators.MONTH_CHOICE)
    page.click_button(MainPageLocators.YEAR_CHOICE)
    page.click_button(MainPageLocators.DATE_ENTER)
    page.fill_field(MainPageLocators.SUBJECTS, subjects)
    page.click_button(MainPageLocators.HOBBIES)
    page.find(MainPageLocators.UPLOAD_FILE).send_keys(file)
    page.find(MainPageLocators.CURRENT_ADDRESS).send_keys(address)
    page.down()
    # page.click_button(MainPageLocators.STATE)
    # page.click_button(MainPageLocators.ENTER_STATE)
    time.sleep(5)



