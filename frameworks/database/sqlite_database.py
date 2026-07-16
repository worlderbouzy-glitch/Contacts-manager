import sqlite3
from frameworks.config import DATABASE_NAME
from infrastructure import database

Database = database(DATABASE_NAME)


class Database:

    def __init__(self, database_name="contacts.db"):

        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts(

                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS groups(

                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT
            )
        """)

        self.connection.commit()

    def execute(self, query, parameters=()):

        self.cursor.execute(query, parameters)
        self.connection.commit()

    def fetch_one(self):

        return self.cursor.fetchone()

    def fetch_all(self):

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()