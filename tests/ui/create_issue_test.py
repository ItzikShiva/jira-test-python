import time
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

from src.jira_test_framework.ui.dashboard_page.dashboard_page import DashboardPage
from src.logger import logger
from tests.ui.constants import PROJECT_NAME, EMPTY_ISSUE_TEXT
from tests.ui.driver_factory import get_chrome_driver
from tests.ui.ui_utils import login


@pytest.fixture
def dashboard_page(driver):
    """
    HOD - this method can be also regular method (not fixture), and call it regular from the tests. (like: dashboard_page = get_dashboard_page(driver) )
    """
    login(driver)
    dashboard_page = DashboardPage(driver)
    dashboard_page.go_to_project(PROJECT_NAME)
    dashboard_page.go_to_backlog()
    return dashboard_page


@pytest.fixture
def driver():
    driver = get_chrome_driver()
    yield driver
    driver.close()


def test_create_issue(driver, dashboard_page):
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


def test_create_empty_issue(driver, dashboard_page):
    dashboard_page.create_issue(EMPTY_ISSUE_TEXT)

    new_issue_element = driver.find_element(By.XPATH, "//textarea[@placeholder='What needs to be done?']")
    assert int(new_issue_element.size['width']) > 0

    logger.info("empty issue wasn't created")
    time.sleep(2)
