import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Sample admin credentials (replace with your own)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        # Successful login, open the admin panel
        open_admin_panel()
    else:
        messagebox.showerror("Login Error", "Invalid username or password")

def open_admin_panel():
    login_frame.destroy()  # Close the login frame

    # Create the admin panel window
    def add_flight():
        # Create a new window for adding a flight
        add_flight_window = tk.Toplevel(admin_window)
        add_flight_window.title("Add Flight")

        # Create labels and entry widgets for flight information
        flight_number_label = tk.Label(add_flight_window, text="Flight Number:")
        flight_number_label.pack()
        flight_number_entry = tk.Entry(add_flight_window)
        flight_number_entry.pack()

        departure_label = tk.Label(add_flight_window, text="Departure City:")
        departure_label.pack()
        departure_entry = tk.Entry(add_flight_window)
        departure_entry.pack()

        destination_label = tk.Label(add_flight_window, text="Destination City:")
        destination_label.pack()
        destination_entry = tk.Entry(add_flight_window)
        destination_entry.pack()

        # Function to save flight information to the database
        def save_flight():
            flight_number = flight_number_entry.get()
            departure = departure_entry.get()
            destination = destination_entry.get()

            # Connect to the MySQL database
            db = mysql.connector.connect(**DB_CONFIG)
            cursor = db.cursor()

            # SQL statement to insert flight information into the database
            insert_query = "INSERT INTO flights (flight_number, departure, destination) VALUES (%s, %s, %s)"
            flight_data = (flight_number, departure, destination)

            try:
                cursor.execute(insert_query, flight_data)
                db.commit()
                messagebox.showinfo("Success", "Flight added successfully.")
                add_flight_window.destroy()  # Close the window after successful addition
            except mysql.connector.Error as err:
                db.rollback()
                messagebox.showerror("Error", f"Flight addition failed: {err}")
            finally:
                cursor.close()
                db.close()

        # Create a button to save flight information
        save_button = tk.Button(add_flight_window, text="Save", command=save_flight)
        save_button.pack()
    admin_window = tk.Tk()
    admin_window.title("Admin Panel")

    # Function to manage passengers
    def manage_passengers():
        # Connect to the MySQL database
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()

        # Retrieve passengers from the database
        cursor.execute("SELECT * FROM passengers")
        passengers = cursor.fetchall()

        # Create a window to display and manage passengers
        passengers_window = tk.Toplevel(admin_window)
        passengers_window.title("Manage Passengers")

        # Create a listbox to display passenger names
        passenger_listbox = tk.Listbox(passengers_window)
        passenger_listbox.pack()

        # Populate the listbox with passenger names
        for passenger in passengers:
            passenger_listbox.insert(tk.END, f"{passenger[1]}")  # Assuming the passenger's name is in the second column

        # Function to display passenger details
        def show_passenger_details():
            selected_passenger = passenger_listbox.get(passenger_listbox.curselection())  # Get the selected passenger name
            passenger_details_window = tk.Toplevel(passengers_window)
            passenger_details_window.title("Passenger Details")

            # Query the database for the selected passenger's details
            cursor.execute("SELECT * FROM passengers WHERE name=%s", (selected_passenger,))
            passenger_details = cursor.fetchone()

            # Display the passenger details
            details_label = tk.Label(passenger_details_window, text=f"Passenger Name: {passenger_details[1]}\n")
            details_label.pack()
            details_label = tk.Label(passenger_details_window, text=f"Passport Number: {passenger_details[2]}\n")
            details_label.pack()
            # Add more fields as needed

        # Create a button to show passenger details
        show_details_button = tk.Button(passengers_window, text="Show Details", command=show_passenger_details)
        show_details_button.pack()

        # Close the database connection
        cursor.close()
        db.close()
        passengers_window = tk.Toplevel(admin_window)
        passengers_window.title("Manage Passengers")

        # You can create a table to display passenger information here

    # Create buttons for admin tasks
    add_flight_button = tk.Button(admin_window, text="Add Flight", command=add_flight)
    add_flight_button.pack()

    manage_passengers_button = tk.Button(admin_window, text="Manage Passengers", command=manage_passengers)
    manage_passengers_button.pack()

    admin_window.mainloop()

# Create the main login window
root = tk.Tk()
root.title("Admin Login")

# Create and place labels and entry widgets for username and password
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Passwords are hidden with '*'
password_entry.pack()

# Create and place the login button
login_button = tk.Button(root, text="Login", command=check_login)
login_button.pack()

root.mainloop()
