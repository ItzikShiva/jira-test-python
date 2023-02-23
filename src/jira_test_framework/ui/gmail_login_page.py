from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GmailLoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators for the email input field and the "Next" button
    email_field_locator = (By.NAME, "identifier")
    next_button_locator = (By.XPATH, "//span[text()='Next']")

    # Locators for the password input field and the "Login" button
    password_field_locator = (By.NAME, "password")
    login_button_locator = (By.XPATH, "//span[text()='Login']")

    def load(self):
        self.driver.get("https://www.gmail.com")

    def enter_email_address(self, email):
        email_field = self.driver.find_element(*self.email_field_locator)
        email_field.send_keys(email)
        next_button = self.driver.find_element(*self.next_button_locator)
        next_button.click()

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.password_field_locator)
        password_field.send_keys(password)
        login_button = self.driver.find_element(*self.login_button_locator)
        login_button.click()

    def login(self, email, password):
        self.load()
        self.enter_email_address(email)
        self.enter_password(password)
