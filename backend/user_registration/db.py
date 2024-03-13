import os
import psycopg2
from flask import current_app


class DB:
    """
    :param user: DB User
    :param password: DB Password
    :param host: DB Host
    :param port: DB Port
    :param database: DB Name
    """
    def __init__(self):
        self.user = os.environ.get('DB_USER', '')
        self.password = os.environ.get('DB_PASS', '')
        self.host = os.environ.get('DB_HOST', '')
        self.port = os.environ.get('DB_PORT', '')
        self.database = os.environ.get('DB_NAME', '')
        self.conn = None
        self.cur = self.connect()

    def connect(self):
        try:
            # Connect to an existing database
            self.conn = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )

            return self.conn.cursor()

        except psycopg2.Error as err:
            current_app.logger.exception("Error Connecting to DB")
            raise err
