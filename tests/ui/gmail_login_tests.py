from selenium import webdriver
from src.jira_test_framework.ui.gmail_login_page import GmailLoginPage


class TestGmailLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver\chromedriver.exe')
        self.login_page = GmailLoginPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_login(self):
        self.login_page.login("your-email-address@gmail.com", "your-password")
        assert "Gmail" in self.driver.title
