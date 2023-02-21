# class="sc-1p2gpiw-3 hVfRVu"
# class="sc-1p2gpiw-3 hVfRVu"
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class DashboardPage():
    project_elements_css_locator = 'p[data-testid="deep-dive-card-content--project-name-heading"]'

    def __init__(self, driver):
        self.driver = driver

    # TODO - use the project_name
    def go_to_project(self, project_name):
        project_elements = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_any_elements_located(
                (By.CSS_SELECTOR, self.project_elements_css_locator)))
        project_elements[0].click()

