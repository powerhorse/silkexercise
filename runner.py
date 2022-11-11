#!/usr/bin/env python3

import time

from random import randint

from interfaces.ticket.jira.jira import JIRAInterface
from interfaces.db.sqlite.sqlite import SQLiteInterface
from interfaces.db.sqlite.sqlite_consts import CREATE_TABLE, INSERT_ROW_TICKET
from interfaces.visualizer.matplotlib.matplotlib import create_bar_graph


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

def store_tickets():
    jira_obj = JIRAInterface()
    sql_intf = SQLiteInterface('test.db')
    sql_intf.create_table(CREATE_TABLE)
    tickets = jira_obj.get_tickets()
    sql_intf.add_rows(INSERT_ROW_TICKET, tickets)
    print('Finished writing into the DB')
    print('Read from DB')
    # sql_intf.read_all_data('tickets')

def delete_tickets():
    jira_obj = JIRAInterface()
    jira_obj.delete_tickets()


if __name__ == '__main__':
    #create_tickets()
    # store_tickets()
    #delete_tickets()
    sql_intf = SQLiteInterface('test.db')
    create_bar_graph(sql_intf.read_all_data(), 'test.png')
    # create_bar_graph()

    
