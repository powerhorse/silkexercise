#!/usr/bin/env python3

import time

from random import randint

from interfaces.ticket.jira.jira import JIRAInterface
from interfaces.db.sqlite import SQLiteInterface
from interfaces.db.sqlite_consts import CREATE_TABLE, INSERT_ROW_TICKET

if __name__ == '__main__':
    jira_obj = JIRAInterface()
    # create random tickets in the next hour or so.
    cur_time = time.time()
    tickets_left = 6
    time_left = 3600
    while time.time() < cur_time + 3600 and tickets_left > 0:
        #delay = randint(0, time_left//tickets_left)
        time_str = time.time()
        #time.sleep(delay)
        summary = ('Creating a tracker ticket at {}'.format(time_str))
        description = ('TEST ticket at {}'.format(time_str))
        jira_obj.create_ticket(project_id='SIM', description=description, summary=summary)
        tickets_left -= 1

    
    """
    TODO
    sql_interface = SQLiteInterface()
    sql_interface.create_connection("test.db")
    sql_interface.create_table(CREATE_TABLE)
    # get tickets from jira_obj
    # write data into the table.
    """
