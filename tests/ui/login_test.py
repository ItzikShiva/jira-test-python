import pytest
from selenium.webdriver.common.by import By

from src.jira_test_framework.ui.login_page import LoginPage
from src.jira_test_framework.ui.ui_utils import UIUtils
from src.logger import logger
from tests.ui.constants import INVALID_USERNAME, INVALID_PASSWORD, USERNAME

from src.jira_test_framework.ui.driver_factory import get_chrome_driver
from tests.ui.ui_utils import ui_login

YOUR_WORK_LOCATOR = {"by": By.XPATH, "locator_string": "//h1[text()='Your work']"}
CONTINUE_LOCATOR = {"by": By.XPATH, "locator_string": "//span[text()='Continue']"}
HELP_LOGGING_IN_LOCATOR = {"by": By.XPATH, "locator_string": "//a[text()='logging in']"}


@pytest.fixture
def driver():
    driver = get_chrome_driver()
    yield driver
    driver.close()


def test_valid_ui_login(driver):
    ui_login(driver)
    your_work_element = UIUtils.wait_for_element_visibility(driver, YOUR_WORK_LOCATOR)
    assert your_work_element.text == "Your work"
    logger.info("login with ui successfully")


def test_invalid_username_ui_login(driver):
    login_page = LoginPage(driver)
    login_page.set_username(INVALID_USERNAME)

    continue_element = UIUtils.wait_for_element_visibility(driver, CONTINUE_LOCATOR)
    assert continue_element.text == "Continue"
    logger.info("username: " + INVALID_USERNAME + " incorrect")


def test_invalid_password_login_ui(driver):
    login_page = LoginPage(driver)
    login_page.login(USERNAME, INVALID_PASSWORD)

    help_logging_in_element = UIUtils.wait_for_element_visibility(driver, HELP_LOGGING_IN_LOCATOR)
    assert help_logging_in_element.text == "logging in"
    logger.info("password: " + INVALID_PASSWORD + " incorrect")

    # try to put filename in global log
    # logger.info(os.path.basename(__file__) + " password: " + INVALID_PASSWORD + " incorrect")
