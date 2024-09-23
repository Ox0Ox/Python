from tkinter import *
from PIL import ImageTk, Image
import sys, os, subprocess
from tkinter import messagebox
import mysql.connector as sql
#window = Tk()


class Register:
    def __init__(self, window):
        self.window = window
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('SignUp Page')
        self.window.configure(bg="#525561")
        # ================Background Image ====================
        self.backgroundImage = ImageTk.PhotoImage(Image.open("assets\\image_1.png"))
        self.bg_image = Label(
            self.window,
            image=self.backgroundImage,
            bg="#525561"
        )
        self.bg_image.place(x=120, y=50)


        self.side_image = Image.open('images\\plane.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.bg_image, image=photo, bg='#272A37')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=175)

        # ================ Header Text Left ====================
        self.headerText_image_left = PhotoImage(file="assets\\logo.png")
        self.headerText_image_label1 = Label(
            self.bg_image,
            image=self.headerText_image_left,
            bg="#272A37"
        )
        self.headerText_image_label1.place(x=60, y=45)

        self.headerText1 = Label(
            self.bg_image,
            text="BravoAirlines",
            fg="#FFFFFF",
            font=("yu gothic ui bold", 20 * -1),
            bg="#272A37"
        )
        self.headerText1.place(x=110, y=45)




        # ================ CREATE ACCOUNT HEADER ====================
        self.createAccount_header = Label(
            self.bg_image,
            text="Create new account",
            fg="#FFFFFF",
            font=("yu gothic ui Bold", 28 * -1),
            bg="#272A37"
        )
        self.createAccount_header.place(x=375+210, y=121-76)

        # ================ ALREADY HAVE AN ACCOUNT TEXT ====================
        self.text = Label(
            self.bg_image,
            text="Already a member?",
            fg="#FFFFFF",
            font=("yu gothic ui Regular", 15 * -1),
            bg="#272A37"
        )
        self.text.place(x=375+230, y=187-76)

        # ================ GO TO LOGIN ====================
        self.switchLogin = Button(
            self.bg_image,
            text="Login",
            fg="#206DB4",
            font=("yu gothic ui Bold", 15 * -1),
            bg="#272A37",
            bd=0,
            cursor="hand2",
            activebackground="#272A37",
            activeforeground="#ffffff",
            command = self.loginner
        )
        self.switchLogin.place(x=530+230, y=185-76, width=50, height=35)

        # ================ First Name Section ====================
        self.firstName_image = PhotoImage(file="assets\\input_img.png")
        self.firstName_image_Label = Label(
            self.bg_image,
            image=self.firstName_image,
            bg="#272A37"
        )
        self.firstName_image_Label.place(x=280+230, y=242-76)

        self.firstName_text = Label(
            self.firstName_image_Label,
            text="First name",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.firstName_text.place(x=25, y=0)

        self.firstName_icon = PhotoImage(file="assets\\name_icon.png")
        self.firstName_icon_Label = Label(
            self.firstName_image_Label,
            image=self.firstName_icon,
            bg="#3D404B"
        )
        self.firstName_icon_Label.place(x=159, y=15)

        self.firstName_entry = Entry(
            self.firstName_image_Label,
            bd=0,
            fg = "#bfbfbf",
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.firstName_entry.place(x=8, y=17, width=140, height=27)


        # ================ Last Name Section ====================
        self.lastName_image = PhotoImage(file="assets\\input_img.png")
        self.lastName_image_Label = Label(
            self.bg_image,
            image=self.lastName_image,
            bg="#272A37"
        )
        self.lastName_image_Label.place(x=593+130, y=242-76)

        self.lastName_text = Label(
            self.lastName_image_Label,
            text="Last name",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.lastName_text.place(x=25, y=0)

        self.lastName_icon = PhotoImage(file="assets\\name_icon.png")
        self.lastName_icon_Label = Label(
            self.lastName_image_Label,
            image=self.lastName_icon,
            bg="#3D404B"
        )
        self.lastName_icon_Label.place(x=159, y=15)

        self.lastName_entry = Entry(
            self.lastName_image_Label,
            bd=0,
            fg = "#bfbfbf",
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.lastName_entry.place(x=8, y=17, width=140, height=27)

        # ================ Email Name Section ====================
        self.emailName_image = PhotoImage(file="assets\\email.png")
        self.emailName_image_Label = Label(
            self.bg_image,
            image=self.emailName_image,
            bg="#272A37"
        )
        self.emailName_image_Label.place(x=380+130, y=311-76)

        self.emailName_text = Label(
            self.emailName_image_Label,
            text="Email Address",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.emailName_text.place(x=25, y=0)

        self.emailName_icon = PhotoImage(file="assets\\email-icon.png")
        self.emailName_icon_Label = Label(
            self.emailName_image_Label,
            image=self.emailName_icon,
            bg="#3D404B"
        )
        self.emailName_icon_Label.place(x=370, y=15)

        self.emailName_entry = Entry(
            self.emailName_image_Label,
            bd=0,
            fg = "#bfbfbf",
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1, ),
        )
        self.emailName_entry.place(x=8, y=17, width=354, height=27)

###########################################################


        self.phone = PhotoImage(file="assets\\phone.png")
        self.phonelabel = Label(
            self.bg_image,
            image=self.phone,
            bg="#272A37"
        )
        self.phonelabel.place(x=380+130, y=311-76+67)

        self.phtext = Label(
            self.phonelabel,
            text="Mobile Number",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.phtext.place(x=25, y=0)

        self.phentry = Entry(
            self.phonelabel,
            bd=0,
            fg = "#bfbfbf",
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.phentry.place(x=8, y=17, width=354, height=27)

########################################################

        self.aadhar = PhotoImage(file="assets\\phone.png")
        self.aadharlabel = Label(
            self.bg_image,
            image=self.phone,
            bg="#272A37"
        )
        self.aadharlabel.place(x=380+130, y=311-76+67+67)

        self.aadhartxt = Label(
            self.aadharlabel,
            text="Aadhaar Number",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.aadhartxt.place(x=25, y=0)

        self.aadharentry = Entry(
            self.aadharlabel,
            bd=0,
            fg = "#bfbfbf",
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.aadharentry.place(x=8, y=17, width=354, height=27)


        # ================ Password Name Section ====================
        self.passwordName_image = PhotoImage(file="assets\\input_img.png")
        self.passwordName_image_Label = Label(
            self.bg_image,
            image=self.passwordName_image,
            bg="#272A37"
        )
        self.passwordName_image_Label.place(x=380+130, y=380-76+67+67)

        self.passwordName_text = Label(
            self.passwordName_image_Label,
            text="Password",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.passwordName_text.place(x=25, y=0)

        self.passwordName_icon = PhotoImage(file="assets\\pass-icon.png")
        self.passwordName_icon_Label = Label(
            self.passwordName_image_Label,
            image=self.passwordName_icon,
            bg="#3D404B"
        )
        self.passwordName_icon_Label.place(x=159, y=15)

        self.passwordName_entry = Entry(
            self.passwordName_image_Label,
            bd=0,
            fg = "#bfbfbf",
            bg="#3D404B",
            highlightthickness=0,
            show="*",
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.passwordName_entry.place(x=8, y=17, width=140, height=27)


        # ================ Confirm Password Name Section ====================
        self.confirm_passwordName_image = PhotoImage(file="assets\\input_img.png")
        self.confirm_passwordName_image_Label = Label(
            self.bg_image,
            image=self.confirm_passwordName_image,
            bg="#272A37"
        )
        self.confirm_passwordName_image_Label.place(x=593+130, y=380-76+67+67)

        self.confirm_passwordName_text = Label(
            self.confirm_passwordName_image_Label,
            text="Confirm Password",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.confirm_passwordName_text.place(x=25, y=0)

        self.confirm_passwordName_icon = PhotoImage(file="assets\\pass-icon.png")
        self.confirm_passwordName_icon_Label = Label(
            self.confirm_passwordName_image_Label,
            image=self.confirm_passwordName_icon,
            bg="#3D404B"
        )
        self.confirm_passwordName_icon_Label.place(x=159, y=15)

        self.confirm_passwordName_entry = Entry(
            self.confirm_passwordName_image_Label,
            bd=0,
            fg = "#bfbfbf",
            bg="#3D404B",
            highlightthickness=0,
            show="*",
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.confirm_passwordName_entry.place(x=8, y=17, width=140, height=27)

        # =============== Submit Button ====================
        self.submit_buttonImage = PhotoImage(
            file="assets\\button_1.png")
        self.submit_button = Button(
            self.bg_image,
            image=self.submit_buttonImage,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#272A37",
            cursor="hand2",
            command=self.registerer
        )
        self.submit_button .place(x=430+130, y=460-76+57+67, width=333, height=65)



        self.window.resizable(False, False)
        self.window.mainloop()
    def loginner(self):
        subprocess.Popen(['python.exe', 'LoginPage.py'])
        sys.exit()

    def registerer(self):
        # Connect to the MySQL database
        db = sql.connect(
            host="localhost",
            user="root",
            password="Root@123",
            database="BravoAirlines"
        )
        l = ['1','2','3','4','5','6','7','8','9','0']
        first_name = self.firstName_entry.get()
        if first_name == None:
            messagebox.showerror("Error","First Name not given!")
        last_name = self.lastName_entry.get()
        password = self.passwordName_entry.get()
        confirm_password = self.confirm_passwordName_entry.get()            
        aadhaar = self.aadharentry.get()
        mnumber = self.phentry.get()
        email = self.emailName_entry.get()
        #username = email
        cur = db.cursor()
        res = any(chr.isdigit() for chr in first_name)
        res1 = any(chr.isdigit() for chr in last_name)
        if len(first_name) == 0:
            messagebox.showerror("Error","First Name not given!")
        elif res == True:
            messagebox.showerror("Error","Invalid Name Format")
        elif len(last_name) == 0:
            messagebox.showerror("Error","Last Name not given!")
        elif res1 == True:
            messagebox.showerror("Error","Invalid Name Format")
        elif len(email) == 0:
            messagebox.showerror("Error","Email not given!")
        elif "@" and ".com" not in email:
            messagebox.showerror("Error","Invalid Email Format")
        elif len(mnumber) == 0:
            messagebox.showerror("Error","Phone Number not given!") 
        elif len(mnumber) > 10 or len(mnumber) < 10 or any(i not in l for i in mnumber):
            messagebox.showerror("Error", "Incorrect Phone number format")
        elif len(aadhaar) > 12 or len(aadhaar) < 12 or any(i not in l for i in aadhaar):
            messagebox.showerror("Error", "Incorrect Aadhaar number format")
        elif len(aadhaar) == 0:
            messagebox.showerror("Error","Aadhaar not given!") 
        elif len(password) == 0:
            messagebox.showerror("Error","Password not given!")
        elif password != confirm_password:
            messagebox.showerror('Error','Passwords do not match!')
        elif password == confirm_password:
            try:
                q = "INSERT INTO users VALUES ('{}','{}','{}','{}','{}','{}')".format(email, first_name, last_name, mnumber, aadhaar, confirm_password)
                cur.execute(q)
                db.commit()
                messagebox.showinfo("Success","You have been registered successfully")
                subprocess.Popen(['python.exe', 'LoginPage.py'])
                sys.exit()
            except Exception as e:
                print(e)
                messagebox.showerror("User is already registered","Please login")


def page():
    window = Tk()
    Register(window)
    window.mainloop()


if __name__ == '__main__':
    page()