#!/usr/bin/env python3
"""
Author: Viswa V

Interact with JIRA as a ticketing subsystem.
"""
from jira import JIRA
from random import choice
from . import consts as consts
from datetime import datetime

class JIRAInterface(object):
    def __init__(self, email=consts.JIRA_EMAIL,
                token=consts.JIRA_TOKEN,
                server=consts.JIRA_SERVER):
        """
        The JIRA interface provides the ability to CRUD jira tickets.
        """
        options = {'server': server}
        self._connection = JIRA(options, basic_auth=(email, token))
        self._issues = []

    def get_tickets(self):
        search_str = 'project={}'.format(consts.JIRA_ID)
        issues = self._connection.search_issues(search_str)
        
        ret = []
        for issue in issues:
            dt = datetime.strptime(issue.fields.created.split('.')[0], '%Y-%m-%dT%H:%M:%S')
            ret.append([issue.key, dt])
        # TODO: Maybe yield's better?
        return ret
    
    def delete_tickets(self):
        search_str = 'project={}'.format(consts.JIRA_ID)
        issues = self._connection.search_issues(search_str)
        for issue in issues:
            issue.delete()
        
    def create_ticket(self, project_id, description, summary, ticket_type=None, priority=None, randomize=True):
        """
        This function creates a ticket using some randomness unless explicitly specified by the creator.
        """
        priority_list = ['Highest', 'High', 'Medium', 'Low' ]
        type_list = ['Bug', 'Task', 'Improvement', 'New Feature']
        if ticket_type is None:
            issue_type = choice(type_list)
        else:
            if ticket_type not in type_list:
                print('Unknown type for ticket. Assigning the default type, Story')
                issue_type = 'Story'
            else:
                issue_type = ticket_type
        if priority is None:
            issue_priority = choice(priority_list)
        else:
            if priority not in priority_list:
                print('Unknown priority for ticket. Assigning to default level of Medium')
                issue_priority = 'Medium'
            else:
                issue_priority = priority
        
        issue_dict = {
            'project': {'key': project_id},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type},
            'priority': {'name': issue_priority}}

        new_issue = self._connection.create_issue(fields=issue_dict)
        self._issues.append(new_issue)
        return new_issue