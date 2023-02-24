import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage():
    project_elements_css_locator = 'p[data-testid="deep-dive-card-content--project-name-heading"]'
    backlog_element_xpath_locator = '//span[contains(text(), "Backlog")]'
    create_issue_element_xpath_locator = '//div[contains(text(), "Create issue")]'
    create_issue_textarea_element_css_locator = 'textarea[placeholder="What needs to be done?"]'

    def __init__(self, driver):
        self.driver = driver

    # TODO - use the project_name
    def go_to_project(self, project_name):
        project_elements = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_any_elements_located(
                (By.CSS_SELECTOR, self.project_elements_css_locator)))
        project_elements[0].click()

    def click_backlog(self):
        backlog_element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            (By.XPATH, self.backlog_element_xpath_locator)))
        backlog_element.click()

    def create_issue(self, issue_value):
        create_issue_element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.create_issue_element_xpath_locator)))
        create_issue_element.click()

        create_issue_textarea_element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.create_issue_textarea_element_css_locator)))
        create_issue_textarea_element.send_keys(issue_value)
        create_issue_textarea_element.send_keys(Keys.RETURN)

    def delete_issue(self, issue_value):
        # TODO - shot Hod what is contain and what is exact with contains(., 456) and contains(., '456')

        time.sleep(2)

        search_element = self.driver.find_element(By.XPATH, "//input[@aria-label]")
        search_element.click()
        search_element.send_keys("456")
        search_element.click()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='ak-main-content']//div[@data-test-id='software-backlog.card-list.id-2']//div[contains(., 456)]").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@aria-label='Actions']").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(), 'Delete')]").click()
        self.driver.find_elements(By.XPATH, "//span[contains(text(), 'Delete')]")[1].click()

        time.sleep(2)

        # TODO - addd timestamp

