
# Importing necessary modules
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
# Importing the view_alldrivers function from the viewalldrivdata module
from Admin.view_all_drivers.viewalldrivdata import view_alldrivers

# Defining the ViewAllDrivers class
class ViewAllDrivers():
    def __init__(self):
        # Creating the main window
        root = Tk()
        # Setting the title of the window
        root.title("View All Drivers")
        # Setting the size of the window
        root.geometry("1700x1070")
        # Disabling the ability to resize the window
        root.resizable(False, False)

        # Open the background image and set it as the background
        img = Image.open('taxipng.png')
        bg = ImageTk.PhotoImage(img)
        label = Label(root, image=bg)
        label.place(x=0, y=0)

        # Create a grey canvas and place it in the middle of the window
        d = Canvas(root, height=370, width=1070, bg="grey")
        # Pack the canvas on the window
        d.pack(pady=280)
        d.pack()

        # Get all the drivers from the view_alldrivers function
        Drivers = view_alldrivers()

        # Create a frame to hold the table
        tableFrame = Frame(root)
        tableFrame.place(x=500, y=300)

        # Create the table to display the drivers
        tblPersons = ttk.Treeview(tableFrame)
        # Defining the columns of the table
        tblPersons['columns'] = ('Driver Id', 'Name','Address' , 'Email','Phone')

        # Set the widths of each column
        tblPersons.column("#0", width=0, stretch=NO)
        tblPersons.column("Driver Id", width=100, anchor=CENTER)
        tblPersons.column("Name", width=150, anchor=CENTER)
        tblPersons.column("Phone", width=150, anchor=CENTER)
        tblPersons.column("Email", width=150, anchor=CENTER)
        tblPersons.column("Address", width=150, anchor=CENTER)

        # Setting the headings of each column
        tblPersons.heading('#0', text='', anchor=CENTER)
        tblPersons.heading('Driver Id', text='Driver Id', anchor=CENTER)
        tblPersons.heading('Name', text='Name', anchor=CENTER)
        tblPersons.heading('Phone', text='Phone', anchor=CENTER)
        tblPersons.heading('Email', text='Email', anchor=CENTER)
        tblPersons.heading('Address', text='Address', anchor=CENTER)

        # Packing the table
        tblPersons.pack()

        # Iterating through a list of drivers
        for driv in Drivers:
            tblPersons.insert(parent='', index='end', iid=driv[0], values=(driv[0], driv[1], driv[2], driv[3], driv[4]))
        tblPersons.pack()
        # Packing the table to display it in the main window
        tblPersons.pack()

        # Defining a function to handle the "Back" button being clicked
        def logon123():
            # Destroying the current window
            root.destroy()
            # Importing the AdminGUI module from the admin_gui package
            from Admin.admin_gui.admingui import AdminGUI
            # Creating an instance of the AdminGUI class
            AdminGUI()

        # Creating the "Back" button
        btnBack = Button(root, text="Back", background="#ff9999", command=logon123)
        btnBack.place(x=870, y=600)

        # Running the main event loop of the program
        root.mainloop()

