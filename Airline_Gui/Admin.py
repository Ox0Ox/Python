import customtkinter
from customtkinter import *
import os
from PIL import Image
import sys, os, subprocess
import mysql.connector 
from tkinter import messagebox

from datetime import date
today = date.today()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Admin")
        self.geometry("1920x1020")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.logoimage = customtkinter.CTkImage(Image.open('images\\logo1.png'), size = (150 , 58))

        self.logolabel = customtkinter.CTkLabel(self.navigation_frame, text = '', image = self.logoimage,
                                                             compound="left")
        self.logolabel.grid(row = 0, column = 0, padx=10, pady=20)



        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="View Customers",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="View Flights",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Schedule Flights",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Manage Flights",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.logout = customtkinter.CTkButton(self.navigation_frame, text="Exit", command = self.loginner)
        self.logout.grid(row=6, column=0)


        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_welcome = customtkinter.CTkLabel(self.home_frame, text = 'View Customers', font=customtkinter.CTkFont(size=20), anchor="w", justify="left")
        self.home_welcome.place(x = 55, y = 30)

        self.current_label = customtkinter.CTkLabel(self.home_frame, text='Search:', font=customtkinter.CTkFont(size=17))
        self.current_label.place(x = 75, y = 90)
        self.search_cust = customtkinter.CTkEntry(self.home_frame, width=200, placeholder_text='CustomerID')
        self.search_cust.place(x = 150, y = 90)
        self.search_button = customtkinter.CTkButton(self.home_frame, text = 'Go', width=50, command = self.cust_search)
        self.search_button.place(x = 400, y = 90)


        
        '''self.home_frame_button_2 = customtkinter.CTkEntry(self.home_frame)
        self.home_frame_button_2.place(x = 150, y = 40)'''
        

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.label = customtkinter.CTkLabel(self.second_frame, text='View Flights', font=customtkinter.CTkFont(size=20))
        self.label.place(x = 55, y = 20)
        self.reloadb = customtkinter.CTkButton(self.second_frame, text = 'Reload', width = 50, command = self.reload)
        self.reloadb.place(x = 200, y = 20)
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root@123",
            database="BravoAirlines"
        )
        cur = db.cursor()
        cur.execute("SELECT * FROM domesticflights limit 0,1")
        columns = [column[0] for column in cur.description]

        # Determine the number of columns
        num_columns = len(columns)

        # Calculate the total width needed for columns
        total_width = num_columns * 110  # Adjust the multiplier as needed

        # Create the CTkScrollableFrame with the calculated width
        self.available_label = customtkinter.CTkScrollableFrame(self.second_frame, label_text='Domestic Flights', width=total_width, label_font=customtkinter.CTkFont(size=15))
        self.available_label.place(x=55, y=65)

        for col_index, col_name in enumerate(columns):
            header_label = customtkinter.CTkLabel(master=self.available_label, text=col_name, width=15)
            header_label.grid(row=0, column=col_index, padx=5, pady=5)

        cur.fetchall()
        cur.close()

        # Create a new cursor for the second query
        cur = db.cursor()

        
        cur.execute("SELECT * FROM domesticflights order by date asc")

        rows = cur.fetchall()

        
        i=0 

        for i,student in enumerate(rows, start=1): 
            for j in range(len(student)):
                e = customtkinter.CTkEntry(master = self.available_label, width=100) 
                e.grid(row=i, column=j, padx = 5, pady = 5) 
                #e.place(x=x_start + j * 105, y=y_start + i * 35)
                e.insert(customtkinter.END, student[j])
                e.configure(state = 'disabled')
            i=i+1
        cur.close()
        db.close()


        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root@123",
            database="BravoAirlines"
        )
        cur = db.cursor()
        cur.execute("SELECT * FROM InternationalFlights limit 0,1")
        columns = [column[0] for column in cur.description]

        # Determine the number of columns
        num_columns = len(columns)

        # Calculate the total width needed for columns
        total_width = num_columns * 110  # Adjust the multiplier as needed

        # Create the CTkScrollableFrame with the calculated width
        self.available_label1 = customtkinter.CTkScrollableFrame(self.second_frame, label_text='International Flights', width=total_width, label_font=customtkinter.CTkFont(size=15))
        self.available_label1.place(x=55, y=365)

        for col_index, col_name in enumerate(columns):
            header_label = customtkinter.CTkLabel(master=self.available_label1, text=col_name, width=15)
            header_label.grid(row=0, column=col_index, padx=5, pady=5)

        cur.fetchall()
        cur.close()

        # Create a new cursor for the second query
        cur = db.cursor()

        
        cur.execute("SELECT * FROM InternationalFlights order by date asc")

        rows = cur.fetchall()

        
        i=0 

        for i,student in enumerate(rows, start=1): 
            for j in range(len(student)):
                e = customtkinter.CTkEntry(master = self.available_label1, width=100) 
                e.grid(row=i, column=j, padx = 5, pady = 5) 
                #e.place(x=x_start + j * 105, y=y_start + i * 35)
                e.insert(customtkinter.END, student[j])
                e.configure(state = 'disabled')
            i=i+1
        cur.close()
        db.close()



        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.label1 = customtkinter.CTkLabel(self.third_frame, text='Schedule Flights', font=customtkinter.CTkFont(size=20))
        self.label1.place(x = 55, y = 30)
        self.search_label1 = customtkinter.CTkEntry(self.third_frame, width =175, placeholder_text='Flight ID')
        self.search_label1.place(x = 95, y = 90)
        self.search_from1 = customtkinter.CTkEntry(self.third_frame, width=175, placeholder_text='From')
        self.search_from1.place(x = 95, y = 130)
        self.search_destination1 = customtkinter.CTkEntry(self.third_frame, width=175, placeholder_text='Destination')
        self.search_destination1.place(x = 350, y = 130)
        self.search_flight1 = customtkinter.CTkEntry(self.third_frame, width=175, placeholder_text='Airline')
        self.search_flight1.place(x = 350, y = 90)
        self.price = customtkinter.CTkEntry(self.third_frame, width=175, placeholder_text='Base Price')
        self.price.place(x = 95, y = 170)
        self.date = customtkinter.CTkEntry(self.third_frame, width=175, placeholder_text='Date of flight')
        self.date.place(x = 350, y = 170)
        self.search_button1 = customtkinter.CTkButton(self.third_frame, text = 'Schedule', width=50, command = self.schedule_flights)
        self.search_button1.place(x = 275, y = 225)
        self.check_type = customtkinter.CTkCheckBox(master = self.third_frame,text = "Domestic")
        self.check_type.place(x = 95, y = 225)

        #create fourth frame

        self.airtxt = StringVar()
        self.fromtxt = StringVar()
        self.dest = StringVar()
        self.base = StringVar()
        self.datetxt = StringVar()


        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.label1 = customtkinter.CTkLabel(self.fourth_frame, text='Manage Flights', font=customtkinter.CTkFont(size=20))
        self.label1.place(x = 55, y = 30)
        self.search_label2 = customtkinter.CTkEntry(self.fourth_frame, width =175, placeholder_text='Flight ID')
        self.search_label2.place(x = 95, y = 90)
        self.search_button2 = customtkinter.CTkButton(self.fourth_frame, text = 'Go', width=50, command = self.printer)
        self.search_button2.place(x = 300, y = 90)
        
        # select default frame
        self.select_frame_by_name("home")


    def schedule_flights(self):
        try:    
            if self.check_type.get() == 1: 
                fid = self.search_label1.get()
                fro = self.search_from1.get()
                destination = self.search_destination1.get()
                airline = self.search_flight1.get()
                date = self.date.get()
                price = self.price.get()
                db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Root@123",
                database="BravoAirlines"
            )
            
                cur = db.cursor()
                s = "INSERT INTO DomesticFlights (ID,Airline,Date,BasePrice,Startpoint,Destination) values('{}','{}','{}',{},'{}','{}')".format(fid,airline,date,price,fro,destination)
                cur.execute(s)
                db.commit()
                messagebox.showinfo("Sucess!","You have scheduled the flight")
                
            
                
            elif self.check_type.get() == 0: 
                fid = self.search_label1.get()
                fro = self.search_from1.get()
                destination = self.search_destination1.get()
                airline = self.search_flight1.get()
                date = self.date.get()
                price = self.price.get()
                db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Root@123",
                database="BravoAirlines"
            )
            
                cur = db.cursor()
                s = "INSERT INTO InternationalFlights (ID,Airline,Date,BasePrice,Startpoint,Destination) values('{}','{}','{}',{},'{}','{}')".format(fid,airline,date,price,fro,destination)
                cur.execute(s)
                db.commit()
                messagebox.showinfo("Sucess!","You have scheduled the flight")

                
                    
        except:
            messagebox.showerror("Error!","Invalid, Check data values and try again")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")
    
    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def printer(self):
        

        def manage_flights():
                basepricechange = self.base_entry.get()
                datechange = self.date1.get()
                db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Root@123",
                database="BravoAirlines"
                )
                cur = db.cursor()
                s = "UPDATE `{}` SET Date = '{}' where id = '{}' ".format(ftype, datechange, fid)
                cur.execute(s)
                y = "UPDATE `{}` SET BasePrice = '{}' where id = '{}' ".format(ftype, basepricechange, fid)
                cur.execute(y)
                z = "UPDATE bookings SET Dateofflight = '{}' where flight_id = '{}' ".format(datechange, fid)
                cur.execute(z)
                messagebox.showinfo("Sucess!","You have successfully updated flight details")
                db.commit()
        
        fid = self.search_label2.get()
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@123",
        database="BravoAirlines")
        cur = db.cursor() 
        airq = "select airline from domesticflights where id = '{}' and '{}'<= date union select airline from internationalflights where id = '{}' and '{}'<= date".format(fid, today, fid, today)
        cur.execute(airq)
        air = ''
        for i in cur:
            for j in i:
                air = j
                print(type(air))
        if air != '':
            if 'I' in fid or 'i' in fid:
                ftype = 'InternationalFlights'
            elif 'D' in fid or 'd' in fid:
                ftype = 'DomesticFlights'
            fromplaceq = "select StartPoint from domesticflights where id = '{}' and '{}'<= date union select StartPoint from internationalflights where id = '{}' and '{}'<= date".format(fid, today, fid, today)
            cur.execute(fromplaceq)
            fromplace = ''
            for i in cur:
                for j in i:
                    fromplace = j

            toplaceq = "select Destination from domesticflights where id = '{}' and '{}'<= date union select destination from internationalflights where id = '{}' and '{}'<= date".format(fid, today, fid, today)
            cur.execute(toplaceq)
            toplace = ''
            for i in cur:
                for j in i:
                    toplace = j
            
            basepriceq = "select baseprice from domesticflights where id = '{}' and '{}'<= date union select baseprice from InternationalFlights where id = '{}' and '{}'<= date".format(fid, today, fid, today)
            cur.execute(basepriceq)
            baseprice = ''
            for i in cur:
                for j in i:
                    baseprice = j

            dateofflightq = "select date from domesticflights where id = '{}' and '{}'<= date union select date from internationalflights where id = '{}' and '{}'<= date".format(fid, today, fid, today)
            cur.execute(dateofflightq)
            dateofflight = ''
            for i in cur:
                for j in i:
                    dateofflight = j

            cur.close()
            db.close()
            
            self.airtxt.set('Airline:')
            self.fromtxt.set('From:')
            self.dest.set('Destination:')
            self.base.set('Base Price:')
            self.datetxt.set('Date of Flight:')
            self.airtxtval = air
            self.fromtxtval = fromplace
            self.destval = toplace
            self.baseval = baseprice
            self.datetxtval = dateofflight
            
            self.from_label = customtkinter.CTkLabel(self.fourth_frame, textvariable = self.fromtxt, font=customtkinter.CTkFont(size=17))
            self.from_label.place(x = 95, y = 210)
            self.search_from2 = customtkinter.CTkEntry(self.fourth_frame, width=175, placeholder_text=self.fromtxtval)
            self.search_from2.configure(state = 'disabled')
            self.destination_label = customtkinter.CTkLabel(self.fourth_frame, textvariable = self.dest, font=customtkinter.CTkFont(size=17))
            self.destination_label.place(x = 95, y = 250)
            self.search_destination2 = customtkinter.CTkEntry(self.fourth_frame, width=175, placeholder_text=self.destval)
            self.search_destination2.configure(state = 'disabled')
            self.airline_label = customtkinter.CTkLabel(self.fourth_frame, textvariable = self.airtxt, font=customtkinter.CTkFont(size=17))
            self.airline_label.place(x = 95, y = 170)
            self.search_flight2 = customtkinter.CTkEntry(self.fourth_frame, width=175, placeholder_text=self.airtxtval)
            self.search_flight2.configure(state = 'disabled')
            self.base_label = customtkinter.CTkLabel(self.fourth_frame, textvariable = self.base, font=customtkinter.CTkFont(size=17))
            self.base_label.place(x = 95, y = 290)
            self.base_entry = customtkinter.CTkEntry(self.fourth_frame, width=175)
            self.base_entry.insert(customtkinter.END, self.baseval)
            self.date_label = customtkinter.CTkLabel(self.fourth_frame, textvariable = self.datetxt, font=customtkinter.CTkFont(size=17))
            self.date_label.place(x = 95, y = 330)
            self.date1 = customtkinter.CTkEntry(self.fourth_frame, width=175)
            self.date1.insert(customtkinter.END, self.datetxtval)
            self.search_button2 = customtkinter.CTkButton(self.fourth_frame, text = 'Update', width=50, command = manage_flights)

            self.search_from2.place(x=250, y=210)
            self.search_destination2.place(x=250, y=250)
            self.search_flight2.place(x=250, y=170)
            self.base_entry.place(x=250, y=290)
            self.date1.place(x=250, y=330)
            self.search_button2.place(x=220, y=400)

            cur.close()
            db.close()

            
        


        else:
            messagebox.showerror('Error!', 'Wrong flight ID/ Flight Completed')


    def cust_search(self):
        s1 = self.search_cust.get()
        db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Root@123",
                database="BravoAirlines"
            )
        cur = db.cursor()

        cur.execute("SELECT email FROM users where email = '{}' limit 0,1".format(s1))
        b = ''
        for i in cur:
            for j in i:
                b = j
        cur.close()
        db.close()
        if b != '':    
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Root@123",
                database="BravoAirlines"
            )
            cur = db.cursor()

            cur.execute("SELECT email, first_name, last_name, mobile_number, aadhaar FROM users where email = '{}' limit 0,1".format(s1))
            i=0 
            
            columns = [column[0] for column in cur.description]
            


            self.desc = customtkinter.CTkLabel(self.home_frame, text='Customer:', font=customtkinter.CTkFont(size=17))
            self.desc.place(x = 60, y = 150)

            for col_index, col_name in enumerate(columns):
                header_label = customtkinter.CTkLabel(self.desc, text=col_name)
                header_label.grid(row=1, column=col_index, padx=5, pady=5)

            cur.fetchall()
            cur.close()

            # Create a new cursor for the second query
            cur = db.cursor()

            
            cur.execute("SELECT email, first_name, last_name, mobile_number, aadhaar FROM users where email = '{}' limit 0,1".format(s1))

            rows = cur.fetchall()

            
            i=0 

            for i,student in enumerate(rows, start=1): 
                print(student)
                for j in range(len(student)):
                    e = customtkinter.CTkEntry(master = self.desc, width=100) 
                    e.grid(row=i+1, column=j, padx = 5, pady = 5) 
                    e.insert(customtkinter.END, student[j])
                    e.configure(state = 'disabled')
                i=i+1

            cur.close()
            db.close()

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Root@123",
                database="bravoairlines"
            )
            cur = db.cursor()

            cur.execute("SELECT * FROM bookings limit 0,1")
            i=0 
            
            columns = [column[0] for column in cur.description]
            # Determine the number of columns
            num_columns = len(columns)

            # Calculate the total width needed for columns
            total_width = num_columns * 110  # Adjust the multiplier as needed


            self.desc1 = customtkinter.CTkScrollableFrame(self.home_frame, label_text='Customer Bookings:', label_font=customtkinter.CTkFont(size=15), width = total_width)
            self.desc1.place(x = 60, y = 325)

            for col_index, col_name in enumerate(columns):
                header_label = customtkinter.CTkLabel(self.desc1, text=col_name)
                header_label.grid(row=1, column=col_index, padx=5, pady=5)

            cur.fetchall()
            cur.close()

            # Create a new cursor for the second query
            cur = db.cursor()

            
            cur.execute("SELECT * FROM bookings where email = '{}'".format(s1))

            rows = cur.fetchall()

            
            i=0 

            for i,student in enumerate(rows, start=1): 
                print(student)
                for j in range(len(student)):
                    e = customtkinter.CTkEntry(master = self.desc1, width=100) 
                    e.grid(row=i+1, column=j, padx = 5, pady = 5) 
                    e.insert(customtkinter.END, student[j])
                    e.configure(state = 'disabled')
                i=i+1

            cur.close()
            db.close()
        else:
            messagebox.showerror("Error!","Invalid, try again")
        

    def loginner(self):
        sys.exit()

    def reload(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root@123",
            database="BravoAirlines"
        )
        cur = db.cursor()
        cur.execute("SELECT * FROM domesticflights limit 0,1")
        columns = [column[0] for column in cur.description]

        # Determine the number of columns
        num_columns = len(columns)

        # Calculate the total width needed for columns
        total_width = num_columns * 110  # Adjust the multiplier as needed

        # Create the CTkScrollableFrame with the calculated width
        self.available_label = customtkinter.CTkScrollableFrame(self.second_frame, label_text='Domestic Flights', width=total_width, label_font=customtkinter.CTkFont(size=15))
        self.available_label.place(x=55, y=65)

        for col_index, col_name in enumerate(columns):
            header_label = customtkinter.CTkLabel(master=self.available_label, text=col_name, width=15)
            header_label.grid(row=0, column=col_index, padx=5, pady=5)

        cur.fetchall()
        cur.close()

        # Create a new cursor for the second query
        cur = db.cursor()

        
        cur.execute("SELECT * FROM domesticflights")

        rows = cur.fetchall()

        
        i=0 

        for i,student in enumerate(rows, start=1): 
            for j in range(len(student)):
                e = customtkinter.CTkEntry(master = self.available_label, width=100) 
                e.grid(row=i, column=j, padx = 5, pady = 5) 
                #e.place(x=x_start + j * 105, y=y_start + i * 35)
                e.insert(customtkinter.END, student[j])
                e.configure(state = 'disabled')
            i=i+1
        cur.close()
        db.close()


        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root@123",
            database="BravoAirlines"
        )
        cur = db.cursor()
        cur.execute("SELECT * FROM InternationalFlights limit 0,1")
        columns = [column[0] for column in cur.description]

        # Determine the number of columns
        num_columns = len(columns)

        # Calculate the total width needed for columns
        total_width = num_columns * 110  # Adjust the multiplier as needed

        # Create the CTkScrollableFrame with the calculated width
        self.available_label1 = customtkinter.CTkScrollableFrame(self.second_frame, label_text='International Flights', width=total_width, label_font=customtkinter.CTkFont(size=15))
        self.available_label1.place(x=55, y=365)

        for col_index, col_name in enumerate(columns):
            header_label = customtkinter.CTkLabel(master=self.available_label1, text=col_name, width=15)
            header_label.grid(row=0, column=col_index, padx=5, pady=5)

        cur.fetchall()
        cur.close()

        # Create a new cursor for the second query
        cur = db.cursor()

        
        cur.execute("SELECT * FROM InternationalFlights ")

        rows = cur.fetchall()

        
        i=0 

        for i,student in enumerate(rows, start=1): 
            for j in range(len(student)):
                e = customtkinter.CTkEntry(master = self.available_label1, width=100) 
                e.grid(row=i, column=j, padx = 5, pady = 5) 
                #e.place(x=x_start + j * 105, y=y_start + i * 35)
                e.insert(customtkinter.END, student[j])
                e.configure(state = 'disabled')
            i=i+1
        cur.close()
        db.close()


if __name__ == "__main__":
    app = App()
    app.mainloop()