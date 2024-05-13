create database restaurant_reservations;

create table Customers (
	customerID int not null unique auto_increment primary key,
    customerName varchar(50) not null,
    contactInfo varchar(150),
    storeEmail varchar(50)
);

create table Reservations (
	reservationID int not null unique auto_increment primary key,
    customerID int not null,
    reservationTime datetime not null,
    numberOfGuests int not null,
    specialRequests varchar(150),
    foreign key(customerID) references Customers(customerID)
);

create table DiningPreferences (	
	preferenceID int not null unique auto_increment primary key,
    customerID int not null,
    favoriteTable varchar(50),
    dietaryRestrictions varchar(150),
    foreign key(customerID) references Customers(customerID)
);

DELIMITER //
CREATE PROCEDURE findReservations(IN customer_ID INT)
BEGIN
    SELECT * FROM Reservations WHERE customerID = customer_ID;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE addSpecialRequest(IN reservation_ID INT, IN requests_cell VARCHAR(150))
BEGIN
    UPDATE Reservations SET specialRequests = requests_cell WHERE reservationID = reservation_ID;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE addReservation(
    IN customerName_cell VARCHAR(50),
    IN contactInfo_cell VARCHAR(150),
    IN reservationTime_cell DATETIME,
    IN numberOfGuests_cell INT,
    IN specialRequests_cell VARCHAR(150)
)
BEGIN
    DECLARE customerID_milt INT;
    
    SELECT customerID INTO customerID_milt FROM Customers WHERE customerName = customerName_cell AND contactInfo = contactInfo_cell;
    
    IF customerID_milt IS NULL THEN
        INSERT INTO Customers (customerName, contactInfo) VALUES (customerName_cell, contactInfo_cell);
        SET customerID_milt = LAST_INSERT_ID();
    END IF;
		INSERT INTO Reservations (customerID, reservationTime, numberOfGuests, specialRequests)
		VALUES (customerID_milt, reservationTime_cell, numberOfGuests_cell, specialRequests_cell);
    
END //
DELIMITER ;

INSERT INTO Customers (customerName, contactInfo) VALUES
("Julynn Pelius", "jilton@cmail.com"),
("John Pelius", "johnboy@cmail.com"),
("Jessiana Pelius", "Jessie@cmail.com");

INSERT INTO Reservations (customerID, reservationTime, numberOfGuests, specialRequests) VALUES
(0001, "2024-05-11 14:00:00", 6, "Window seat preferred"),
(0002, "2024-05-12 15:00:00", 12, NULL),
(0003, "2024-05-13 16:00:00", 9, "Meat options requested");

INSERT INTO DiningPreferences (customerID, favoriteTable, dietaryRestrictions) VALUES
(0001, "Table 2", "None"),
(0002, "Table 1", "Gluten-free"),
(0003, "Table 3", "Vegan");



