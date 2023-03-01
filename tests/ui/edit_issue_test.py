import pytest

from src.logger import logger
from src.jira_test_framework.ui.dashboard_page.dashboard_page import DashboardPage
from tests.ui.constants import PROJECT_NAME, ISSUE_VALUE_TO_EDIT, NEW_ISSUE_VALUE
from tests.ui.driver_factory import get_chrome_driver
from tests.ui.ui_utils import login


@pytest.fixture
def driver():
    driver = get_chrome_driver()
    yield driver
    driver.close()


def test_edit_issue(driver):
    login(driver)
    dashboard_page = DashboardPage(driver)

    dashboard_page.go_to_project(PROJECT_NAME)
    dashboard_page.go_to_backlog()

    dashboard_page.create_issue(ISSUE_VALUE_TO_EDIT)
    assert dashboard_page.is_issue_exist(ISSUE_VALUE_TO_EDIT) == True
    logger.info("issue with value: " + ISSUE_VALUE_TO_EDIT + ". was created for testing purpose")

    dashboard_page.edit_issue(ISSUE_VALUE_TO_EDIT, NEW_ISSUE_VALUE)
    assert dashboard_page.is_issue_exist(NEW_ISSUE_VALUE) == True
    logger.info("issue with old value: " + ISSUE_VALUE_TO_EDIT + ". was update to new value: " + NEW_ISSUE_VALUE)

    dashboard_page.delete_issue(NEW_ISSUE_VALUE)
    assert dashboard_page.is_issue_exist(NEW_ISSUE_VALUE) == False
    logger.info("issue with value: " + NEW_ISSUE_VALUE + ". was deleted")
