from tkinter import *
from tkinter import ttk
from Customers.customer_viewbooking.cviewbookingdata import view_booking1

from PIL import Image,ImageTk
from Admin.assign_driver.available_drivers import ViewAvailableDrivers

class ViewBook():
    def __init__(self):
        # Create Tkinter window
        self.root = Tk()
        self.root.title("Pending Trips")
        self.root.geometry("1700x1070")
        self.root.resizable(False, False)
        self.tripid = None
        self.img = Image.open('taxipng.png')
        self.bg = ImageTk.PhotoImage(self.img)

        # Set background image
        self.label = Label(self.root, image=self.bg)
        self.label.place(x=0, y=0)
        d = Canvas(self.root, height=370, width=1070, bg="grey")
        d.pack(pady=280)
        d.pack()

        # Get pending trips
        trips = view_booking1()

        # Create frame for table
        tableFrame = Frame(self.root)
        tableFrame.place(x=450, y=300)

        # Create ttk.Treeview widget to display pending trips
        self.tblPersons = ttk.Treeview(tableFrame)
        self.tblPersons['columns'] = ('tid', 'Pickup-Address', 'Dropoff-Address','Pickup-Date', 'Pickup-Time','Status')

        # Set column widths and headers for table
        self.tblPersons.column("#0", width=0, stretch=NO)
        self.tblPersons.column("tid", width=100, anchor=CENTER)
        self.tblPersons.column("Pickup-Address", width=150, anchor=CENTER)
        self.tblPersons.column("Dropoff-Address", width=150, anchor=CENTER)
        self.tblPersons.column("Pickup-Time", width=150, anchor=CENTER)
        self.tblPersons.column("Pickup-Date", width=150, anchor=CENTER)
        self.tblPersons.column("Status", width=150, anchor=CENTER)



        self.tblPersons.heading('#0', text='', anchor=CENTER)
        self.tblPersons.heading('tid', text='TID', anchor=CENTER)
        self.tblPersons.heading('Pickup-Address', text='Pickup-Address', anchor=CENTER)
        self.tblPersons.heading('Dropoff-Address', text='Dropoff-Address', anchor=CENTER)
        self.tblPersons.heading('Pickup-Time', text='Pickup-Time', anchor=CENTER)
        self.tblPersons.heading('Pickup-Date', text='Pickup-Date', anchor=CENTER)
        self.tblPersons.heading('Status', text='Status', anchor=CENTER)
        self.tblPersons.bind("<<TreeviewSelect>>", self.selectId)
        self.tblPersons.pack()
        # Insert trips into table
        for trip in trips:
            self.tblPersons.insert(parent='', index='end', iid=trip[0], values=(trip[0], trip[1], trip[2], trip[3],trip[4],trip[7]))
            self.tblPersons.pack()
            # Create button to assign driver to selected trip
        btnAssign = Button(self.root, text="Assign", background="#ff9999", command=self.driverList)
        btnAssign.place(x=800, y=600)
        btnBack = Button(self.root, text="Back", background="#ff9999", command=self.logon123)
        btnBack.place(x=870, y=600)

    def selectId(self, _):
        self.tripid = self.tblPersons.selection()[0]

    def driverList(self):
        # Destroy current window and open available driver window
        self.root.destroy()
        if not self.tripid:
            return
        ViewAvailableDrivers(self.tripid)

    def logon123(self):
        from Admin.admin_gui.admingui import AdminGUI
        self.root.destroy()
        AdminGUI()

        self.root.mainloop()






