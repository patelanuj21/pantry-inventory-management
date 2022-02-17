from distutils.command.config import config
import mysql.connector
from mysql.connector import errorcode
from backend import app
__cnx = None

def __init__(self):
    pass


def get_sql_connection():
    global __cnx
    if __cnx is None:
        try:
            __cnx = mysql.connector.connect(user=app.config['DB_USER'], password=app.config['DB_PASSWORD'], host=app.config['DB_HOST'], database=app.config['DB_NAME'])

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            _cnx.close()
    return __cnx
