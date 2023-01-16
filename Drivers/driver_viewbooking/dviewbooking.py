from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from Drivers.driver_viewbooking.dviewbookingdata import view_booking

class ViewBook():
    def __init__(self):

        #create the main window
        root = Tk()
        root.title("View Booking")
        root.geometry("1700x1070")
        root.resizable(False,False)
        #open and display the background image
        img = Image.open('taxipng.png')
        bg = ImageTk.PhotoImage(img)

        label = Label(root, image=bg)
        label.place(x=0, y=0)

        #create a canvas to hold the table
        d = Canvas(root, height=370, width=1070, bg="grey")
        d.pack(pady=280)
        d.pack()
        #create a label
        lblApp = Label(root, text="Yourstaxi", font=("Snell", 60), background="black", foreground="White")
        lblApp.place(x=1290, y=50)

        #get the data for the table from the view_booking function
        trips = view_booking()

        #create a frame to hold the table
        tableFrame = Frame(root)
        tableFrame.place(x=500, y=300)

        #create the table
        tblPersons = ttk.Treeview(tableFrame)
        tblPersons['columns'] = ['tid', 'Pickup-Address', 'Dropoff-Address','Pickup-Date', 'Pickup-Time']

        #set the width of each column
        tblPersons.column("#0", width=0, stretch=NO)
        tblPersons.column("tid", width=100, anchor=CENTER)
        tblPersons.column("Pickup-Address", width=150, anchor=CENTER)
        tblPersons.column("Dropoff-Address", width=150, anchor=CENTER)
        tblPersons.column("Pickup-Time", width=150, anchor=CENTER)
        tblPersons.column("Pickup-Date", width=150, anchor=CENTER)

        #set the headings of each column
        tblPersons.heading('#0', text='', anchor=CENTER)
        tblPersons.heading('tid', text='TID', anchor=CENTER)
        tblPersons.heading('Pickup-Address', text='Pickup-Address', anchor=CENTER)
        tblPersons.heading('Dropoff-Address', text='Dropoff-Address', anchor=CENTER)
        tblPersons.heading('Pickup-Time', text='Pickup-Time', anchor=CENTER)
        tblPersons.heading('Pickup-Date', text='Pickup-Date', anchor=CENTER)

        for trip in trips:
            tblPersons.insert(parent='', index='end', iid=trip[0], values=(trip[0], trip[1], trip[2], trip[3], trip[4]))
        tblPersons.pack()

        def logon123():
            root.destroy()
            from Login.logingui import Logingui
            Logingui()

        btnBack = Button(root, text="Back",background="#ff9999",command=logon123)
        btnBack.place(x=820,y=600)



        root.mainloop()

