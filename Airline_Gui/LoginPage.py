from tkinter import *
from PIL import ImageTk, Image
import subprocess, sys, os
import mysql.connector
from tkinter import messagebox

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')
        self.window.configure(bg="#525561")

        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#272A37', width=950, height=600)
        self.lgn_frame.place(x=175, y=60)


        # ========================================================================
        self.headerText_image_left = PhotoImage(file="assets\\logo.png")
        self.headerText_image_label1 = Label(
            self.lgn_frame,
            image=self.headerText_image_left,
            bg="#272A37"
        )
        self.headerText_image_label1.place(x=60, y=45)

        self.txt = "Bravo Airlines"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 20 * -1, "bold"), bg="#272A37",
                             fg='white')
        self.heading.place(x=110, y=45, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================

        self.side_image = Image.open('images\\plane.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#272A37')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=175)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================

        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#272A37')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130-75)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================

        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#272A37", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240-75)

        # ========================================================================
        # ============================username====================================
        # ========================================================================

        self.username_label = Label(self.lgn_frame, text="Email Address", bg="#272A37", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300-75)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#272A37", fg="#bfbfbf",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=335-75, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359-75)

        # ===== Username icon =========

        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#272A37')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332-75)

        # ========================================================================
        # ============================login button================================
        # ========================================================================

        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#272A37')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450-75)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.validate_credentials)
        self.login.place(x=20, y=10)
        
        # =========== Sign Up ==================================================

        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#272A37", fg='white')
        self.sign_label.place(x=580, y=515-75)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#272A37", activebackground="#272A37", command = self.signupper)
        self.signup_button_label.place(x=700, y=510-75, width=111, height=35)

        # ========================================================================
        # ============================password====================================
        # ========================================================================

        self.password_label = Label(self.lgn_frame, text="Password", bg="#272A37", fg="white",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380-75)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#272A37", fg="#bfbfbf",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=416-75, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440-75)

        # ======== Password icon ================

        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#272A37')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414-75)

        # ========= show/hide password ==================================================================
        
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420-75)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420-75)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420-75)
        self.password_entry.config(show='*')
    

    def signupper(self):
        subprocess.Popen(['python.exe', 'RegisterPage.py'])
        sys.exit()

    def validate_credentials(self):
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root@123",
            database="BravoAirlines"
        )

        cursor = db.cursor()

        
        # Retrieve the hashed password from the database
        cursor.execute("SELECT password FROM users WHERE email = '{}'".format(username))
        
        result = cursor.fetchone()
        print(result)
        try:
            if len(result) > 0:
                stored_password = result[0]
                print(stored_password)
                
                # Hash the entered password and compare it to the stored password
                # password_hash = hashlib.sha256(password.encode()).hexdigest()
                
                if password == stored_password:
                    messagebox.showinfo("Success!", "Successfully logged in!")
                    f = open('User.txt', 'w+')
                    f.write(username)
                    subprocess.Popen(['python.exe', 'Customer.py'])
                    sys.exit()
                else:
                    messagebox.showerror("Error!", "Incorrect Username/Password")
            else:
                messagebox.showerror("Error!", "Incorrect Username/Password")
        except Exception as e:
            messagebox.showerror("Error!", "Incorrect Username/Password")


        cursor.close()
        db.close()


def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()