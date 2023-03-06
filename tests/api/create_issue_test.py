"""
 private static String createdIssueKey = null;

    @Test
    public static void createIssue() {
        apiService.login();


        IssueRequest createIssueRequest = new IssueRequest();
        APIUtils.insertValuesForIssueRequest(createIssueRequest, true);

        Response response = issueService.createIssue(createIssueRequest);
        Assert.assertEquals(response.code(), 201);
        CreateIssueResponse createIssueResponse = responseToObject(response, CreateIssueResponse.class);
        createdIssueKey = createIssueResponse.getKey();
        logger.info("Issue created with key: " + createdIssueKey);

        response = issueService.getIssue(createdIssueKey);
        Assert.assertEquals(response.code(), 200);
        GetIssueResponse getIssueResponse = responseToObject(response, GetIssueResponse.class);
        Assert.assertEquals(getIssueResponse.getKey(), createdIssueKey);
        logger.info("issue with key: " + createdIssueKey + " got successfully from server");
    }
"""
import json

from src.jira_test_framework.api.api_login_service import APILoginService
from src.logger import logger
from tests.api.api_utils import valid_login
from tests.api.constants import *

createdIssueKey = None
api_login_service = APILoginService()


def test_create_issue():
    issue_service = valid_login(api_login_service)
    create_issue_request = insert_values_for_issue_request(True)
    response = issue_service.create_issue_issue(create_issue_request)
    assert response.status_code == 201
    created_issue_key = json.loads(response.content).get('key')
    logger.info("Issue created with key: " + created_issue_key)

    response = issue_service.get_issue(created_issue_key)
    assert response.status_code == 200
    assert json.loads(response.content).get('key') == created_issue_key
    logger.info("issue with key: " + created_issue_key + " got successfully from server")


    """
    
    valid_issue_type - use for 2 different tests
    """
def insert_values_for_issue_request(valid_issue_type, summary=SUMMARY):
    issue_request = {}
    fields = {}
    fields["summary"] = summary

    if valid_issue_type:
        fields["issuetype"] = {"id": ISSUE_TYPE}
    else:
        fields["issuetype"] = {"id": "10070"}

    fields["project"] = {"id": PROJECT_ID}
    fields["customfield_10020"] = CUSTOM_FIELD_10020_ID
    fields["reporter"] = {"accountId": REPORTER_ID}
    fields["labels"] = LABELS
    fields["assignee"] = {"accountId": ASSIGNEE_ID}

    description = {}
    description["type"] = DESCRIPTION_TYPE
    description["version"] = DESCRIPTION_VERSION

    content = []
    content.append({"type": DESCRIPTION_CONTENT_TYPE})

    contents__1 = []
    contents__1.append({"text": DESCRIPTION_CONTENT__1_TEXT, "type": DESCRIPTION_CONTENT__1_TYPE})

    content[0]["content"] = contents__1

    description["content"] = content
    fields["description"] = description

    issue_request["fields"] = fields
    return issue_request

