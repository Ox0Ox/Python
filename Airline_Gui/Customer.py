import customtkinter
import os
from PIL import Image
import sys, os, subprocess
import mysql.connector as mysql
from tkinter import messagebox
from datetime import date
import webbrowser
import time

today = date.today()

f = open('User.txt', 'r')
idc = f.read()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        

        db = mysql.connect(
            host="localhost",
            user="root",
            password="Root@123",
            database="BravoAirlines")
        cur = db.cursor() 

        
        x = "select first_name from users where email = '{}'".format(idc)

        
        name = ''
        cur.execute(x)
        for i in cur:
            for j in i:
                name = j
        
        x1 = "select last_name from users where email = '{}'".format(idc)
        cur.execute(x1)
        for i in cur:
            for j in i:
                name = name + ' ' + j

        name = str(name)
        print(type(name))
        
        #WHATEVER ELSE IS TO BE LOADED
        cur.close()
        db.close()

        self.title("BravoAirlines")
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



        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Domestic Flights",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="International Flights",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.logout = customtkinter.CTkButton(self.navigation_frame, text="Logout", command = self.loginner)
        self.logout.grid(row=6, column=0)


        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.reloadb = customtkinter.CTkButton(self.home_frame, text = 'Reload', width = 50, command = self.reload)
        self.reloadb.place(x = 475, y = 20)
        self.bookdel = customtkinter.CTkEntry(self.home_frame, placeholder_text = 'Enter BID to cancel', width = 125)
        self.bookdel.place(x = 850, y = 20)
        self.bookdelb = customtkinter.CTkButton(self.home_frame, text = 'Cancel', width = 50, command = self.delete_booking)
        self.bookdelb.place(x = 1000, y = 20)
        


        
        msg = 'Welcome ' + name
        self.home_welcome = customtkinter.CTkLabel(self.home_frame, text = msg, font=customtkinter.CTkFont(size=25, weight = 'bold'), anchor="w", justify="left")
        self.home_welcome.place(x = 50, y = 20)
        db = mysql.connect(
            host="localhost",
            user="root",
            password="Root@123",
            database="BravoAirlines"
        )
        cur = db.cursor()
        cur.execute("SELECT * FROM bookings where email = '{}' and '{}' < dateofflight limit 0,1".format(idc,today))
        columns = [column[0] for column in cur.description]

        # Determine the number of columns
        num_columns = len(columns)

        # Calculate the total width needed for columns
        total_width = num_columns * 110  # Adjust the multiplier as needed

        # Create the CTkScrollableFrame with the calculated width
        self.currentbook = customtkinter.CTkScrollableFrame(self.home_frame, label_text='Current Bookings', width=total_width, label_font=customtkinter.CTkFont(size=15))
        self.currentbook.place(x=55, y=65)

        for col_index, col_name in enumerate(columns):
            header_label = customtkinter.CTkLabel(master=self.currentbook, text=col_name, width=15)
            header_label.grid(row=0, column=col_index, padx=5, pady=5)

        cur.fetchall()
        cur.close()

        # Create a new cursor for the second query
        cur = db.cursor()

        cur.execute("SELECT * FROM bookings where email = '{}' and '{}' <= dateofflight".format(idc,today))

        rows = cur.fetchall()

        
        i=0 

        for i,student in enumerate(rows, start=1): 
            for j in range(len(student)):
                e = customtkinter.CTkEntry(master = self.currentbook, width=100) 
                e.grid(row=i, column=j, padx = 5, pady = 5) 
                #e.place(x=x_start + j * 105, y=y_start + i * 35)
                e.insert(customtkinter.END, student[j])
                e.configure(state = 'disabled')
            i=i+1
        cur.close()
        db.close()


        db = mysql.connect(
            host="localhost",
            user="root",
            password="Root@123",
            database="BravoAirlines"
        )
        cur = db.cursor()
        cur.execute("SELECT * FROM bookings where email = '{}' and '{}' > dateofflight limit 0,1".format(idc,today))
        columns = [column[0] for column in cur.description]

        # Determine the number of columns
        num_columns = len(columns)

        # Calculate the total width needed for columns
        total_width = num_columns * 110  # Adjust the multiplier as needed

        # Create the CTkScrollableFrame with the calculated width
        self.prevbook = customtkinter.CTkScrollableFrame(self.home_frame, label_text='Previous Bookings', width=total_width, label_font=customtkinter.CTkFont(size=15))
        self.prevbook.place(x=55, y=365)

        for col_index, col_name in enumerate(columns):
            header_label = customtkinter.CTkLabel(master=self.prevbook, text=col_name, width=15)
            header_label.grid(row=0, column=col_index, padx=5, pady=5)

        cur.fetchall()
        cur.close()

        # Create a new cursor for the second query
        cur = db.cursor()

        
        cur.execute("SELECT * FROM bookings where email = '{}' and '{}' > dateofflight limit 0,1".format(idc,today))

        rows = cur.fetchall()

        
        i=0 

        for i,student in enumerate(rows, start=1): 
            for j in range(len(student)):
                e = customtkinter.CTkEntry(master = self.prevbook, width=100) 
                e.grid(row=i, column=j, padx = 5, pady = 5) 
                #e.place(x=x_start + j * 105, y=y_start + i * 35)
                e.insert(customtkinter.END, student[j])
                e.configure(state = 'disabled')
            i=i+1
        cur.close()
        db.close()
        

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.label = customtkinter.CTkLabel(self.second_frame, text='Domestic Flights', font=customtkinter.CTkFont(size=17))
        self.label.place(x = 55, y = 30)
        self.search_label = customtkinter.CTkLabel(self.second_frame, text='Search:', font=customtkinter.CTkFont(size=17))
        self.search_label.place(x = 55, y = 80)
        self.search_from = customtkinter.CTkEntry(self.second_frame, width=175, placeholder_text='From')
        self.search_from.place(x = 130, y = 80)
        self.search_destination = customtkinter.CTkEntry(self.second_frame, width=175, placeholder_text='Destination')
        self.search_destination.place(x = 310, y = 80)
        self.search_button = customtkinter.CTkButton(self.second_frame, text = 'Go', width=50, command = self.bookdom)
        self.search_button.place(x = 500, y = 80)


        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.label1 = customtkinter.CTkLabel(self.third_frame, text='International Flights', font=customtkinter.CTkFont(size=17))
        self.label1.place(x = 55, y = 30)
        self.search_label1 = customtkinter.CTkLabel(self.third_frame, text='Search:', font=customtkinter.CTkFont(size=17))
        self.search_label1.place(x = 55, y = 80)
        self.search_from1 = customtkinter.CTkEntry(self.third_frame, width=175, placeholder_text='From')
        self.search_from1.place(x = 130, y = 80)
        self.search_destination1 = customtkinter.CTkEntry(self.third_frame, width=175, placeholder_text='Destination')
        self.search_destination1.place(x = 310, y = 80)
        self.search_button1 = customtkinter.CTkButton(self.third_frame, text = 'Go', width=50, command = self.bookdom1)
        self.search_button1.place(x = 500, y = 80)


        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

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

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")
    
    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def bookdom(self):
        
        def bookdomestic():
            frod = self.search_from.get()
            destinationd = self.search_destination.get()
            did = self.book_id.get()
            fcd = self.flight_class.get()
            
            try:
                db = mysql.connect(
                host="localhost",
                user="root",
                password="Root@123",
                database="BravoAirlines"
                )
                cur = db.cursor()
                cur.execute("select date from domesticflights where id = '{}'".format(did))
                dated = ''
                for i in cur:
                    for j in i:
                        dated = j

                cur.execute("select airline from DomesticFlights where id = '{}'".format(did))
                aname = ''
                for i in cur:
                    for j in i:
                        aname = j
                
                cur.execute("select {} from airline where aname = '{}'".format(fcd, aname))
                priced = 0
                for i in cur:
                    for j in i:
                        priced = j
                    
                cur.execute("select baseprice from DomesticFlights where id = '{}'".format(did))
                pricec = 0
                for i in cur:
                    for j in i:
                        pricec = j
                
                if (dated-today).days>30:
                    priced = priced+pricec
                elif (dated-today).days>15:
                    priced = priced+pricec+1000
                elif (dated-today).days>7:
                    priced = priced+pricec+2000
                else:
                    priced = priced+pricec+3000
                
                a = "INSERT INTO Bookings(flight_ID,CLASS,dateofbook,email, startpoint, destination, dateofflight, totalprice) values('{}','{}','{}','{}','{}','{}','{}', '{}')".format(did,fcd,today,idc, frod,destinationd, dated, priced)
                cur.execute(a)
                db.commit()
                cur.close()
                db.close()
                msg = 'You have successfully booked the flight! Total price = Rs.' + str(priced)
                messagebox.showinfo("Success!",msg)
                time.sleep(2)
                webbrowser.open('pay.html')
            except :
               messagebox.showerror("Error!","Please check values and try again")
            
        
        
        frod = self.search_from.get()
        destinationd = self.search_destination.get()

        db = mysql.connect(
            host="localhost",
            user="root",
            password="Root@123",
            database="Bravoairlines"
        )
        cur = db.cursor()
        cur.execute("SELECT id FROM Domesticflights where StartPoint = '{}' and destination = '{}' and '{}'<=date limit 0,1".format(frod, destinationd, today))
        chkd = ''
        for i in cur:
            for j in i:
                chkd = j
        cur.close()
        db.close()

        if chkd != '':
            self.booklabel = customtkinter.CTkLabel(self.second_frame, text =  'Book Flight:', font=customtkinter.CTkFont(size=17))
            self.booklabel.place(x = 640, y = 80)
            self.book_id = customtkinter.CTkEntry(self.second_frame, width=275, placeholder_text='Flight ID')
            self.book_id.place(x = 750, y = 80)
            self.flight_class = customtkinter.CTkEntry(self.second_frame, width=275, placeholder_text='Flight Class(Economy, Business, FirstClass)')
            self.flight_class.place(x = 750, y = 120)
            self.book_button = customtkinter.CTkButton(self.second_frame, text = 'Book', width=50, command = bookdomestic)
            self.book_button.place(x = 1040, y = 100)

            db = mysql.connect(
                host="localhost",
                user="root",
                password="Root@123",
                database="BravoAirlines"
            )
            cur = db.cursor()
            cur.execute("SELECT * FROM domesticflights where startpoint = '{}' and destination = '{}' and '{}'<=date  limit 0,1".format(frod, destinationd,today))
            columns = [column[0] for column in cur.description]
            print(columns)

            # Determine the number of columns
            num_columns = len(columns)

            # Calculate the total width needed for columns
            total_width = num_columns * 110  # Adjust the multiplier as needed

            # Create the CTkScrollableFrame with the calculated width
            self.available_label = customtkinter.CTkScrollableFrame(self.second_frame, label_text='Available Flights', width=total_width, label_font=customtkinter.CTkFont(size=15))
            self.available_label.place(x=55, y=190)

            for col_index, col_name in enumerate(columns):
                header_label = customtkinter.CTkLabel(master=self.available_label, text=col_name, width=15)
                header_label.grid(row=0, column=col_index, padx=5, pady=5)

            cur.fetchall()
            cur.close()

            # Create a new cursor for the second query
            cur = db.cursor()

            
            cur.execute("SELECT * FROM domesticflights where startpoint = '{}' and destination = '{}' and '{}'<=date order by date asc".format(frod, destinationd,today))

            rows = cur.fetchall()

            
            i=0 

            for i,student in enumerate(rows, start=1): 
                print(student)
                for j in range(len(student)):
                    e = customtkinter.CTkEntry(master = self.available_label, width=100) 
                    e.grid(row=i, column=j, padx = 5, pady = 5) 
                    #e.place(x=x_start + j * 105, y=y_start + i * 35)
                    e.insert(customtkinter.END, student[j])
                    e.configure(state = 'disabled')
                i=i+1
            cur.close()
            db.close()
        else:
            messagebox.showerror('Error', 'Check name properly / No available Flights')

    def bookdom1(self):
        
        def bookinternational():
            dii = self.book_id1.get()
            fci = self.flight_class1.get()
            froi = self.search_from1.get()
            destinationi = self.search_destination1.get()
            
            try:
                db = mysql.connect(
                host="localhost",
                user="root",
                password="Root@123",
                database="BravoAirlines")
                cur = db.cursor()
                cur.execute("select date from internationalflights where id = '{}'".format(dii))
                dated = ''
                for i in cur:
                    for j in i:
                        dated = j

                cur.execute("select airline from InternationalFlights where id = '{}'".format(dii))
                aname = ''
                for i in cur:
                    for j in i:
                        aname = j
                print(aname)
                
                cur.execute("select {} from airline where aname = '{}'".format(fci, aname))
                priced = 0
                for i in cur:
                    for j in i:
                        priced = j
                    
                cur.execute("select baseprice from internationalflights where id = '{}'".format(dii))
                pricec = 0
                for i in cur:
                    for j in i:
                        pricec = j
                print(type(pricec),'baseprice')
                
                if (dated-today).days>30:
                    priced = priced+pricec
                elif (dated-today).days>15:
                    priced = priced+pricec+1000
                elif (dated-today).days>7:
                    print(type(priced+pricec))
                    priced = priced+pricec+2000
                else:
                    priced = priced+pricec+3000

                
                a = "INSERT INTO Bookings(flight_ID,CLASS,dateofbook,email, startpoint, destination, dateofflight, totalprice) values('{}','{}','{}','{}','{}','{}','{}', '{}')".format(dii,fci,today,idc, froi,destinationi, dated, priced)
                cur.execute(a)
                db.commit()
                cur.close()
                db.close()
                msg = 'You have successfully booked the flight! Total price = Rs.' + str(priced)
                messagebox.showinfo("Success!",msg)
                time.sleep(2)
                webbrowser.open('pay.html')
            except :
               messagebox.showerror("Error!","Please check values and try again")


        froi = self.search_from1.get()
        destinationi = self.search_destination1.get()

        db = mysql.connect(
            host="localhost",
            user="root",
            password="Root@123",
            database="Bravoairlines"
        )
        cur = db.cursor()
        cur.execute("SELECT id FROM Internationalflights where StartPoint = '{}' and destination = '{}' and '{}'<=date limit 0,1".format(froi, destinationi,today))
        chki = ''
        for i in cur:
            for j in i:
                chki = j
        cur.close()
        db.close()
        if chki != '':
            self.booklabel1 = customtkinter.CTkLabel(self.third_frame, text =  'Book Flight:', font=customtkinter.CTkFont(size=17))
            self.booklabel1.place(x = 640, y = 80)
            self.book_id1 = customtkinter.CTkEntry(self.third_frame, width=275, placeholder_text='Flight ID')
            self.book_id1.place(x = 750, y = 80)
            self.flight_class1 = customtkinter.CTkEntry(self.third_frame, width=275, placeholder_text='Flight Class(Economy, Business, FirstClass)')
            self.flight_class1.place(x = 750, y = 120)
            self.book_button = customtkinter.CTkButton(self.third_frame, text = 'Book', width=50, command = bookinternational)
            self.book_button.place(x = 1040, y = 100)


            db = mysql.connect(
                host="localhost",
                user="root",
                password="Root@123",
                database="Bravoairlines"
            )
            cur = db.cursor()
            cur.execute("SELECT * FROM Internationalflights where StartPoint = '{}' and destination = '{}' and '{}'<=date limit 0,1".format(froi, destinationi,today))
            columns = [column[0] for column in cur.description]
            print(columns)

            # Determine the number of columns
            num_columns = len(columns)

            # Calculate the total width needed for columns
            total_width = num_columns * 110  # Adjust the multiplier as needed

            # Create the CTkScrollableFrame with the calculated width
            self.available_label1 = customtkinter.CTkScrollableFrame(self.third_frame, label_text='Available Flights', width=total_width, label_font=customtkinter.CTkFont(size=15))
            self.available_label1.place(x=55, y=190)

            for col_index, col_name in enumerate(columns):
                header_label = customtkinter.CTkLabel(master=self.available_label1, text=col_name, width=15)
                header_label.grid(row=0, column=col_index, padx=5, pady=5)

            cur.fetchall()
            cur.close()

            # Create a new cursor for the second query
            cur = db.cursor()

            
            cur.execute("SELECT * FROM internationalflights where StartPoint = '{}' and Destination = '{}' and '{}'<=date order by date asc".format(froi, destinationi,today))

            rows = cur.fetchall()

            
            i=0 

            for i,student in enumerate(rows, start=1): 
                print(student)
                for j in range(len(student)):
                    e = customtkinter.CTkEntry(master = self.available_label1, width=100) 
                    e.grid(row=i, column=j, padx = 5, pady = 5) 
                    #e.place(x=x_start + j * 105, y=y_start + i * 35)
                    e.insert(customtkinter.END, student[j])
                    e.configure(state = 'disabled')
                i=i+1

            cur.close()
            db.close()
        else:
            messagebox.showerror('Error','Check name / No available flights')


    def loginner(self):
        subprocess.Popen(['python.exe', 'LoginPage.py'])
        sys.exit()

    def delete_booking(self):
        todelete = self.bookdel.get()
        db = mysql.connect(
        host="localhost",
        user="root",
        password="Root@123",
        database="BravoAirlines"
        )
        cur = db.cursor()
        s = "DELETE FROM Bookings WHERE BID = {} and email = '{}' and '{}'<=dateofflight".format(todelete,idc,today)
        z = "Select * FROM Bookings WHERE BID = '%s' and email = '%s' and '%s'<=dateofflight"%(todelete,idc,today)
        cur.execute(z)
        chking = ''
        for i in cur:
            for j in i:
                chking = j
        try:    
            if chking != '':
                cur.execute(s)
                db.commit()
                cur.close()
                db.close()
                messagebox.showinfo("Success!", "You have cancelled the flight, Amount will be refunded shortly \nRefund Amount is subject to variation")
            else:
                messagebox.showerror("Error!", "Check Values and try again")
        except:
            messagebox.showerror("Error!", "Check Values and try again")

    def reload(self):
        db = mysql.connect(
            host="localhost",
            user="root",
            password="Root@123",
            database="BravoAirlines"
        )
        cur = db.cursor()
        cur.execute("SELECT * FROM bookings where email = '{}' and '{}' < dateofflight limit 0,1".format(idc,today))
        columns = [column[0] for column in cur.description]

        # Determine the number of columns
        num_columns = len(columns)

        # Calculate the total width needed for columns
        total_width = num_columns * 110  # Adjust the multiplier as needed

        # Create the CTkScrollableFrame with the calculated width
        self.currentbook = customtkinter.CTkScrollableFrame(self.home_frame, label_text='Current Bookings', width=total_width, label_font=customtkinter.CTkFont(size=15))
        self.currentbook.place(x=55, y=65)

        for col_index, col_name in enumerate(columns):
            header_label = customtkinter.CTkLabel(master=self.currentbook, text=col_name, width=15)
            header_label.grid(row=0, column=col_index, padx=5, pady=5)

        cur.fetchall()
        cur.close()

        # Create a new cursor for the second query
        cur = db.cursor()

        cur.execute("SELECT * FROM bookings where email = '{}' and '{}' <= dateofflight".format(idc,today))

        rows = cur.fetchall()

        
        i=0 

        for i,student in enumerate(rows, start=1): 
            for j in range(len(student)):
                e = customtkinter.CTkEntry(master = self.currentbook, width=100) 
                e.grid(row=i, column=j, padx = 5, pady = 5) 
                #e.place(x=x_start + j * 105, y=y_start + i * 35)
                e.insert(customtkinter.END, student[j])
                e.configure(state = 'disabled')
            i=i+1
        cur.close()
        db.close()


        db = mysql.connect(
            host="localhost",
            user="root",
            password="Root@123",
            database="BravoAirlines"
        )
        cur = db.cursor()
        cur.execute("SELECT * FROM bookings where email = '{}' and '{}' > dateofflight limit 0,1".format(idc,today))
        columns = [column[0] for column in cur.description]

        # Determine the number of columns
        num_columns = len(columns)

        # Calculate the total width needed for columns
        total_width = num_columns * 110  # Adjust the multiplier as needed

        # Create the CTkScrollableFrame with the calculated width
        self.prevbook = customtkinter.CTkScrollableFrame(self.home_frame, label_text='Previous Bookings', width=total_width, label_font=customtkinter.CTkFont(size=15))
        self.prevbook.place(x=55, y=365)

        for col_index, col_name in enumerate(columns):
            header_label = customtkinter.CTkLabel(master=self.prevbook, text=col_name, width=15)
            header_label.grid(row=0, column=col_index, padx=5, pady=5)

        cur.fetchall()
        cur.close()

        # Create a new cursor for the second query
        cur = db.cursor()

        
        cur.execute("SELECT * FROM bookings where email = '{}' and '{}' > dateofflight limit 0,1".format(idc,today))

        rows = cur.fetchall()

        
        i=0 

        for i,student in enumerate(rows, start=1): 
            for j in range(len(student)):
                e = customtkinter.CTkEntry(master = self.prevbook, width=100) 
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