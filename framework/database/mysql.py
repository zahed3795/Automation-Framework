"""
Wrapper for MySQL DB functions to make life easier.
"""

import time
from framework import config as sb_config
from framework.data import settings


class DatabaseManager:
    """
    This class wraps MySQL database methods for easy use.
    """

    def __init__(self, database_env='test', conf_creds=None):
        """
        Create a connection to the MySQL DB.
        """
        import pymysql
        db_server = settings.DB_HOST
        db_port = settings.DB_PORT
        db_user = settings.DB_USERNAME
        db_pass = settings.DB_PASSWORD
        db_schema = settings.DB_SCHEMA
        retry_count = 3
        backoff = 1.2  # Time to wait (in seconds) between retries.
        count = 0
        while count < retry_count:
            try:
                self.conn = pymysql.connect(host=db_server,
                                            port=db_port,
                                            user=db_user,
                                            passwd=db_pass,
                                            db=db_schema)
                self.conn.autocommit(True)
                self.cursor = self.conn.cursor()
                return
            except Exception:
                time.sleep(backoff)
                count = count + 1
        if retry_count == 3:
            raise Exception("Unable to connect to Database after 3 retries.")

    def query_fetch_all(self, query, values):
        """
        Executes a db query, gets all the values, and closes the connection.
        """
        self.cursor.execute(query, values)
        retval = self.cursor.fetchall()
        self.__close_db()
        return retval

    def query_fetch_one(self, query, values):
        """
        Executes a db query, gets the first value, and closes the connection.
        """
        self.cursor.execute(query, values)
        retval = self.cursor.fetchone()
        self.__close_db()
        return retval

    def execute_query(self, query, values):
        """
        Executes a query to the test_db and closes the connection afterwards.
        """
        retval = self.cursor.execute(query, values)
        self.__close_db()
        return retval

    def __close_db(self):
        self.cursor.close()
        self.conn.close()
