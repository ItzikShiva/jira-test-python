import json
import time

import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.jira_test_framework.ui.get_token.get_token_login_page import GetTokenLoginPage
from src.logger import logger


class APILoginService:
    code = None
    token = None

    AUTHORIZATION_CODE = "authorization_code";
    CLIENT_ID = "EMcZzazmRdqdGmD48zjmCD3tVielmpwN";
    CLIENT_SECRET = "ATOAGP08RpVfirid_8ZpNWXQagGIMv_cMrGITtoODjN5GIcDlbXL-jmsZOmeUDV7wbTkC73F4623";
    REDIRECT_URI = "https://task-day.onrender.com/";
    driver = None

    # def __init__(self, driver):
    #     driver = driver

    def get_token(self):
        logger.info("start login proccess")
        self.driver = APILoginService.get_chrome_driver()

        get_token_login_page = GetTokenLoginPage(self.driver)
        authorize_page = get_token_login_page.login()

        time.sleep(4)

        authorize_page.authorize_access()
        # todo - all next will be authrize page (return new AuthorizePage(driver);)

        self.wait_for_expected_title("Taskday")
        logger.info("login and authorization successful")

        self.code = self.get_code_from_url()
        self.driver.close()

        self.get_access_token()

    def wait_for_expected_title(self, expected_title: str) -> bool:
        """
        wait for specific title of web page. return true if happen, else false.
        """
        wait = WebDriverWait(self.driver, 25)
        return wait.until(EC.title_contains(expected_title))
        # return wait.until(EC.title_is(expected_title))

    def get_code_from_url(self) -> str:
        """
        get secret code that generate from url
        """
        url = self.driver.current_url
        hash_index = url.find("#")
        return url[url.index("code=") + 5:hash_index]

    # change / delete after:
    @staticmethod
    def get_chrome_driver() -> webdriver:
        # this "option" because old writing is deprecated & to cancel an error of "USB: usb_device_handle..." 19-2-23
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--start-maximized")
        return webdriver.Chrome(executable_path='C:\Drivers\chromedriver\chromedriver.exe', options=options)

    def get_access_token(self):
        url = "https://auth.atlassian.com/oauth/token"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        data = {
            "grant_type": self.AUTHORIZATION_CODE,
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "code": self.code,
            "redirect_uri": self.REDIRECT_URI
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.ok:
            token = "Bearer " + response.json()["access_token"]
            return token
        else:
            return None