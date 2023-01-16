from tkinter import *
from PIL import Image,ImageTk

class AdminGUI():
    def __init__(self):
        root = Tk()
        root.title("Admin")
        root.geometry("1700x1070")
        root.resizable(False,False)

        # Open and set image as background
        img = Image.open('taxipng.png')
        bg = ImageTk.PhotoImage(img)
        label = Label(root, image=bg)
        label.place(x=0, y=0)

        # Create canvas
        d = Canvas(root, height=500, width=1050, bg="grey")
        d.pack(padx=700, pady=280)
        d.pack()

        # Create title label
        lblTitle = Label(root, text="ADMIN", font=("Times New Roman", 18), background="grey")
        lblTitle.place(x=800, y=350)

        # Create "Assign Driver" button
        def ViewAllTrips012():
            root.destroy()
            from Admin.assign_driver.pending_trips import ViewBook
            ViewBook()
        btnAssign = Button(root, text="Assign Driver",background="#ff9999",command=ViewAllTrips012)

        # Create "View All Customers" button
        def ViewAllCustomers0():
            root.destroy()
            from Admin.view_all_customers.viewallcust import ViewAllCustomers
            ViewAllCustomers()
        btnViewC = Button(root, text="View All Customers",background="#ff9999",command=ViewAllCustomers0)

        # Create "View All Drivers" button
        def ViewAllDrivers0():
            root.destroy()
            from Admin.view_all_drivers.viewalldriv import ViewAllDrivers
            ViewAllDrivers()
        btnViewD = Button(root, text="View All Drivers",background="#ff9999",command=ViewAllDrivers0)

        # Create "View All Trips" button
        def ViewAllTrips0():
            root.destroy()
            from Admin.view_all_trips.viewalltrip import ViewAllTrips
            ViewAllTrips()
        btnViewT = Button(root, text="View All Trips", background="#ff9999",command=ViewAllTrips0)

        # Create "Close" button
        btnClose = Button(root, text="Close",background="#ff9999",command=exit)

        # Create "Back" button
        def logon123():
            root.destroy()
            from Login.logingui import Logingui
            Logingui()
        btnBack = Button(root, text="Back",background="#ff9999",command=logon123)
        btnBack.place(x=870,y=730)

        # Create "Yourstaxi" label
        lblApp = Label(root, text="Yourstaxi", font=("Snell", 60), background="black", foreground="White")
        lblApp.place(x=1290, y=50)

        # Place buttons on screen
        btnAssign.place(x=800,y=450)
        btnViewC.place(x=800,y=520)
        btnViewD.place(x=800, y=590)
        btnViewT.place(x=800, y=660)
        btnClose.place(x=770, y=730)

        # Start main loop for GUI
        root.mainloop()

