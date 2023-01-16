import mysql.connector
import sys


def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root',password='', database='yourstaxi')
    except:
        print("Error: ", sys.exc_info())
    finally:
       return conn

def makeBooking(pick_up,drop_off,date, time,cid):
    conn = None
    sql = """INSERT INTO trips (pick_up,drop_off,date, time,status,cid) VALUES (%s, %s, %s,%s,"pending",%s)"""
    values = (pick_up,drop_off,date, time,cid)
    try:
        conn = connect()
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





