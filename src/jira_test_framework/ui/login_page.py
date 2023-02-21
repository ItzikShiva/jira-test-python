from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage():
    base_url = "https://automat-ct.atlassian.net/jira/your-work"
    username_name_locator = "username"
    password_name_locator = "password"

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.base_url)

    def login(self, username, password):
        self.set_details(username, password)
        # return self.driver

    def set_details(self, username, password):
        self.set_username(username)
        self.set_password(password)

    def set_username(self, username):
        username_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.username_name_locator)))
        username_element.send_keys(username)
        username_element.send_keys(Keys.RETURN)

    # this method can execute only after set_username()
    def set_password(self, password):
        password_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.password_name_locator)))
        password_element.send_keys(password)
        password_element.send_keys(Keys.RETURN)
