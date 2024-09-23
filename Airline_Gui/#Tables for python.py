#Tables for python
import mysql.connector

con = mysql.connector.connect(user = "root", password = "Root@123", host = "localhost")
cur = con.cursor()

#cur.execute("create database BravoAirlines")

cur.execute("Use BravoAirlines")

#creating tables in the database
#cur.execute('CREATE TABLE Airline (aname VARCHAR(225) PRIMARY KEY, Economy INT, Business INT, FirstClass INT)')
#cur.execute('CREATE TABLE DomesticFlights (ID VARCHAR(225) PRIMARY KEY,Airline VARCHAR(225), foreign key(airline) references airline(aname), Date DATE,BasePrice INT, StartPoint VARCHAR(225), Destination VARCHAR(225))')
#cur.execute('CREATE TABLE InternationalFlights (ID VARCHAR(225) PRIMARY KEY,Airline VARCHAR(225), foreign key(airline) references airline(aname), Date DATE, BasePrice INT, StartPoint VARCHAR(225), Destination VARCHAR(225))')
cur.execute('CREATE TABLE Bookings (BID int not null auto_increment primary key, Email VARCHAR(225),Flight_ID VARCHAR(255), Class VARCHAR(225), StartPoint VARCHAR(225), Destination VARCHAR(225) ,DateOfBook date ,DateOfFlight date, TotalPrice int)')

#cur.execute('CREATE TABLE Users (Email VARCHAR(225) PRIMARY KEY,First_Name VARCHAR(225),Last_Name VARCHAR(225), Mobile_Number VARCHAR(225), Aadhaar VARCHAR(225), Password VARCHAR(225))')
#cur.execute("update Internationalflights set Airline = 'CocoAirlines' where id = 'I1'")
#cur.execute('delete from internationalflights where id = "I1"')
con.commit()