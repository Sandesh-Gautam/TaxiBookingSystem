import mysql.connector
import sys

def saveCustomer(fullname,address,phone,email,password,payment):
    #SQL query to insert customer information
    sql = """INSERT INTO customers (fullname,address,phone,email,password,payment) VALUES (%s, %s, %s,%s, %s,%s)"""
    #Values to be inserted
    values = (fullname,address,phone,email,password,payment)
    try:
        #Establishing connection to the database
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='yourstaxi')
        cursor = conn.cursor()
        #Execute insert query
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
    except:
        #Print error
        print("Error : ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
