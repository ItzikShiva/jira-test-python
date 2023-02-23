import time

from selenium.webdriver.common.action_chains import ActionChains
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

    # TODO - ask, i delete after click the element, but there's hover also. show to Hod
    def delete_issue(self, issue_value):
        # TODO - shot Hod what is contain and what is exact with contains(., 456) and contains(., '456')
        # TODO - check iframe

        # iframe_element = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, "//div[@data-onboarding-observer-id='backlog-wrapper']")))
        # iframe_element.click()

        search_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@aria-label]")))
        search_element.send_keys("456")
        search_element.click()
        # //input[@aria-label]

        # element = self.driver.find_element(By.XPATH, "//div[@data-onboarding-observer-id='backlog-wrapper']")
        # actions = ActionChains(self.driver)







        time.sleep(10)
        issue_elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located((By.XPATH, "//span[contains(., 456)]")))
        # //span[contains(text(), '456')]
        # //button[@aria-label[contains(., 456)]]
        issue_elements[0].click()

        delete_button_from_dropdown_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Delete')]")))
        delete_button_from_dropdown_element.click()

        # //span[contains(text(), 'Delete')]
        # <span class="ItemParts__Content-sc-14xek3m-5 jRBaLt">Delete</span>
        #
        delete_button_elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located((By.XPATH, "//span[contains(text(), 'Delete')]")))
        delete_button_elements[1].click()

        # /html/body/div[16]/div[2]/div/div[3]/div/div/section/div[3]/button[1]
        # //*[@id="jira"]/div[16]/div[2]/div/div[3]/div/div/section/div[3]/button[1]/span

        time.sleep(2)

# TODO - addd timestamp

# By.XPATH, "//span[contains(@class, 'css-hdknak') and @data-item-title='true' and text()='from test ui - can delete']"
# By.XPATH, '//span[contains(text(), "from test ui - can delete")]'
# By.CSS_SELECTOR, 'span.css-hdknak[data-item-title="true"]'


# menu_element = WebDriverWait(self.driver, 30).until(
#     EC.visibility_of_element_located(
#         (By.XPATH, 'button[data-testid="issue-meatball-menu.ui.dropdown-trigger.button"]')))
# menu_element.click()
#


#         <button aria-label="Actions" aria-expanded="false" class="css-d45s07" data-testid="issue-meatball-menu.ui.dropdown-trigger.button" type="button" tabindex="0"><span class="css-16j5qb5"><span aria-hidden="true" class="css-1afrefi" style="--icon-primary-color:currentColor; --icon-secondary-color:var(--ds-surface, #FFFFFF);"><svg width="24" height="24" viewBox="0 0 24 24" role="presentation"><g fill="currentColor" fill-rule="evenodd"><circle cx="5" cy="12" r="2"></circle><circle cx="12" cy="12" r="2"></circle><circle cx="19" cy="12" r="2"></circle></g></svg></span></span></button>
