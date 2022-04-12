# do some imports
from mysql import connector


# Add connection and cursor wrapper
class MySQLConnector:
    conn = None
    cursor = None

    def __init__(self):
        self.conn = connector.connect(
            host="localhost",
            # port="3",
            user="root",
            password="root",
            database="fb"
        )
        self.cursor = self.conn.cursor()
        #print(self.cursor)

