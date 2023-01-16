import sys
import mysql.connector

# Defining the view_alldrivers function
def view_alldrivers():
    # SQL query to select all drivers from the 'drivers' table
    sql = """SELECT * FROM drivers"""
    result = None
    try:
        # Connecting to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            database='yourstaxi'
        )
        # Creating a cursor to execute the SQL query
        cursor = conn.cursor()
        # Executing the SQL query
        cursor.execute(sql)
        # Fetching all the results from the query
        result = cursor.fetchall()
        # Closing the cursor
        cursor.close()
        # Closing the connection
        conn.close()
    except:
        # Printing the error message if there is an exception
        print("Error: ", sys.exc_info())
    finally:
        # Deleting the connection object
        del conn
        # Returning the result of the query
        return result
