#!/usr/bin/env python3

import time

from random import randint

from interfaces.ticket.jira.jira import JIRAInterface
from interfaces.db.sqlite import SQLiteInterface
from interfaces.db.sqlite_consts import CREATE_TABLE, INSERT_ROW_TICKET


def create_tickets():
    jira_obj = JIRAInterface()
    # create random tickets in the next hour or so.
    cur_time = time.time()
    tickets_left = 100
    time_left = 3600
    while tickets_left > 0:
        delay = randint(0, time_left//tickets_left)
        time_str = time.time()
        print('Waiting for {} seconds before creating a ticket'.format(delay))
        time.sleep(delay)
        summary = ('Creating a tracker ticket at {}'.format(time_str))
        description = ('TEST ticket at {}'.format(time_str))
        issue = jira_obj.create_ticket(project_id='SIM', description=description, summary=summary)
        tickets_left -= 1
        print('Created ticket {}'.format(issue.key))
    print('All tickets created successfully')

def get_tickets():
    jira_obj = JIRAInterface()
    jira_obj.get_tickets()

def delete_tickets():
    jira_obj = JIRAInterface()
    jira_obj.delete_tickets()

if __name__ == '__main__':
    create_tickets()
    get_tickets()
    # delete_tickets()
    
    #sql_interface = SQLiteInterface()
    #sql_interface.create_connection("test.db")
    #sql_interface.create_table(CREATE_TABLE)
    # get tickets from jira_obj
    # write data into the table.
