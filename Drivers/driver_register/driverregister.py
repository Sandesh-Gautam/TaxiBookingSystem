import tkinter
from tkinter import *
from tkinter import messagebox
from Drivers.driver_register.dregisterdata import saveDriver
from PIL import Image,ImageTk
import mysql.connector
import re

class Drivregister1():
    def __init__(self):
        def save():
            # get the entered information from the entry fields
            name = txtName.get()
            address = txtAddress.get()
            email = txtEmail.get()
            licenseno = txtLicenseno.get()
            password = txtPassword.get()
            # create a connection to the database
            conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='',
                                           database='yourstaxi')
            cursor = conn.cursor()
            # check if the email already exists in the database
            cursor.execute("SELECT * FROM drivers WHERE email=%s", (email,))
            results = cursor.fetchall()

            # check if any fields are empty
            if not name or not email or not password or not address or not licenseno:
                messagebox.showerror("Invalid", "All fields are required")
            # check if the email is in the correct format
            elif not re.match(r"[^@]+@[^@]+.[^@]+", email):
                messagebox.showerror("Invalid", "Invalid email address")
            # check if the license number is at least 8 characters long
            elif len(licenseno) < 8:
                messagebox.showerror("Invalid", "License no  must be at least 8 characters")
            # check if the password is at least 8 characters long
            elif len(password) < 8:
                messagebox.showerror("Invalid", "Password must be at least 8 characters")
            # check if the email already exists in the database
            elif results:
                messagebox.showerror("Invalid", "Email already exists")
            else:
                # call the saveDriver function with the entered information
                saveDriver(name, address,  email,licenseno, password)
                messagebox.showinfo("Title", "User Registered")
                root.destroy()

        # create the main window
        root = Toplevel()
        root.title("Driver Registration")
        root.geometry("1700x1070")
        root.resizable(False,False)

        # open and display the background image
        img = Image.open('taxipng.png')
        bg = ImageTk.PhotoImage(img)

        label = Label(root, image=bg)
        label.place(x=0, y=0)

        # create a canvas to hold the form
        d = Canvas(root, height=500, width=1050, bg="grey")
        d.pack(padx=700, pady=280)
        d.pack()
        # create a label
        lblApp = Label(root, text="Yourstaxi", font=("Snell", 60), background="black", foreground="White")
        lblApp.place(x=1290, y=50)
        # create labels for the form

        lblName = Label(root, text="Full name: ",background="grey")
        lblLicenseno = Label(root, text="License no: ",background="grey")
        lblEmail = Label(root, text="Email: ", background="grey")
        lblAddress = Label(root,text="Address: ",background="grey")
        lblPassword = Label(root, text="Password: ",background="grey")

        txtName = Entry(root,width=20)
        txtLicenseno = Entry(root,width=20)
        txtEmail = Entry(root, width=20)
        txtAddress = Entry(root,width=20)
        txtPassword = Entry(root, width=20,show="*")

        btnSave = Button(root, text="Register",background="#ff9999",command=save)
        btnClose = Button(root, text="Close",background="#ff9999",command=exit)

        lblName.place(x=725, y=300)
        txtName.place(x=825, y=300)

        lblAddress.place(x=725, y=350)
        txtAddress.place(x=825, y=350)

        lblLicenseno.place(x=725, y=400)
        txtLicenseno.place(x=825, y=400)

        lblEmail.place(x=725, y=450)
        txtEmail.place(x=825, y=450)

        lblPassword.place(x=725, y=500)
        txtPassword.place(x=825, y=500)

        btnSave.place(x=755, y=600)
        btnClose.place(x=910, y=600)


        def showPassword():
            if txtPassword.cget('show')== "*":
                txtPassword.config(show='')
            else:
                txtPassword.config(show='*')
        btnShow = Checkbutton(root,text="Show",background="grey",command=showPassword)
        btnShow.place(x= 725,y= 520)


        lblName.mainloop()
        root.mainloop()
