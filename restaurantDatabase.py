import mysql.connector
from mysql.connector import Error

class RestaurantDatabase():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="restaurant_reservations",
                 user='root',
                 password='m6001278#$ER34er'):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password)
            
            if self.connection.is_connected():
                print("Successfully connected to the database")
                return
        except Error as e:
            print("Error while connecting to MySQL", e)

    def addReservation(self, customer_id, reservation_time, number_of_guests, special_requests):
        try:
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                query = "INSERT INTO reservations (customer_id, reservation_time, number_of_guests, special_requests) VALUES (%s, %s, %s, %s)"
                self.cursor.execute(query, (customer_id, reservation_time, number_of_guests, special_requests))
                self.connection.commit()
                print("Reservation added successfully")
        except Error as e:
            print("Failed to add reservation", e)

    def getAllReservations(self):
        try:
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                query = "SELECT * FROM reservations"
                self.cursor.execute(query)
                records = self.cursor.fetchall()
                return records
        except Error as e:
            print("Failed to retrieve reservations", e)
            return []

    def addCustomer(self, customer_name, contact_info):
        try:
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                query = "INSERT INTO customers (customer_name, contact_info) VALUES (%s, %s)"
                self.cursor.execute(query, (customer_name, contact_info))
                self.connection.commit()
                print("Customer added successfully")
        except Error as e:
            print("Failed to add customer", e)

    def getCustomerPreferences(self, customer_id):
        try:
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                query = "SELECT * FROM diningPreferences WHERE customerId = %s"
                self.cursor.execute(query, (customer_id,))
                preferences = self.cursor.fetchall()
                return preferences
        except Error as e:
            print("Failed to retrieve customer preferences", e)
            return []
   
