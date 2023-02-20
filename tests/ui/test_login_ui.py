from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.jira_test_framework.ui.ui_service import UiService
from tests.ui.ui_utils import setup_driver_options

driver = setup_driver_options()
ui_service = UiService(driver)

# I'll take it out to constant file if it will be necessary
USERNAME = "itzikv3@gmail.com"
PASSWORD = "itzikpass"


def test_login_ui():
    ui_service.login(USERNAME, PASSWORD)

    your_work_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "css-kwc091")))
    assert your_work_element.text == "Your work"
