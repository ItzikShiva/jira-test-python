import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from src.jira_test_framework.ui.dashboard_page.dashboard_utils import DashboardUtils
from src.jira_test_framework.ui.ui_utils import UIUtils
from src.logger import logger


class DashboardPage():
    # PROJECT_NAME_CSS_LOCATOR = 'p[data-testid="deep-dive-card-content--project-name-heading"]'
    BACKLOG_XPATH_LOCATOR = '//span[contains(text(), "Backlog")]'
    CREATE_ISSUE_XPATH_LOCATOR = '//div[contains(text(), "Create issue")]'
    CREATE_ISSUE_TEXTAREA_CSS_LOCATOR = 'textarea[placeholder="What needs to be done?"]'

    ACTION_BUTTON_XPATH_LOCATOR = "//button[@aria-label='Actions']"
    DELETE_BUTTON_XPATH_LOCATOR = "//span[contains(text(), 'Delete')]"
    DELETE_BUTTONS_APPROVE_XPATH_LOCATOR = "//span[contains(text(), 'Delete')]"

    ISSUE_SUMMARY_XPATH_LOCATOR = "//h1[@data-test-id='issue.views.issue-base.foundation.summary.heading']"
    ISSUE_SUMMARY_WRITING_XPATH_LOCATOR = "//h1[@data-test-id='issue.views.issue-base.foundation.summary.heading.writeable']//textarea"

    def __init__(self, driver):
        self.driver = driver

    def edit_issue(self, old_issue_value, new_issue_value):
        logger.info("editing issue with value: " + old_issue_value + " to new value: " + new_issue_value)

        DashboardUtils.search(self.driver, old_issue_value).click()

        UIUtils.wait_for_element_visibility(self.driver, By.XPATH, self.ISSUE_SUMMARY_XPATH_LOCATOR).click()

        issue_summary_element_writing = self.driver.find_element(By.XPATH,
                                                                 self.ISSUE_SUMMARY_WRITING_XPATH_LOCATOR)
        issue_summary_element_writing.send_keys(Keys.CONTROL + "a")
        issue_summary_element_writing.send_keys(new_issue_value)
        issue_summary_element_writing.send_keys(Keys.ENTER)

        DashboardUtils.clear_search_tab(self.driver)

    def go_to_project(self, project_name):
        """
        Opens the project with the specified name.
        :param project_name: The name of the project.
        """
        logger.info("Opening project: %s", project_name)
        projects_xpath_locator = f'// p[contains(text(), "{project_name}")]'

        UIUtils.wait_for_visibility_of_any_elements(self.driver, By.XPATH, projects_xpath_locator)[0].click()

    def go_to_backlog(self):
        logger.info("Opening backlog")

        UIUtils.wait_for_element_visibility(self.driver, By.XPATH, self.BACKLOG_XPATH_LOCATOR).click()

    def create_issue(self, issue_value):
        logger.info("creating issue with value: %s", issue_value)

        UIUtils.wait_for_element_visibility(self.driver, By.XPATH, self.CREATE_ISSUE_XPATH_LOCATOR).click()

        create_issue_textarea_element = UIUtils.wait_for_element_visibility(self.driver, By.CSS_SELECTOR,
                                                                            self.CREATE_ISSUE_TEXTAREA_CSS_LOCATOR)
        create_issue_textarea_element.send_keys(issue_value)
        create_issue_textarea_element.send_keys(Keys.RETURN)

    def delete_issue(self, issue_value):
        # TODO - show Hod what is contain and what is exact with contains(., 456) and contains(., '456')

        logger.info("deleting issue with value: %s", issue_value)

        DashboardUtils.search(self.driver, issue_value).click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, self.ACTION_BUTTON_XPATH_LOCATOR).click()
        self.driver.find_element(By.XPATH, self.DELETE_BUTTON_XPATH_LOCATOR).click()
        self.driver.find_elements(By.XPATH, self.DELETE_BUTTONS_APPROVE_XPATH_LOCATOR)[1].click()

    def delete_issue_v1(self, issue_value):
        logger.info("deleting issue with value: %s", issue_value)

        DashboardUtils.search(self.driver, issue_value).click()

        UIUtils.wait_for_element_visibility(self.driver, By.XPATH, self.ACTION_BUTTON_XPATH_LOCATOR).click()
        UIUtils.wait_for_element_visibility(self.driver, By.XPATH, self.DELETE_BUTTON_XPATH_LOCATOR).click()
        UIUtils.wait_for_visibility_of_any_elements(self.driver, By.XPATH, self.DELETE_BUTTONS_APPROVE_XPATH_LOCATOR)[
            1].click()

    def is_issue_exist(self, issue_value):
        """
        Checks if a Jira issue with the given value exists by searching for it in the dashboard search bar.
        :param issue_value: the value of the issue to search for
        :return: True if the issue is found, False otherwise
        :raises NoSuchElementException: if the search bar or the issue itself cannot be found
        """
        # this is another options to check if the element finds.. - if int(is_issue_exist.size['width']) > 0
        try:
            DashboardUtils.search(self.driver, issue_value)
            DashboardUtils.clear_search_tab(self.driver)
            return True
        except NoSuchElementException:
            return False
