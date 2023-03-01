import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.jira_test_framework.ui.login_page import LoginPage
from src.logger import logger
from tests.ui.constants import INVALID_USERNAME, INVALID_PASSWORD, USERNAME

from tests.ui.driver_factory import get_chrome_driver
from tests.ui.ui_utils import login

your_work_class_name_locator = "css-kwc091"
continue_xpath_locator = "//span[text()='Continue']"
help_logging_in_xpath_locator = "//a[text()='logging in']"


@pytest.fixture
def driver():
    driver = get_chrome_driver()
    yield driver
    driver.close()


def test_valid_ui_login(driver):
    login(driver)
    your_work_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, your_work_class_name_locator)))
    assert your_work_element.text == "Your work"
    logger.info("login with ui successfully")


def test_invalid_username_ui_login(driver):
    login_page = LoginPage(driver)
    login_page.set_username(INVALID_USERNAME)

    continue_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, continue_xpath_locator)))

    assert continue_element.text == "Continue"
    logger.info("username: " + INVALID_USERNAME + " incorrect")


def test_invalid_password_login_ui(driver):
    login_page = LoginPage(driver)
    login_page.login(USERNAME, INVALID_PASSWORD)

    help_logging_in_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, help_logging_in_xpath_locator)))

    assert help_logging_in_element.text == "logging in"
    logger.info("password: " + INVALID_PASSWORD + " incorrect")

    # try to put filename in global log
    # logger.info(os.path.basename(__file__) + " password: " + INVALID_PASSWORD + " incorrect")
