import time

from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage():
    username = "itzikv3@gmail.com"
    password = "itzikpass"
    scope = "read:me"
    base_code_url = "https://auth.atlassian.com/authorize?audience=api.atlassian.com&client_id" \
                    "=EMcZzazmRdqdGmD48zjmCD3tVielmpwN&scope=" + scope + \
                    "&redirect_uri=https%3A%2F%2Ftask-day.onrender.com%2F&response_type=code&prompt=consent"

    username_name_locator = "username"
    password_name_locator = "password"
    choose_elements_xpath_locator = "//*[text()='Choose a site']"
    automat_value_xpath_locator = "//*[text()='automat-ct.atlassian.net']"
    accept_button_xpath_locator = "//*[text()='Accept']"

    def __init__(self):
        # this "option" because old writing is deprecated & to cancel an error of "USB: usb_device_handle..." 19-2-23
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self.base_code_url)

    # def login(self, username, password):
    def login(self):
        username_element = self.driver.find_element(By.NAME, self.username_name_locator)
        username_element.send_keys(self.username)
        username_element.send_keys(Keys.RETURN)

        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.password_name_locator)))
        password.send_keys(self.password)

        # 2 option:
        # password.click()
        password.send_keys(Keys.RETURN)

        choose_elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.choose_elements_xpath_locator)))
        choose_elements.click()

        automat_value = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.automat_value_xpath_locator)))
        automat_value.click()

        # time.sleep(2)
        accept_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.accept_button_xpath_locator)))
        time.sleep(4)
        accept_button.click()

    # get code

        time.sleep(2)
        self.driver.close()
