import mysql.connector
from mysql.connector import Error

def create_connection('cis2368spring.cdmxqnqr8wm7.us-east-1.rds.amazonaws.com', 'admin', 'cis2368spring', 'cis2368spring'):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error {e} ocurred.")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error {e} ocurred.")

def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error {e} ocurred.")
 DB_CONFIG