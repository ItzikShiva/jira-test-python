import time

from selenium.webdriver.common.by import By

from src.jira_test_framework.ui.ui_utils import UIUtils
from src.logger import logger


class AuthorizePage:
    choose_elements_locator = {"by": By.XPATH, "locator_string": "//*[text()='Choose a site']"}
    automat_value_locator = {"by": By.XPATH, "locator_string": "//*[text()='automat-ct.atlassian.net']"}
    accept_button_locator = {"by": By.XPATH, "locator_string": "//*[text()='Accept']"}

    def __init__(self, driver):
        self.driver = driver

    def authorize_access(self):
        logger.info("start authorizing process")
        choose_elements = UIUtils.wait_for_element_visibility(self.driver, self.choose_elements_locator)
        choose_elements.click()

        automat_value_element = UIUtils.wait_for_element_visibility(self.driver, self.automat_value_locator)
        automat_value_element.click()

        time.sleep(2)
        accept_button = UIUtils.wait_for_element_visibility(self.driver, self.accept_button_locator )
        accept_button.click()
