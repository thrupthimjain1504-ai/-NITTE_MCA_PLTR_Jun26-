import mysql.connector
# db file
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="thrupthi",
        database="hostel_db"
    )
