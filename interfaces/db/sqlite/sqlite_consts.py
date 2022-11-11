CREATE_TABLE = """  CREATE TABLE IF NOT EXISTS tickets (
                    ticket_id VARCHAR(255) PRIMARY KEY,
                    time integer NOT NULL); """
INSERT_ROW_TICKET = """ INSERT OR IGNORE INTO tickets(ticket_id, time)
                        VALUES(?,?)
                    """
READ_TIME = """ SELECT time from tickets
            """