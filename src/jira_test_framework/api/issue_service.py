import requests

from src.logger import logger


class IssueService:
    base_url = "https://api.atlassian.com/ex/jira/93916ef5-a97b-47de-9a28-80fe8572a67e/rest/api/3/issue/"
    headers = {"Accept": "application/json"}

    def __init__(self, api_login_service=None):
        self.api_login_service = api_login_service

    def create_issue_issue(self, issue_request, token=None):
        logger.info("creating new issue from API")
        self.headers.update({"Authorization": self.api_login_service.token if token is None else token})
        return requests.post(self.base_url, headers=self.headers, json=issue_request)

    def get_issue(self, issue_key, token=None):
        logger.info("getting issue with key: " + issue_key + " from API")
        url = self.base_url + issue_key

        self.headers.update({"Authorization": self.api_login_service.token if token is None else token})

        return requests.get(url, headers=self.headers)
