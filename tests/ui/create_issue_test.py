import time
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

from src.jira_test_framework.ui.dashboard_page.dashboard_page import DashboardPage
from src.logger import logger
from tests.ui.constants import PROJECT_NAME, EMPTY_ISSUE_TEXT
from src.jira_test_framework.ui.driver_factory import get_chrome_driver
from tests.ui.ui_utils import ui_login


@pytest.fixture
def get_get_dashboard_and_driver():
    driver = get_chrome_driver()
    ui_login(driver)
    dashboard_page = DashboardPage(driver)
    dashboard_page.go_to_project(PROJECT_NAME)
    dashboard_page.go_to_backlog()
    yield driver, dashboard_page
    driver.close()


def test_create_issue(get_dashboard_and_driver):
    driver, dashboard_page = get_dashboard_and_driver

    timestamp_str = str(datetime.now().timestamp())
    issue_text = "ISSUE from ui test " + timestamp_str

    dashboard_page.create_issue(issue_text)
    assert dashboard_page.is_issue_exist(issue_text) == True
    logger.info("issue: " + issue_text + " was created")

    # two options:
    # dashboard_page.delete_issue(timestamp_str)
    dashboard_page.delete_issue_v1(timestamp_str)
    assert dashboard_page.is_issue_exist(issue_text) == False
    logger.info("issue: " + issue_text + " was deleted")
    time.sleep(2)


def test_create_empty_issue(get_dashboard_and_driver):
    driver, dashboard_page = get_dashboard_and_driver

    dashboard_page.create_issue(EMPTY_ISSUE_TEXT)

    new_issue_element = driver.find_element(By.XPATH, "//textarea[@placeholder='What needs to be done?']")
    assert int(new_issue_element.size['width']) > 0

    logger.info("empty issue wasn't created")
    time.sleep(2)
