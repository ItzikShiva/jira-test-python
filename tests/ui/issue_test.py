import time
from datetime import datetime
import pytest

from src.jira_test_framework.ui.dashboard_page import DashboardPage
from tests.ui.constants import PROJECT_NAME
from tests.ui.driver_factory import get_chrome_driver
from tests.ui.ui_utils import login


@pytest.fixture
def driver():
    driver = get_chrome_driver()
    yield driver
    driver.close()


def test_create_issue(driver):
    timestamp_str = str(datetime.now().timestamp())
    issue_text = "from test ui - can delete " + timestamp_str

    login(driver)
    dashboard_page = DashboardPage(driver)

    dashboard_page.go_to_project(PROJECT_NAME)
    dashboard_page.click_backlog()

    dashboard_page.create_issue(issue_text)
    # TODO    need assertion + log
    # two options:
    # dashboard_page.delete_issue(timestamp_str)
    dashboard_page.delete_issue_v1(timestamp_str)
    time.sleep(2)

# TODO def create_empty_issue
