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

    AUTHORIZATION_CODE = "authorization_code"
    CLIENT_ID = "EMcZzazmRdqdGmD48zjmCD3tVielmpwN"
    CLIENT_SECRET = "ATOAGP08RpVfirid_8ZpNWXQagGIMv_cMrGITtoODjN5GIcDlbXL-jmsZOmeUDV7wbTkC73F4623"
    REDIRECT_URI = "https://task-day.onrender.com/"
    driver = None

    """
    # Performs a series of actions to obtain an access token:
    # 1. Logs in to a website.
    # 2. Authorizes access.
    # 3. Waits for the expected title to appear.
    # 4. Obtains a code from the URL.
    # 5. Exchanges the code for an access token.
    # Returns the access token.
    """

    def get_token_process(self, scope=None):
        logger.info("start get-token process")
        self.driver = APILoginService.get_chrome_driver()

        get_token_login_page = GetTokenLoginPage(self.driver)

        #todo - ask - this is another option instead of if -  authorize_page = get_token_login_page.login(None if scope is None else scope)
        if scope is None:
            authorize_page = get_token_login_page.login()
        else:
            authorize_page = get_token_login_page.login(scope)

        time.sleep(4)

        authorize_page.authorize_access()

        self.wait_for_expected_title("Taskday")
        logger.info("login and authorization successful")

        self.code = self.get_code_from_url()
        self.driver.close()

        self.token = self.get_access_token()

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
        logger.info("getting CODE from url")
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
        logger.info("getting token from API")
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

        if response.status_code == 200:
            token = "Bearer " + response.json()["access_token"]
            return token
        else:
            return None

    def get_token(self):
        return self.token
