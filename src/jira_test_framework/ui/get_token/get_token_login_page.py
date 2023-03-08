from selenium.webdriver.common.by import By

from src.jira_test_framework.ui.get_token.authorize_page import AuthorizePage
from src.jira_test_framework.ui.ui_utils import UIUtils
from src.logger import logger


class GetTokenLoginPage():
    USERNAME = "itzikv3@gmail.com"
    PASSWORD = "itzikpass1212"
    scope = ""
    base_url = "https://auth.atlassian.com/authorize?audience=api.atlassian.com&client_id=EMcZzazmRdqdGmD48zjmCD3tVielmpwN&redirect_uri=https%3A%2F%2Ftask-day.onrender.com%2F&response_type=code&prompt=consent&state=test_itzik"

    CONTINUE_BUTTON_LOCATOR = {"by": By.XPATH, "locator_string": "//span[text()='Continue']"}
    LOGIN_BUTTON_LOCATOR = {"by": By.XPATH, "locator_string": "//span[text()='Log in']"}
    USERNAME_LOCATOR = {"by": By.NAME, "locator_string": "username"}
    PASSWORD_LOCATOR = {"by": By.NAME, "locator_string": "password"}

    def __init__(self, driver):
        self.driver = driver

    def set_base_url(self, scope):
        self.scope = scope
        self.base_url = f"{self.base_url}&scope={self.scope}"

    def login(self, scope="read:jira-work read:account read:me write:jira-work"):
        logger.info("start ui-login process")

        self.set_base_url(scope)
        self.driver.get(self.base_url)

        self.set_username(self.USERNAME)
        continue_button = UIUtils.wait_for_element_visibility(self.driver, self.CONTINUE_BUTTON_LOCATOR)
        continue_button.click()

        login_button = UIUtils.wait_for_element_visibility(self.driver, self.LOGIN_BUTTON_LOCATOR)
        self.set_password(self.PASSWORD)

        login_button.click()
        logger.info("move to authorize page")
        return AuthorizePage(self.driver)

    def set_username(self, username):
        logger.info("setting username: %s", username)
        username_element = UIUtils.wait_for_element_visibility(self.driver, self.USERNAME_LOCATOR)
        username_element.send_keys(username)

    def set_password(self, password):
        logger.info("set password: %s", password)
        password_element = UIUtils.wait_for_element_visibility(self.driver, self.PASSWORD_LOCATOR)
        password_element.send_keys(password)
