import mysql.connector
from mysql.connector import Error

class RestaurantDatabase:
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
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Successfully connected to the database")
        except Error as e:
            print("Error while connecting to MySQL", e)

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")

    def addReservation(self, customer_name, contact_info, reservation_time, number_of_guests, special_requests):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.callproc('addReservation', [customer_name, contact_info, reservation_time, number_of_guests, special_requests])
                self.connection.commit()
                print("Reservation added successfully")
            cursor.close()
        except Error as e:
            print("Failed to add reservation", e)

    def getAllReservations(self):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = "SELECT * FROM Reservations"
                cursor.execute(query)
                records = cursor.fetchall()
                cursor.close()
                return records
        except Error as e:
            print("Failed to retrieve reservations", e)
            return []

    def addCustomer(self, customer_name, contact_info):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = "INSERT INTO Customers (customerName, contactInfo) VALUES (%s, %s)"
                cursor.execute(query, (customer_name, contact_info))
                self.connection.commit()
                print("Customer added successfully")
            cursor.close()
        except Error as e:
            print("Failed to add customer", e)

    def getCustomerPreferences(self, customer_id):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = "SELECT * FROM DiningPreferences WHERE customerId = %s"
                cursor.execute(query, (customer_id,))
                preferences = cursor.fetchall()
                cursor.close()
                return preferences
        except Error as e:
            print("Failed to retrieve customer preferences", e)
            return []

    def execute_stored_procedure(self, procedure_name, params):
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.callproc(procedure_name, params)
                results = []
                for result in cursor.stored_results():
                    results.append(result.fetchall())
                cursor.close()
                return results
        except Error as e:
            print(f"Failed to execute stored procedure {procedure_name}", e)
            return []
