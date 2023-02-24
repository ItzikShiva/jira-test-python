from datetime import datetime
import pytest

from src.jira_test_framework.ui.dashboard_page import DashboardPage
from src.jira_test_framework.ui.login_page import LoginPage
from tests.ui.driver_factory import get_chrome_driver

USERNAME = "itzikv3@gmail.com"
PASSWORD = "itzikpass1212"


@pytest.fixture
def driver():
    driver = get_chrome_driver()
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver\chromedriver.exe', options=options)
    yield driver
    driver.close()


def test_create_issue(driver):
    login(driver)
    dashboard_page = DashboardPage(driver)
    # TODO - project_name!
    dashboard_page.go_to_project("ss")
    dashboard_page.click_backlog()

    timestamp_str = str(datetime.now().timestamp())
    issue_text = "from test ui - can delete " + timestamp_str

    dashboard_page.create_issue(issue_text)
    # TODO    need assertion + delete + log
    dashboard_page.delete_issue(timestamp_str)
    time.sleep(2)


# TODO def create_empty_issue

def login(driver):
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)
