import mysql.connector
import customtkinter
from datetime import datetime

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        today = datetime.today()
        self.geometry("400x250") 
        my_connect = mysql.connector.connect(
        host="localhost",
        user="root", 
        passwd="Root@123",
        database="performance_schema"
        )

        my_conn = my_connect.cursor()
        ####### end of connection ####
        my_conn.execute("SELECT * FROM error_log limit 0,1")
        i=0 
        x = ''
        for z in my_conn:
            for l in z:
                x = l
        print(x, type(x))
        my_conn.close()
        my_conn = my_connect.cursor()
        my_conn.execute("SELECT * FROM error_log limit 0,20")
        for student in my_conn: 
            for j in range(len(student)):
                e = customtkinter.CTkEntry(self, width=100) 
                e.grid(row=i, column=j) 
                e.insert(customtkinter.END, student[j])
                e.configure(state = 'disabled')
            i=i+1
        my_conn.close()
        my_connect.close()

        my_connect = mysql.connector.connect(
        host="localhost",
        user="root", 
        passwd="Root@123",
        database="performance_schema"
        )
        my_conn = my_connect.cursor()
        my_conn.execute("SELECT logged FROM error_log limit 0,20")
        datee = ''
        for i in my_conn:
            for j in i:
                datee = j

        print(today-datee)
        if (today-datee).days>100:
            print('yay')
            print(type((today-datee).days))
if __name__ == "__main__":
    app = App()
    app.mainloop()