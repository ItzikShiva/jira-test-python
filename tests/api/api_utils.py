from src.jira_test_framework.api.issue_service import IssueService


def valid_login(api_login_service):
    api_login_service.get_token_process()
    return IssueService(api_login_service)