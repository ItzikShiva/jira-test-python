import pytest

from src.logger import logger
from src.jira_test_framework.ui.dashboard_page.dashboard_page import DashboardPage
from tests.ui.constants import PROJECT_NAME, ISSUE_VALUE_TO_EDIT, NEW_ISSUE_VALUE
from src.jira_test_framework.ui.driver_factory import get_chrome_driver
from tests.ui.ui_utils import ui_login


@pytest.fixture
def get_dashboard_and_driver():
    driver = get_chrome_driver()
    ui_login(driver)
    dashboard_page = DashboardPage(driver)
    dashboard_page.go_to_project(PROJECT_NAME)
    dashboard_page.go_to_backlog()
    yield driver, dashboard_page
    driver.close()


def test_edit_issue(get_dashboard_and_driver):
    driver, dashboard_page = get_dashboard_and_driver

    create_issue(dashboard_page)
    edit_issue(dashboard_page)
    delete_issue(dashboard_page)


def delete_issue(dashboard_page):
    dashboard_page.delete_issue(NEW_ISSUE_VALUE)
    assert dashboard_page.is_issue_exist(NEW_ISSUE_VALUE) == False
    logger.info("issue with value: " + NEW_ISSUE_VALUE + ". was deleted")


def edit_issue(dashboard_page):
    dashboard_page.edit_issue(ISSUE_VALUE_TO_EDIT, NEW_ISSUE_VALUE)
    assert dashboard_page.is_issue_exist(NEW_ISSUE_VALUE) == True
    logger.info("issue with old value: " + ISSUE_VALUE_TO_EDIT + ". was update to new value: " + NEW_ISSUE_VALUE)


def create_issue(dashboard_page):
    dashboard_page.create_issue(ISSUE_VALUE_TO_EDIT)
    assert dashboard_page.is_issue_exist(ISSUE_VALUE_TO_EDIT) == True
    logger.info("issue with value: " + ISSUE_VALUE_TO_EDIT + ". was created for testing purpose")
