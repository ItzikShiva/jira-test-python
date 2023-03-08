import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from src.jira_test_framework.ui.ui_utils import UIUtils
from src.logger import logger


class DashboardPage():
    BACKLOG_LOCATOR = {"by": By.XPATH, "locator_string": '//span[contains(text(), "Backlog")]'}
    CREATE_ISSUE_LOCATOR = {"by": By.XPATH, "locator_string": '//div[contains(text(), "Create issue")]'}

    CREATE_ISSUE_TEXTAREA_LOCATOR = {"by": By.CSS_SELECTOR,
                                     "locator_string": 'textarea[placeholder="What needs to be done?"]'}

    ACTION_BUTTON_LOCATOR = {"by": By.XPATH, "locator_string": "//button[@aria-label='Actions']"}
    DELETE_BUTTON_LOCATOR = {"by": By.XPATH, "locator_string": "//span[contains(text(), 'Delete')]"}
    DELETE_BUTTONS_APPROVE_LOCATOR = {"by": By.XPATH, "locator_string": "//span[contains(text(), 'Delete')]"}

    ISSUE_SUMMARY_LOCATOR = {"by": By.XPATH,
                             "locator_string": "//h1[@data-test-id='issue.views.issue-base.foundation.summary.heading']"}
    ISSUE_SUMMARY_WRITING_LOCATOR = {"by": By.XPATH,
                                     "locator_string": "//h1[@data-test-id='issue.views.issue-base.foundation.summary.heading.writeable']//textarea"}

    SEARCH_XPATH_LOCATOR = {"by": By.XPATH, "locator_string": "//input[@aria-label]"}
    CLEAR_SEARCH_LOCATOR = {"by": By.XPATH, "locator_string": '//span[@aria-label="Clear"]'}
    FOUND_BY_SEARCH_LOCATOR = {"by": By.XPATH, "locator_string": '//div[@role="presentation"]//mark'}

    def __init__(self, driver):
        self.driver = driver

    def edit_issue(self, old_issue_value, new_issue_value):
        logger.info("editing issue with value: " + old_issue_value + " to new value: " + new_issue_value)

        self.search(old_issue_value).click()

        UIUtils.wait_for_element_visibility(self.driver, self.ISSUE_SUMMARY_LOCATOR).click()

        issue_summary_element_writing = UIUtils.find_element(self.driver, self.ISSUE_SUMMARY_WRITING_LOCATOR)
        issue_summary_element_writing.send_keys(Keys.CONTROL + "a")
        issue_summary_element_writing.send_keys(new_issue_value)
        issue_summary_element_writing.send_keys(Keys.ENTER)

        self.clear_search_tab()

    def go_to_project(self, project_name):
        """
        Opens the project with the specified name.
        :param project_name: The name of the project.
        """
        logger.info("Opening project: %s", project_name)
        string_project_locator = f'// p[contains(text(), "{project_name}")]'
        projects_locator = {"by": By.XPATH, "locator_string": string_project_locator}

        UIUtils.wait_for_visibility_of_any_elements(self.driver, projects_locator)[0].click()

    def go_to_backlog(self):
        logger.info("Opening backlog")

        UIUtils.wait_for_element_visibility(self.driver, self.BACKLOG_LOCATOR).click()

    def create_issue(self, issue_value):
        logger.info("creating issue with value: %s", issue_value)

        UIUtils.wait_for_element_visibility(self.driver, self.CREATE_ISSUE_LOCATOR).click()

        create_issue_textarea_element = UIUtils.wait_for_element_visibility(self.driver,
                                                                            self.CREATE_ISSUE_TEXTAREA_LOCATOR)
        create_issue_textarea_element.send_keys(issue_value)
        create_issue_textarea_element.send_keys(Keys.RETURN)

    def delete_issue(self, issue_value):
        # TODO - show Hod what is contain and what is exact with contains(., 456) and contains(., '456')

        logger.info("deleting issue with value: %s", issue_value)

        self.search(issue_value).click()

        time.sleep(3)
        UIUtils.find_element(self.driver, self.ACTION_BUTTON_LOCATOR).click()
        UIUtils.find_element(self.driver, self.DELETE_BUTTON_LOCATOR).click()
        UIUtils.find_elements(self.driver, self.DELETE_BUTTONS_APPROVE_LOCATOR)[1].click()

    def delete_issue_v1(self, issue_value):
        logger.info("deleting issue with value: %s", issue_value)

        self.search(issue_value).click()

        UIUtils.wait_for_element_visibility(self.driver, self.ACTION_BUTTON_LOCATOR).click()
        UIUtils.wait_for_element_visibility(self.driver, self.DELETE_BUTTON_LOCATOR).click()
        UIUtils.wait_for_visibility_of_any_elements(self.driver, self.DELETE_BUTTONS_APPROVE_LOCATOR)[
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
            self.search(issue_value)
            self.clear_search_tab()
            return True
        except NoSuchElementException:
            return False

    def clear_search_tab(self):
        UIUtils.find_element(self.driver, self.CLEAR_SEARCH_LOCATOR).click()

    def search(self, issue_value):
        """
        Searches for the given issue_value using the search box on the dashboard page.
        :param driver: Selenium WebDriver instance
        :param issue_value: the value to search for
        :return: the element found after the search
        """
        # TODO - ask, i thought to write here log, but it feels to much, what do you say?
        time.sleep(2)
        search_element = UIUtils.find_element(self.driver, self.SEARCH_XPATH_LOCATOR)
        search_element.click()
        search_element.send_keys(issue_value)

        time.sleep(1)
        return UIUtils.find_element(self.driver, self.FOUND_BY_SEARCH_LOCATOR)
