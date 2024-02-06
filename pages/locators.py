from selenium.webdriver.common.by import By


class MainPageLocators:
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.CSS_SELECTOR, "input[id=\"lastName\"]")
    EMAIL = (By.XPATH, "//*[@id=\"userEmail\"]")
    INPUT_MALE = (By.XPATH, "//*[text()=\"Male\"]")
    INPUT_MOBILE = (By.ID, "userNumber")
    DATE_OF_BIRTH = (By.XPATH, "//*[@id=\"dateOfBirth-wrapper\"]")
    MONTH_BACK = (By.CSS_SELECTOR, "button[aria-label=\"Previous Month\"]")
    MONTH_NEXT = (By.CSS_SELECTOR, "button[aria-label=\"Next Month\"]")
    MONTH_ENTER = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    MONTH_CHOICE = (By.CSS_SELECTOR, ".react-datepicker__month-select  option[value=\"3\"]")
    YEAR_ENTER = (By.CSS_SELECTOR, "react-datepicker__year-select")
    YEAR_CHOICE = (By.CSS_SELECTOR, ".react-datepicker__year-select  option[value=\"1998\"]")
    DATE_ENTER = (By.CSS_SELECTOR, "div[class=\"react-datepicker__day react-datepicker__day--022\"]")
    SUBJECTS = (By.XPATH, "//*[@id=\"subjectsInput\"]")
    HOBBIES = (By.XPATH, "//*[@id=\"hobbiesWrapper\"]/div[2]/div[1]/label")
    UPLOAD_FILE = By.XPATH, "//*[@id=\"uploadPicture\"]"
    CURRENT_ADDRESS = By.ID, "currentAddress"
    STATE = By.XPATH, "//*[@id=\"state\"]/div/div[1]"
    ENTER_STATE = By.XPATH, "//*[@id=\"react-select-3-option-0\"]"
    CITY = By.XPATH, "//*[@id=\"city\"]/div/div[1]"
    ENTER_CITY = By.XPATH, "//*[@id=\"react-select-4-option-1\"]"
    BODY = By.CSS_SELECTOR, "body"
    # SUBMIT = By.CSS_SELECTOR, "button[id=\"submit\"]"
    SUBMIT = By.XPATH, ""


