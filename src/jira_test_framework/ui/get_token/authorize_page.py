import time

from selenium.webdriver.common.by import By

from src.jira_test_framework.ui.ui_utils import UIUtils
from src.logger import logger


class AuthorizePage:
    def __init__(self, driver):
        self.driver = driver

    def authorize_access(self):
        logger.info("start authorizing process")
        choose_elements = UIUtils.wait_for_element_visibility(self.driver, By.XPATH, "//*[text()='Choose a site']")
        choose_elements.click()

        automat_value_element = UIUtils.wait_for_element_visibility(self.driver, By.XPATH,
                                                                    "//*[text()='automat-ct.atlassian.net']")
        automat_value_element.click()

        time.sleep(2)
        accept_button = UIUtils.wait_for_element_visibility(self.driver, By.XPATH, "//*[text()='Accept']")
        accept_button.click()
