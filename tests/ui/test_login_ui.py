import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.jira_test_framework.ui.ui_service import UiService
from tests.ui.ui_utils import setup_driver_options

# I'll take it out to constant file if it will be necessary
USERNAME = "itzikv3@gmail.com"
PASSWORD = "itzikpass"


# @pytest.fixture it's like before test
@pytest.fixture
def setup():
    driver = setup_driver_options()
    ui_service = UiService(driver)
    yield ui_service, driver
    driver.close()


def test_valid_login_ui(setup):
    ui_service = setup[0]
    driver = setup[1]
    ui_service.login(USERNAME, PASSWORD)

    your_work_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "css-kwc091")))
    assert your_work_element.text == "Your work"

# def test_invalid_username_login_ui():
# def test_invalid_password_login_ui():
