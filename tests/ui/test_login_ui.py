import logging

import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.jira_test_framework.ui.login_page import LoginPage
from tests.ui.ui_utils import setup_driver_options

# I'll take it out to constant file if it will be necessary
USERNAME = "itzikv3@gmail.com"
PASSWORD = "itzikpass"


# logger = get_logger()

# Set up the logger
# logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
# handler = logging.StreamHandler()
# handler.setFormatter(formatter)
# logger.addHandler(handler)


# @pytest.fixture it's like before test
@pytest.fixture
def driver():
    driver = setup_driver_options()
    yield driver
    driver.close()


def test_valid_login_ui(driver):
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)

    your_work_css_locator = "css-kwc091"
    your_work_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, your_work_css_locator)))
    assert your_work_element.text == "Your work"


def test_invalid_username_login_ui(driver):
    login_page = LoginPage(driver)
    login_page.set_username("INVALID_USERNAME")

    continue_xpath_locator = "//span[text()='Continue']"
    continue_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, continue_xpath_locator)))

    assert continue_element.text == "Continue"
    # logger.info("logged in successfully")
    # logger.info("logged in successfully")
    # logger.info("logged in successfully")
    # logger.info("logged in successfully")

# def test_invalid_password_login_ui():
