
# from sqlite_consts import CREATE_TABLE
import sqlite3

class SQLiteInterface(object):
    def __init__(self, data_path):
        self._connection = None
        self._cursor = None
    
    def create_connection(self, data_path):
        try:
            self._connection = sqlite3.connect(data_path)
            self._cursor = self._connection.cursor()
        except Exception as e:
            print('Failed to create a DB connection to %s' % data_path)
        return self._connection
        
    def create_table(self, sql_str):
        try:
            if self._cursor is not None:
                self._cursor.execute(sql_str)
        finally:
            self._connection.commit()
    
    def add_rows(self, add_row_sql_str, tickets):
        try:
            with self._cursor:
                for ticket in tickets:
                    self._cursor.execute(add_row_sql_str, ticket)
        finally:
            self._connection.commit()

