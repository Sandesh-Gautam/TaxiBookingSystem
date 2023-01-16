import mysql.connector
import sys

def editCustomer(fullname, phone,email, password, address):
    #SQL query to update customer information
    sql = """UPDATE customers SET fullname=%s, phone=%s, password=%s, address=%s where email=%s"""
    #Values to be updated
    values = (fullname, phone, password, address, email)
    result = False
    try:
        #Establishing connection to the database
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='yourstaxi')
        cursor = conn.cursor()
        #Execute update query
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
