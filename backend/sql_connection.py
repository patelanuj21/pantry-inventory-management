import mysql.connector
__cnx = None

def __init__(self):
    pass


def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='pantry')
    return __cnx
