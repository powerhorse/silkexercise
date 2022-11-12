#!/usr/bin/env python3

import time
import json
import sys

from random import randint

from interfaces.ticket.jira.jira import JIRAInterface
from interfaces.db.sqlite.sqlite import SQLiteInterface
from interfaces.db.sqlite.sqlite_consts import CREATE_TABLE, INSERT_ROW_TICKET
from interfaces.visualizer.matplotlib.matplotlib import create_bar_graph

from optparse import OptionParser

def create_tickets(jira_consts, db_path):
    jira_obj = JIRAInterface(jira_consts)
    # create random tickets in the next hour or so.
    cur_time = time.time()
    tickets_left = 100
    time_left = 3600
    while tickets_left > 0:
        delay = randint(0, time_left//tickets_left)
        print('Waiting for {} seconds before creating a ticket'.format(delay))
        time.sleep(delay)
        time_str = time.time()
        summary = ('Creating a tracker ticket at {}'.format(time_str))
        description = ('TEST ticket at {}'.format(time_str))
        issue = jira_obj.create_ticket(project_id='SIM', description=description, summary=summary)
        tickets_left -= 1
        print('Created ticket {}'.format(issue.key))
    print('All tickets created successfully')
    store_tickets(db_path, jira_obj=jira_obj)

def store_tickets(db_path, jira_consts=None, jira_obj=None):
    if jira_obj is None:
        if jira_consts is None:
            raise Exception("Cannot create a jira connection as jira object or constants are missing")
        jira_obj = JIRAInterface(jira_consts)
    sql_intf = SQLiteInterface(db_path)
    sql_intf.create_table(CREATE_TABLE)
    tickets = jira_obj.get_tickets()
    sql_intf.add_rows(INSERT_ROW_TICKET, tickets)
    print('Finished writing into the DB')
    print('Read from DB')

def delete_tickets(jira_consts):
    jira_obj = JIRAInterface(jira_consts)
    jira_obj.delete_tickets()


if __name__ == '__main__':
    optparse = OptionParser()

    config = {}
    try:
        with open('config/configuration.json', 'r') as w:
            config = json.load(w)
    except Exception as ex:
        print("Failed to read the configuration file ({})".format('config/configuration.json'))
        sys.exit(-1)

    # TODO: config type checking.
    db_path = config['database']['sqlite']['location']
    jira_consts = config['ticketing']['jira']
    optparse.add_option('-j', '--create_tickets', dest="ticket_create", help='Create tickets', action='store_true')
    optparse.add_option('-s', '--store_tickets', dest='store_tickets', help='Store tickets in database', action='store_true' )
    optparse.add_option('-p', '--publish_plot', dest='plot_publish', help='Publish a plot for this option', action='store_true')
    options, args = optparse.parse_args()
    if options.ticket_create:
        create_tickets(jira_consts)
    elif options.store_tickets:
        store_tickets(db_path, jira_consts=jira_consts)
    elif options.plot_publish:
        output_file = config['visualizer']['output']
        sql_intf = SQLiteInterface(db_path)
        create_bar_graph(sql_intf.read_all_data(), output_file)
    # delete_tickets()

    
