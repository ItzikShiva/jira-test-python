import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.logger import logger


class DashboardPage():
    project_elements_css_locator = 'p[data-testid="deep-dive-card-content--project-name-heading"]'
    backlog_element_xpath_locator = '//span[contains(text(), "Backlog")]'
    create_issue_element_xpath_locator = '//div[contains(text(), "Create issue")]'
    create_issue_textarea_element_css_locator = 'textarea[placeholder="What needs to be done?"]'

    search_element_locator = "//input[@aria-label]"
    action_button_locator = "//button[@aria-label='Actions']"
    delete_button_locator = "//span[contains(text(), 'Delete')]"
    delete_buttons_approve_locator = "//span[contains(text(), 'Delete')]"

    def __init__(self, driver):
        self.driver = driver

    def edit_issue(self, old_issue_value, new_issue_value):
        logger.info("editing issue with value: " + old_issue_value + " to new value: " + new_issue_value)

        self.search(old_issue_value).click()

        issue_element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//h1[@data-test-id="issue.views.issue-base.foundation.summary.heading"]')))

        issue_element.click()
        issue_element_writing = self.driver.find_element(By.XPATH,
                                                         '//h1[@data-test-id="issue.views.issue-base.foundation.summary.heading.writeable"]//textarea')

        issue_element_writing.send_keys(Keys.CONTROL + "a")
        issue_element_writing.send_keys(new_issue_value)
        issue_element_writing.send_keys(Keys.ENTER)
        self.clear_search_tab()

    def clear_search_tab(self):
        clear_element = self.driver.find_element(By.XPATH, '//span[@aria-label="Clear"]')
        clear_element.click()


    def search(self, issue_value):
        # TODO - ask, i thought to write here log, but it feels to much, what do you say?
        time.sleep(2)
        search_element = self.driver.find_element(By.XPATH, self.search_element_locator)
        search_element.click()
        search_element.send_keys(issue_value)
        # search_element.click()

        time.sleep(1)
        # OLD return - option 1 - suddenly not work
        # return self.driver.find_element(By.XPATH, f"//*[@id='ak-main-content']//div[@data-test-id='software-backlog.card-list.id-2']//div[contains(., '{issue_value}')]")
        # NEW return - working
        # return self.driver.find_element(By.XPATH,  "//span[@class='css-hdknak']//mark")
        return self.driver.find_element(By.XPATH, '//div[@role="presentation"]//mark')

    def is_issue_exist(self, issue_value):
        # this is another options to check if the element finds.. - if int(is_issue_exist.size['width']) > 0
        try:
            self.search(issue_value)
            self.clear_search_tab()
            return True
        except NoSuchElementException:
            return False

    def go_to_project(self, project_name):
        logger.info("open project: " + project_name)
        project_elements_xpath_locator = f'// p[contains(text(), "{project_name}")]'

        project_elements = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_any_elements_located(
                (By.XPATH, project_elements_xpath_locator)))

        project_elements[0].click()

    def click_backlog(self):
        logger.info("open backlog")

        backlog_element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, self.backlog_element_xpath_locator)))
        backlog_element.click()

    def create_issue(self, issue_value):
        logger.info("creating issue with value: " + issue_value)

        create_issue_element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.create_issue_element_xpath_locator)))
        create_issue_element.click()

        create_issue_textarea_element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.create_issue_textarea_element_css_locator)))
        create_issue_textarea_element.send_keys(issue_value)
        create_issue_textarea_element.send_keys(Keys.RETURN)

    def delete_issue(self, issue_timestamp):
        # TODO - show Hod what is contain and what is exact with contains(., 456) and contains(., '456')

        logger.info("deleting issue with value: " + issue_timestamp)

        self.search(issue_timestamp).click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, self.action_button_locator).click()
        self.driver.find_element(By.XPATH, self.delete_button_locator).click()
        self.driver.find_elements(By.XPATH, self.delete_buttons_approve_locator)[1].click()

    def delete_issue_v1(self, issue_timestamp):
        logger.info("deleting issue with value: " + issue_timestamp)

        self.search(issue_timestamp).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.action_button_locator))).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.delete_button_locator))).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located((By.XPATH, self.delete_buttons_approve_locator)))[1].click()
