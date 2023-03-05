from selenium.webdriver.common.by import By

from src.jira_test_framework.ui.get_token.authorize_page import AuthorizePage
from src.jira_test_framework.ui.ui_utils import UIUtils
from src.logger import logger


class GetTokenLoginPage():
    base_url = ""
    USERNAME = "itzikv3@gmail.com"
    PASSWORD = "itzikpass1212"

    def __init__(self, driver):
        self.driver = driver

    def set_base_url(self, scope):
        self.base_url = f"https://auth.atlassian.com/authorize?audience=api.atlassian.com&client_id=EMcZzazmRdqdGmD48zjmCD3tVielmpwN&scope={scope}&redirect_uri=https%3A%2F%2Ftask-day.onrender.com%2F&response_type=code&prompt=consent&state=test_itzik"

    def login(self, scope="read:jira-work read:account read:me write:jira-work"):
        logger.info("start ui-login process")
        self.set_base_url(scope)
        self.driver.get(self.base_url)

        self.set_username(self.USERNAME)

        continue_button = UIUtils.wait_for_element_visibility(self.driver, By.XPATH, "//span[text()='Continue']")
        continue_button.click()

        login_button = UIUtils.wait_for_element_visibility(self.driver, By.XPATH, "//span[text()='Log in']")
        self.set_password(self.PASSWORD)

        login_button.click()
        logger.info("move to authorize page")
        return AuthorizePage(self.driver)

    def set_username(self, username):
        logger.info("setting username: %s", username)
        username_element = UIUtils.wait_for_element_visibility(self.driver, By.CLASS_NAME, "css-wxvfrp")
        username_element.send_keys(username)

    def set_password(self, password):
        logger.info("set password: %s", password)
        password_element = UIUtils.wait_for_element_visibility(self.driver, By.NAME, "password")
        password_element.send_keys(password)
