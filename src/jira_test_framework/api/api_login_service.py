import json
import time
from datetime import timedelta

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.jira_test_framework.ui.get_token.authorize_page import AuthorizePage
from src.jira_test_framework.ui.get_token.get_token_login_page import GetTokenLoginPage
from src.jira_test_framework.ui.ui_utils import UIUtils
from src.logger import logger


class APILoginService:
    code = None
    token = None

    authorization_code = "authorization_code";
    client_id = "EMcZzazmRdqdGmD48zjmCD3tVielmpwN";
    client_secret = "ATOAGP08RpVfirid_8ZpNWXQagGIMv_cMrGITtoODjN5GIcDlbXL-jmsZOmeUDV7wbTkC73F4623";
    redirect_uri = "https://task-day.onrender.com/";

    # def __init__(self, driver):
    #     driver = driver

    def get_token(self):
        logger.info("start login proccess")
        driver = APILoginService.get_chrome_driver()

        get_token_login_page = GetTokenLoginPage(driver)
        get_token_login_page.login()

        # todo - waitForExpectedTitle(driver, "Authorize app")
        time.sleep(4)

        authorize_page = AuthorizePage(driver)
        authorize_page.authorize_access()
        # todo - all next will be authrize page (return new AuthorizePage(driver);)

        APILoginService.wait_for_expected_title(driver, "Taskday")
        logger.info("login and authorization successful")

        code = APILoginService.get_code_from_url(driver)
        driver.close()

        self.get_access_token(code)

    def get_access_token(self, code):
        url = "https://auth.atlassian.com/oauth/token"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        data = {
            "grant_type": self.authorization_code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code,
            "redirect_uri": self.redirect_uri
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.ok:
            return "Bearer " + response.json()["access_token"]
        else:
            return None

        """
            public static String getAccessToken(String code) {
        logger.info("getting TOKEN from server");
        String url = "https://auth.atlassian.com/oauth/token";

        GetAccessTokenRequest getAccessTokenRequest = new GetAccessTokenRequest(code);
        RequestBody body = RequestBody.create(gson.toJson(getAccessTokenRequest), jsonMediaType);
        Request request = new Request.Builder().url(url).post(body).build();

        Response response = executeMethod(request, logger);
        return "Bearer " + getTokenFromResponse(response);
    }
        """

    def wait_for_expected_title(driver, expected_title):
        """
        wait for specific title of web page. return true if happen, else false.
        """
        wait = WebDriverWait(driver, 25)
        return wait.until(EC.title_contains(expected_title))
        # return wait.until(EC.title_is(expected_title))

    def get_code_from_url(driver):
        """
        get secret code that generate from url
        """
        url = driver.current_url
        hash_index = url.find("#")
        return url[url.index("code=") + 5:hash_index]

    # change / delete after:
    @staticmethod
    def get_chrome_driver():
        # this "option" because old writing is deprecated & to cancel an error of "USB: usb_device_handle..." 19-2-23
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--start-maximized")
        return webdriver.Chrome(executable_path='C:\Drivers\chromedriver\chromedriver.exe', options=options)


"""
public LoginPageWeb(WebDriver driver, String scope) {
		super(driver);
		setBaseCodeUrl(scope);
		logger.info("open\start login page");
		driver.get(baseCodeUrl);
		this.driver = driver;
	}
	
	
	********************************************************
	
	public AuthorizePage login() {
		return login(username, password);
	}

	public AuthorizePage login(String username, String password) {
		logger.info("start login proccess");

		usernameElement = waitForElementByLocator(driver, usernameElementLocator);
		setUsername(username);

		continueButton = waitForElementByLocator(driver, continueButtonLocator);
		continueButton.click();

		loginButton = waitForElementByLocator(driver, loginButtonLocator);
		passwordElement = waitForElementByLocator(driver, passwordElementLocator);

		setPassword(password);
		submit();
		if (waitForExpectedTitle(driver, "Authorize app")) {
			logger.info("first step login successful going to authorization");
		} else {
			logger.error("login not successful");
		}

		return new AuthorizePage(driver);
	}

"""
