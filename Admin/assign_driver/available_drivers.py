from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from PIL import Image,ImageTk
from Admin.view_all_drivers.viewalldrivdata import view_alldrivers

class ViewAvailableDrivers():
    def __init__(self,tripid):
        # Initialize variables
        self.tripid = tripid
        self.root = Tk()
        self.root.title("View Available Drivers")
        self.root.geometry("1700x1070")
        self.root.resizable(False, False)

        # Open and set background image
        self.img = Image.open('taxipng.png')
        self.bg = ImageTk.PhotoImage(self.img)

        label = Label(self.root, image=self.bg)
        label.place(x=0, y=0)
        d = Canvas(self.root, height=370, width=1070, bg="grey")
        d.pack(pady=280)

        # Create and pack canvas
        d.pack()

        # Get all drivers from view_alldrivers function
        Drivers = view_alldrivers()

        # Create table frame
        tableFrame = Frame(self.root)
        tableFrame.place(x=500, y=300)

        # Create ttk.Treeview widget to display drivers
        self.tblPersons = ttk.Treeview(tableFrame)
        self.tblPersons['columns'] = ('Driver Id', 'Name', 'Address', 'Email','License no')

        # Set column widths and headings
        self.tblPersons.column("#0", width=0, stretch=NO)
        self.tblPersons.column("Driver Id", width=100, anchor=CENTER)
        self.tblPersons.column("Name", width=150, anchor=CENTER)
        self.tblPersons.column("License no", width=150, anchor=CENTER)
        self.tblPersons.column("Email", width=150, anchor=CENTER)
        self.tblPersons.column("Address", width=150, anchor=CENTER)

        self.tblPersons.heading('#0', text='', anchor=CENTER)
        self.tblPersons.heading('Driver Id', text='Driver Id', anchor=CENTER)
        self.tblPersons.heading('Name', text='Name', anchor=CENTER)
        self.tblPersons.heading('License no', text='License no', anchor=CENTER)
        self.tblPersons.heading('Email', text='Email', anchor=CENTER)
        self.tblPersons.heading('Address', text='Address', anchor=CENTER)

        # Bind event for selecting a driver
        self.tblPersons.bind("<<TreeviewSelect>>",self.selectId)

        # Insert all drivers into the table
        for driv in Drivers:
            self.tblPersons.insert(parent='', index='end', iid=driv[0], values=(driv[0], driv[1], driv[2], driv[3],driv[4]))
            self.tblPersons.pack()

        # Create "Back" button
        def logon123():
            from Admin.assign_driver.pending_trips import ViewBook
            self.root.destroy()
            ViewBook()

        btnBack = Button(self.root, text="Back", background="#ff9999", command=logon123)
        btnBack.place(x=900, y=600)

    def selectId(self, _):
        # Get selected driver id
        self.driverid = self.tblPersons.selection()[0]

        # Create "Select Driver" button
        btnAssign = Button(self.root, text="Select Driver", background="#ff9999", command=self.selectDriver)
        btnAssign.place(x=800, y=600)

    def selectDriver(self):
        # Print driver id and trip id for testing
        print(self.driverid, self.tripid)
        if not self.driverid:
            return
        # Update SQL query to assign driver to trip
        sql = "UPDATE trips SET did=%s, status= 'confirm' WHERE tid=%s"
        values = (self.driverid, self.tripid)
        self.root.destroy()
        # Show messagebox on success
        messagebox.showinfo("Success", "Driver assigned successfully")
        record = None

        # Connect to database
        conn = mysql.connector.connect(host='localhost',
                port='3306',
                user='root',
                password='',
                database='yourstaxi'
                )
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        # Close the window and return to previous window


