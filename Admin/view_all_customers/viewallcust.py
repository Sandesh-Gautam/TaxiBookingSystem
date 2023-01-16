from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from Admin.view_all_customers.viewallcustdata import view_allcustomers

class ViewAllCustomers():
    def __init__(self):
        # Create the main window
        root = Tk()
        root.title("View All Customers")
        root.geometry("1700x1070")
        root.resizable(False, False)

        # Open the background image and set it as the background
        img = Image.open('taxipng.png')
        bg = ImageTk.PhotoImage(img)
        label = Label(root, image=bg)
        label.place(x=0, y=0)

        # Create a grey canvas and place it in the middle of the window
        d = Canvas(root, height=370, width=1070, bg="grey")
        d.pack(pady=280)
        d.pack()

        # Get all the customers from the view_allcustomers function
        customers = view_allcustomers()

        # Create a frame to hold the table
        tableFrame = Frame(root)
        tableFrame.place(x=500, y=300)

        # Create the table to display the customers
        tblPersons = ttk.Treeview(tableFrame)
        tblPersons['columns'] = ('Customer Id', 'Name', 'Phone', 'Email','Address')

        # Set the widths of each column
        tblPersons.column("#0", width=0, stretch=NO)
        tblPersons.column("Customer Id", width=100, anchor=CENTER)
        tblPersons.column("Name", width=150, anchor=CENTER)
        tblPersons.column("Phone", width=150, anchor=CENTER)
        tblPersons.column("Email", width=150, anchor=CENTER)
        tblPersons.column("Address", width=150, anchor=CENTER)

        # Set the headings of each column
        tblPersons.heading('#0', text='', anchor=CENTER)
        tblPersons.heading('Customer Id', text='Customer Id', anchor=CENTER)
        tblPersons.heading('Name', text='Name', anchor=CENTER)
        tblPersons.heading('Phone', text='Phone', anchor=CENTER)
        tblPersons.heading('Email', text='Email', anchor=CENTER)
        tblPersons.heading('Address', text='Address', anchor=CENTER)
        tblPersons.pack()

        # Iterating through a list of customers
        for cust in customers:
            # The values parameter is set to a tuple containing the customer's information
            tblPersons.insert(parent='', index='end', iid=cust[0], values=(cust[0], cust[1], cust[2], cust[3], cust[5]))
        tblPersons.pack()

        # Defining a function to handle the "Back" button being clicked
        def logon123():

            from Admin.admin_gui.admingui import AdminGUI
            root.destroy()
            AdminGUI()

        btnBack = Button(root, text="Back",background="#ff9999",command=logon123)
        btnBack.place(x=870,y=600)



        root.mainloop()
