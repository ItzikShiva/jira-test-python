from src.jira_test_framework.ui.login_page import LoginPage
from tests.ui.constants import USERNAME, PASSWORD


def login(driver):
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)
