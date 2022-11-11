
# from sqlite_consts import CREATE_TABLE
import sqlite3

class SQLiteInterface(object):
    def __init__(self, data_path):
        try:
            self._connection = sqlite3.connect(data_path)
            self._cursor = self._connection.cursor()
        except Exception as e:
            print('Failed to create a DB connection to %s' % data_path)
    
    def create_table(self, sql_str):
        if self._connection is None or self._cursor is None:
            raise Exception('Cannot make connection to the underlying DB')
        try:
            if self._cursor is not None:
                print(sql_str)
                self._cursor.execute(sql_str)
        finally:
            self._connection.commit()
    
    def add_rows(self, add_row_sql_str, tickets):
        try:
            for ticket in tickets:
                self._cursor.execute(add_row_sql_str, ticket)
        finally:
            self._connection.commit()

    def read_all_data(self, table_name):
        try:
            self._cursor.execute('SELECT * from {}'.format(table_name))
            rows = self._cursor.fetchall()
            for row in rows:
                print(row)
        except Exception as ex:
            print('Exception occurred: %s' % str(ex))
