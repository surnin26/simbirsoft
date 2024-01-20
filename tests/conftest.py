import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())


@pytest.fixture(scope='function')
def browser():
    chrome_options = Options()
    # chrome_options.add_argument("window-size=1920,1080")
    browser = webdriver.Chrome(options=chrome_options, service=service)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()
