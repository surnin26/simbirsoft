import allure

from pages.main_page import MainPage

link = "https://demoqa.com/automation-practice-form"


@allure.testcase("Проверка формы регистрации")
@allure.title("Проверка формы регистрации")
def test_fill_form_registration(browser):
    page = MainPage(browser, link)
    page.open()
    page.fill()
    page.submit()
    # page.check()
