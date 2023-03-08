from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UIUtils:

    @staticmethod
    def wait_for_element_visibility1(driver, locator_type, locator_string, timeout=30):
        """
        Waits for visibility of the element using WebDriverWait and ExpectedConditions
       :param driver: Selenium WebDriver instance
       :param locator_type: the locator type (e.g. By.XPATH, By.CSS_SELECTOR)
       :param locator_string: the locator string (e.g. "//div[@class='issue-summary']", ".my-class")
       :param timeout: timeout in seconds (default 30)
       :return: the element found
       """
        locator = (locator_type, locator_string)
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

    @staticmethod
    def wait_for_element_visibility(driver, locator, timeout=30):
        # locator = (locator_type, locator_string)
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((locator["by"], locator["locator_string"])))

    @staticmethod
    def find_element(driver, locator):
        return driver.find_element(locator["by"], locator["locator_string"])

    @staticmethod
    def find_elements(driver, locator):
        return driver.find_elements(locator["by"], locator["locator_string"])

    @staticmethod
    def wait_for_visibility_of_any_elements(driver, locator, timeout=30):
        """
        same as wait_for_element_visibility() but for list of elements!
        :return: a list of visible elements found
        """
        # EC.visibility_of_any_elements_located(By.XPATH,"")
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_any_elements_located((locator["by"], locator["locator_string"])))
