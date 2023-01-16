import sys
import mysql.connector


def view_booking():
    sql = """SELECT * FROM trips"""
    result = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='yourstaxi'
        )
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error: ", sys.exc_info())
    finally:
        del conn
        return result