from distutils.command.config import config
import mysql.connector
from backend import app
__cnx = None

def __init__(self):
    pass


def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user=app.config['DB_USER'], password=app.config['DB_PASSWORD'], host=app.config['DB_HOST'], database=app.config['DB_NAME'])
    return __cnx
