import mysql.connector
import sys


def saveDriver(fullname,address,email,licenseno,password):
    conn = None
    sql = """INSERT INTO drivers (fullname,address,email,licenseno,password) VALUES (%s, %s, %s,%s, %s)"""
    values = (fullname,address,email,licenseno,password)
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='yourstaxi')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values
        del sql
        del conn