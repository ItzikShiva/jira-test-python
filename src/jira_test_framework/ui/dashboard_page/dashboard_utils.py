import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from src.logger import logger


class DashboardUtils:
    SEARCH_XPATH_LOCATOR = "//input[@aria-label]"

    @staticmethod
    def clear_search_tab(driver):
        driver.find_element(By.XPATH, '//span[@aria-label="Clear"]').click()

    @staticmethod
    def search(driver, issue_value):
        """
        Searches for the given issue_value using the search box on the dashboard page.
        :param driver: Selenium WebDriver instance
        :param issue_value: the value to search for
        :return: the element found after the search
        """
        # TODO - ask, i thought to write here log, but it feels to much, what do you say?
        time.sleep(2)
        search_element = driver.find_element(By.XPATH, DashboardUtils.SEARCH_XPATH_LOCATOR)
        search_element.click()
        search_element.send_keys(issue_value)

        time.sleep(1)
        return driver.find_element(By.XPATH, '//div[@role="presentation"]//mark')
