import sys
from loginconnect import connect
from loginsettersgetters import LoginSetGet


def search_customer(email, password):
    sql = """SELECT * FROM customers WHERE email = %s and password = %s"""
    values = (email,password)
    result = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error: ", sys.exc_info())
    finally:
        del conn
        del values
        return result
def search_driver(email, password):
    sql = """SELECT * FROM drivers WHERE email = %s and password = %s"""
    values = (email,password)
    result = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error: ", sys.exc_info())
    finally:
        del conn
        del values
        return result

def search_admin(email, password):
    sql = """SELECT * FROM admin WHERE email = %s and password = %s"""
    values = (email,password)
    result = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error: ", sys.exc_info())
    finally:
        del conn
        del values
        return result
