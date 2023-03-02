from selenium.webdriver.common.by import By

from src.jira_test_framework.ui.get_token.authorize_page import AuthorizePage
from src.jira_test_framework.ui.ui_utils import UIUtils


class GetTokenLoginPage():
    base_url = "https://auth.atlassian.com/authorize?audience=api.atlassian.com&client_id=EMcZzazmRdqdGmD48zjmCD3tVielmpwN" \
               "&scope=read:me&redirect_uri=https%3A%2F%2Ftask-day.onrender.com%2F&response_type=code&prompt=consent&state" \
               "=test_itzik"
    USERNAME = "itzikv3@gmail.com"
    PASSWORD = "itzikpass1212"

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.get(self.base_url)

        username_element = UIUtils.wait_for_element_visibility(self.driver, By.CLASS_NAME, "css-wxvfrp")
        username_element.send_keys(self.USERNAME)

        continue_button = UIUtils.wait_for_element_visibility(self.driver, By.XPATH, "//span[text()='Continue']")
        continue_button.click()

        login_button = UIUtils.wait_for_element_visibility(self.driver, By.XPATH, "//span[text()='Log in']")
        password_element = UIUtils.wait_for_element_visibility(self.driver, By.NAME, "password")

        password_element.send_keys(self.PASSWORD)
        login_button.click()
        return AuthorizePage(self.driver)