import json

from src.jira_test_framework.api.api_login_service import APILoginService
from src.jira_test_framework.api.issue_service import IssueService
from src.logger import logger
from tests.api.api_utils import valid_login
from tests.api.constants import *

api_login_service = APILoginService()


def test_get_issue():
    issue_service = valid_login(api_login_service)

    response = issue_service.get_issue(VALID_ISSUE_KEY)
    assert response.status_code == 200
    assert json.loads(response.content).get('key') == VALID_ISSUE_KEY
    logger.info("got issue with key: " + VALID_ISSUE_KEY)


def test_invalid_issue_key():
    issue_service = valid_login(api_login_service)

    response = issue_service.get_issue(INVALID_ISSUE_KEY)
    assert response.status_code == 404

    logger.info("error in get-issue with invalid key: " + INVALID_ISSUE_KEY)


def test_incorrect_authentication():
    issue_service = IssueService(api_login_service)

    response = issue_service.get_issue("JTP-1", INVALID_TOKEN)
    assert response.status_code == 401
    logger.info("authentication credentials are incorrect or missing")


def test_user_without_permission():
    """
    this has expected [404] and actual [403] not same - open bug
    """
    issue_service = IssueService(api_login_service)

    api_login_service.get_token_process("read:me")

    response = issue_service.get_issue(VALID_ISSUE_KEY)
    assert response.status_code == 404
    logger.info("the user does not have permission to view it")
