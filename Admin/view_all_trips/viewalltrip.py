from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from Admin.view_all_trips.viewalltripdata import view_alltrips

# Class to create a window to view all trips
class ViewAllTrips():
    # Initializing the class
    def __init__(self):
        # Creating the main window
        root = Tk()
        root.title("View All Trips")
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

        # Get all the trips from the view_alltrips function
        trips = view_alltrips()

        # Create a frame to hold the table
        tableFrame = Frame(root)
        tableFrame.place(x=500, y=300)

        # Create the table to display the trips
        tblPersons = ttk.Treeview(tableFrame)
        tblPersons['columns'] = ('Trip Id', 'Pickup-Address', 'Dropoff-Address', 'Pickup-Date','Pickup-Time')

        # Set the widths of each column
        tblPersons.column("#0", width=0, stretch=NO)
        tblPersons.column("Trip Id", width=100, anchor=CENTER)
        tblPersons.column("Pickup-Address", width=150, anchor=CENTER)
        tblPersons.column("Dropoff-Address", width=150, anchor=CENTER)
        tblPersons.column("Pickup-Time", width=150, anchor=CENTER)
        tblPersons.column("Pickup-Date", width=150, anchor=CENTER)

        # Set the headings of each column
        tblPersons.heading('#0', text='', anchor=CENTER)
        tblPersons.heading('Trip Id', text='Trip Id', anchor=CENTER)
        tblPersons.heading('Pickup-Address', text='Pickup-Address', anchor=CENTER)
        tblPersons.heading('Dropoff-Address', text='Dropoff-Address', anchor=CENTER)
        tblPersons.heading('Pickup-Time', text='Pickup-Time', anchor=CENTER)
        tblPersons.heading('Pickup-Date', text='Pickup-Date', anchor=CENTER)

        # Adding the trips data to the table
        for trip in trips:
            tblPersons.insert(parent='', index='end', iid=trip[0], values=(trip[0], trip[1], trip[2], trip[3], trip[4]))
        tblPersons.pack()


        def logon123():
            from Admin.admin_gui.admingui import AdminGUI
            root.destroy()
            AdminGUI()

        btnBack = Button(root, text="Back",background="#ff9999",command=logon123)
        btnBack.place(x=870,y=600)

        root.mainloop()
