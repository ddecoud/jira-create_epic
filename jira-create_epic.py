from jira import JIRA

jira_connection = JIRA(
    basic_auth=('daniela.decoud@gmail.com', 'k'),
    server="https://danidq.atlassian.net"
)
# Create a new epic with the given name and description
ticket_options = {
    'project': {'key': 'PROD'},
    'summary': 'Plan de retiro anticipado',
    'description': 'Plan de retiro anticipado',
    'issuetype': {'name': 'Epic'},
    'customfield_10011': 'Plan de retiro anticipado'
}

epic = jira_connection.create_issue(fields=ticket_options)

# Add the specified issues to the epic
jira_connection.add_issues_to_epic(epic_id=epic.id, issue_keys=["PROD-1","PROD-2","PROD-3"])
