import mysql.connector
import sys


def editDriver(fullname, licenseno,email, password, address):
    sql = """UPDATE drivers SET fullname=%s, licenseno=%s, password=%s, address=%s where email=%s"""
    values = (fullname,licenseno, password, address, email)
    result = False
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='yourstaxi')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result=True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql, conn
        return result