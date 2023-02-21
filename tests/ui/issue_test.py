import time

import pytest

from src.jira_test_framework.ui.dashboard_page import DashboardPage
from src.jira_test_framework.ui.login_page import LoginPage
from tests.ui.driver_factory import get_chrome_driver

USERNAME = "itzikv3@gmail.com"
PASSWORD = "itzikpass"


@pytest.fixture
def driver():
    driver = get_chrome_driver()
    yield driver
    driver.close()


def test_create_issue(driver):
    login(driver)
    dashboard_page = DashboardPage(driver)
    # TODO - project_name!
    dashboard_page.go_to_project("ss")
    dashboard_page.click_backlog()
    dashboard_page.create_issue("from test ui - can delete")
    # time.sleep(2)
    # TODO    need assertion + delete + log


# TODO def create_empty_issue

def login(driver):
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)
