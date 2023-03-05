"""
todo -
test_get_issue() - done!
test_invalid_issue_key()
test_incorrect_authentication()
test_user_without_permission() - this has expected and actual not same - open bug


"""
import json

from src.jira_test_framework.api.api_login_service import APILoginService
from src.jira_test_framework.api.issue_service import IssueService
from src.logger import logger



def test_get_issue():
    VALID_ISSUE_KEY = "JTP-1"
    api_login_service = APILoginService()
    api_login_service.get_token_process()
    api_login_service.get_token()
    issue_service = IssueService(api_login_service)
    response = issue_service.get_issue(VALID_ISSUE_KEY)
    assert response.status_code == 200
    assert json.loads(response.content).get('key') == VALID_ISSUE_KEY
    logger.info("got issue with key: " + VALID_ISSUE_KEY)