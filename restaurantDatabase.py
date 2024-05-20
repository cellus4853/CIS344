import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(
        host = "localhost",
        port = "3306",
        database = "restaurant_reservations",
        user = "root",
        password= "m6001278#$ER34er" )
except Error as e:
    print("Error while connecting")

if (connection.is_connected()):
    cursor = connection.cursor()
    query = "select * from reservations"
    cursor.execute(query)
    reservations = cursor.fetchall()
    print(reservations)
