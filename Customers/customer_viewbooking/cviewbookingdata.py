# import sys and mysql connector
import sys
import mysql.connector

# function to view bookings for a specific customer
def view_booking(cid):
    # SQL statement to select all trips where the customer id matches the input cid
    sql = """SELECT * FROM trips where cid = %s"""
    result = None
    # values for the SQL statement
    values = (cid,)
    try:
        # connect to the database
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='yourstaxi'
        )
        # create cursor
        cursor = conn.cursor()
        # execute SQL statement
        cursor.execute(sql,values)
        # fetch results
        result = cursor.fetchall()
        # close cursor and connection
        cursor.close()
        conn.close()
    except:
        # print error message if there is an exception
        print("Error: ", sys.exc_info())
    finally:
        del conn
        # return the result
        return result

# function to view all bookings
def view_booking1():
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


# function to update bookings
def update_booking(pick_up,drop_off,date,time,tid):
    # SQL statement to update the trips table where the tid matches the input tid
    sql = """UPDATE trips SET pick_up= %s, drop_off = %s, date = %s, time = %s WHERE tid = %s"""
    values = (pick_up,drop_off,date,time,tid)

    result = False
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='yourstaxi'
        )
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error: ", sys.exc_info())
    finally:
        del conn
        del values
        return result

def delete_booking(tid):
    sql = """DELETE FROM trips WHERE tid =%s"""
    values = tid
    result = False
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='yourstaxi'
        )
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        result = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error: ", sys.exc_info())
    finally:
        del conn
        return result