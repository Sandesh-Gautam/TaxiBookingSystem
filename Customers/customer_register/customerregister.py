import tkinter
from tkinter import *
from tkinter import messagebox, Label, Button
from Customers.customer_register.cregisterdata import saveCustomer
from PIL import ImageTk, Image
from tkinter import ttk
import mysql.connector
import re



class Custregister1():
    def __init__(self):
            def save():
                #Get values from textboxes
                name = txtName.get()
                address = txtAddress.get()
                email = txtEmail.get()
                phone = txtPhone.get()
                password = txtPassword.get()
                payment = txtPayment.get()

                #Establishing connection to the database
                conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='',
                                               database='yourstaxi')
                cursor = conn.cursor()
                #Checking if email already exists in the database
                cursor.execute("SELECT * FROM customers WHERE email=%s", (email,))
                results = cursor.fetchall()

                #Validation checks
                if not name or not email or not password or not address or not phone:
                    messagebox.showerror("Invalid", "All fields are required")
                elif not re.match(r"[^@]+@[^@]+.[^@]+", email):
                    messagebox.showerror("Invalid", "Invalid email address")
                elif len(phone) < 10:
                    messagebox.showerror("Invalid", "Mobile Number must be at least 10 characters")
                elif len(password) < 8:
                    messagebox.showerror("Invalid", "Password must be at least 8 characters")
                elif results:
                    messagebox.showerror("Invalid", "Email already exists")
                else:
                    # If input is valid, insert data into the database and show success message
                    print("Inserted Successfully!!")
                    saveCustomer(name, address, phone, email, password, payment)
                    messagebox.showinfo("Title", "User Registered")
                    root.destroy()

            # Creating Toplevel window
            root = Toplevel()
            root.title("Customer Registration")
            root.geometry("1700x1070")
            root.resizable(False, False)

            # Opening background image
            img = Image.open('taxipng.png')
            bg = ImageTk.PhotoImage(img)

            # Creating a label for the background image
            label = Label(root, image=bg)
            label.place(x=0, y=0)

            # Creating a canvas
            d = Canvas(root, height=500, width=1050, bg="grey")
            d.pack(padx=700, pady=280)

            # Packing the canvas
            d.pack()

            # Creating labels
            lblName = Label(root, text="Full name: ", background="grey")
            lblPhone = Label(root, text="Phone: ", background="grey")
            lblAddress = Label(root, text="Address: ", background="grey")
            lblEmail = Label(root, text="Email: ", background="grey")
            lblPassword = Label(root, text="Password: ", background="grey")
            lblPayment = Label(root, text="Payment: ", background="grey")

            # Creating textboxes
            txtName = Entry(root, width=20)
            txtPhone = Entry(root, width=20)
            txtAddress = Entry(root, width=20)
            txtEmail = Entry(root, width=20)
            txtPassword = Entry(root, width=20, show="*")
            txtPayment = ttk.Combobox(root, values=['Online payment', 'Cash payment'])

            # Creating buttons
            btnSave = Button(root, text="Register", background="#ff9999", command=save)

            # Navigating to login page
            def logon1():
                root.destroy()
                from Login.logingui import Logingui
                Logingui()

            btnClose = Button(root, text="Close", background="#ff9999", command=logon1)

            # Placing labels and textboxes
            lblName.place(x=725, y=300)
            txtName.place(x=825, y=300)

            lblAddress.place(x=725, y=350)
            txtAddress.place(x=825, y=350)

            lblPhone.place(x=725, y=400)
            txtPhone.place(x=825, y=400)

            lblEmail.place(x=725, y=450)
            txtEmail.place(x=825, y=450)

            lblPassword.place(x=725, y=500)
            txtPassword.place(x=825, y=500)

            lblPayment.place(x=725,y=550)
            txtPayment.place(x=825,y=550)

            btnSave.place(x=755, y=650)
            btnClose.place(x=910, y=650)

            def showPassword():
                if txtPassword.cget('show')== "*":
                    txtPassword.config(show='')
                else:
                    txtPassword.config(show='*')
            btnShow = Checkbutton(root,text="Show",background="grey",command=showPassword)
            btnShow.place(x= 725,y= 520)
            lblApp = Label(root, text="Yourstaxi", font=("Snell", 60), background="black", foreground="White")
            lblApp.place(x=1290, y=50)

            root.mainloop()


