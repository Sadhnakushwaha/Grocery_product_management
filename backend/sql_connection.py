import mysql.connector

__cnx = None

def get_Sql_connection():
    global __cnx
    if __cnx is None:
        __cnx =  mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='grocery_store')

    return __cnx