"""
todo -
test_get_issue()
test_invalid_issue_key()
test_incorrect_authentication()
test_user_without_permission() - this has expected and actual not same - open bug


"""
from src.jira_test_framework.api.api_login_service import APILoginService

"""
    from JAVA
    @Test
    public static void getIssue() {
        apiService.login();
        Response response = issueService.getIssue(validIssueKey);
        Assert.assertEquals(response.code(), 200);
        GetIssueResponse getIssueResponse = responseToObject(response, GetIssueResponse.class);
        Assert.assertEquals(validIssueKey, getIssueResponse.getKey());
        logger.info("got issue with id: " + validIssueKey);
    }
"""

def test_get_issue():
    api_service = APILoginService()
    api_service.get_token_process()
    api_service.get_token()