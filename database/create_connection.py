import pyodbc
from confidential.secret_file import *


class EstablishConnection:
    server = server
    database = database
    username = username
    password = password

    def database_oop(self):
        connections = ('DRIVER={ODBC Driver 17 for SQL Server};'
                       'SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        try:
            with pyodbc.connect(connections, timeout=5) as connection:
                print("Connection Successful")
        except (ConnectionError, pyodbc.OperationalError, pyodbc.DatabaseError):
            print("Connection Timed Out, retrying...")
            self.establish_connection()
        except pyodbc.InterfaceError:
            print("Invalid connection to DB interface, retrying...")
            self.establish_connection()
        else:
            cursor = connection.cursor()
            return cursor


