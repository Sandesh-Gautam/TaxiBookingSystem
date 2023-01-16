from tkinter import *
from logincrud import search_customer,search_driver,search_admin
from tkinter import messagebox
import Global
from PIL import Image,ImageTk

class Logingui():
    def __init__(self):

            def searchvd():
                email=txtEmail.get()
                password=txtPassword.get()
                customer = search_customer(email,password)
                driver = search_driver(email,password)
                admin = search_admin(email,password)
                if customer !=None:
                    Global.customeracc = customer
                    messagebox.showinfo("Customer Login Sucessful","Welcome {}".format(txtEmail.get()))
                    root.destroy()
                    from trips.tripgui import MakeBooking
                    MakeBooking()

                elif driver != None:
                    Global.driveracc = driver
                    messagebox.showinfo("Driver Login Sucessful","Welcome {}".format(txtEmail.get()))
                    root.destroy()
                    from Drivers.driver_viewbooking.dviewbooking import ViewBook
                    ViewBook()

                elif admin != None:
                    Global.adminacc = admin
                    messagebox.showinfo("Admin Login Sucessful","Welcome {}".format(txtEmail.get()))
                    root.destroy()
                    from Admin.admin_gui.admingui import AdminGUI
                    AdminGUI()

                else:
                    messagebox.showerror(":(", "Incorrect Username or Password")
            root = Tk()
            root.title("Log In")
            root.geometry("1700x1070")
            root.resizable(False,False)
            img = Image.open('taxipng.png')
            bg = ImageTk.PhotoImage(img)

            label = Label(root, image=bg)
            label.place(x=0, y=0)

            d = Canvas(root, height=500, width=1050, bg="grey")
            d.pack(padx=700, pady=280)



            d.pack()



            lblTitle = Label(root,text="Welcome to the Login Page",font=("Times New Roman",18),background="grey")
            lblTitle.place(x=710,y=380)

            lblApp = Label(root,text="Yourstaxi",font=("Snell",60),background="black",foreground="White")
            lblApp.place(x=1290,y=50)


            lblEmail = Label(root,text="Email: ",background="grey")
            lblPassword = Label(root, text="Password: ",background="grey")

            txtEmail = Entry(root, width=20)
            txtPassword = Entry(root, width=20,show="*")

            btnSave = Button(root, text="Log In",background="#ff9999",command=lambda :searchvd())
            btnClose = Button(root, text="Close",background="#ff9999",command=exit)


            lblEmail.place(x=725, y=450)
            txtEmail.place(x=825, y=450)

            lblPassword.place(x=725, y=500)
            txtPassword.place(x=825, y=500)

            btnSave.place(x=755, y=600)
            btnClose.place(x=910, y=600)

            def Custregister12():
                from Customers.customer_register.customerregister import Custregister1
                Custregister1()

            btnRegister_Customer = Button(root,text="Register as Customer",background="#ff9999",command=Custregister12)
            def Drivregister12():
                from Drivers.driver_register.driverregister import Drivregister1
                Drivregister1()
            btnRegister_Driver = Button(root,text="Register as Driver",background="#ff9999",command=Drivregister12)

            btnRegister_Customer.place(x=780,y=650)
            btnRegister_Driver.place(x=790,y=700)


            def showPassword():
                if txtPassword.cget('show') == "*":
                    txtPassword.config(show='')
                else:
                    txtPassword.config(show='*')


            btnShow = Checkbutton(root, text="Show", background="grey", command=showPassword)
            btnShow.place(x=725, y=520)


            root.mainloop()

Logingui()
















