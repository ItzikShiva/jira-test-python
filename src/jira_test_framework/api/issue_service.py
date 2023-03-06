import json

import requests

from src.logger import logger


class IssueService:

    def __init__(self, api_login_service):
        self.api_login_service = api_login_service

    def create_issue_issue(self, issue_request, token=None):
        url = "https://api.atlassian.com/ex/jira/93916ef5-a97b-47de-9a28-80fe8572a67e/rest/api/3/issue/"
        headers = {
            "Accept": "application/json",
            "Authorization": self.api_login_service.token if token is None else token
        }
        return requests.post(url, headers=headers, json=issue_request)

    """
       public Response createIssue(IssueRequest createIssueRequest, String token) {
        logger.info("sending request for create issue to server");

        RequestBody body = RequestBody.create(gson.toJson(createIssueRequest), jsonMediaType);
        Request request = new Request.Builder().url(baseUrl).addHeader("Accept", "application/json")
                .addHeader("Authorization", token).post(body).build();

        return executeMethod(request, logger);
    }
    """

    def get_issue(self, issue_key, token=None):
        logger.info("getting issue with key: " + issue_key + " from API")
        base_url = f"https://api.atlassian.com/ex/jira/93916ef5-a97b-47de-9a28-80fe8572a67e/rest/api/3/issue/{issue_key}"

        headers = {
            "Accept": "application/json",
            "Authorization": self.api_login_service.token if token is None else token
        }

        return requests.get(base_url, headers=headers)
