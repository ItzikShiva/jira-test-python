import json

import requests

from src.logger import logger


class IssueService:

    def __init__(self, api_login_service):
        self.api_login_service = api_login_service

    # @staticmethod
    def get_issue(self, issue_key, token=None):
        logger.info("getting issue with key: " + issue_key + " from API")
        base_url = f"https://api.atlassian.com/ex/jira/93916ef5-a97b-47de-9a28-80fe8572a67e/rest/api/3/issue/{issue_key}"

        headers = {
            "Accept": "application/json",
            "Authorization": self.api_login_service.token if token is None else token
        }
        data = {
        }
        return requests.get(base_url, headers=headers, data=json.dumps(data))

        # if response.status_code == 200:
        #     token = "Bearer " + response.json()["access_token"]
        #     return token
        # else:
        #     return None
