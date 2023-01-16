from tkinter import *
from tkinter import ttk

import Global
from Customers.customer_viewbooking.cviewbookingdata import view_booking
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry

from Customers.customer_viewbooking.cviewbookingdata import update_booking
from Customers.customer_viewbooking.cviewbookingdata import delete_booking


class ViewBook():
    def __init__(self):
        root = Tk()
        root.title("View Booking")
        root.geometry("1700x1070")
        root.resizable(False, False)

        # Open and set background image
        img = Image.open('taxipng.png')
        bg = ImageTk.PhotoImage(img)

        label = Label(root, image=bg)
        label.place(x=0, y=0)

        # Create a grey canvas for the UI elements
        d = Canvas(root, height=370, width=1070, bg="grey")
        d.pack(pady=280)
        d.pack()

        # Create a label for the title of the application
        lblApp = Label(root, text="Yourstaxi", font=("Snell", 60), background="black", foreground="White")
        lblApp.place(x=1290, y=50)

        # Get the current customer's ID and retrieve their bookings
        cid = Global.customeracc[0]
        trips = view_booking(cid)

        # Create a frame to hold the table of bookings
        tableFrame = Frame(root)
        tableFrame.place(x=450, y=300)

        # Create a table to display the bookings
        tblPersons = ttk.Treeview(tableFrame)
        tblPersons['columns'] = ('tid', 'Pickup-Address', 'Dropoff-Address', 'Pickup-Date', 'Pickup-Time', 'Status')

        tblPersons.column("#0", width=0, stretch=NO)
        tblPersons.column("tid", width=100, anchor=CENTER)
        tblPersons.column("Pickup-Address", width=150, anchor=CENTER)
        tblPersons.column("Dropoff-Address", width=150, anchor=CENTER)
        tblPersons.column("Pickup-Time", width=150, anchor=CENTER)
        tblPersons.column("Pickup-Date", width=150, anchor=CENTER)
        tblPersons.column("Status", width=150, anchor=CENTER)


        tblPersons.heading('#0', text='', anchor=CENTER)
        tblPersons.heading('tid', text='TID', anchor=CENTER)
        tblPersons.heading('Pickup-Address', text='Pickup-Address', anchor=CENTER)
        tblPersons.heading('Dropoff-Address', text='Dropoff-Address', anchor=CENTER)
        tblPersons.heading('Pickup-Date', text='Pickup-Date', anchor=CENTER)
        tblPersons.heading('Pickup-Time', text='Pickup-Time', anchor=CENTER)
        tblPersons.heading('Status', text='Status', anchor=CENTER)

        tblPersons.pack()

        for trip in trips:
            tblPersons.insert(parent='', index='end', iid=trip[0], values=(trip[0], trip[1], trip[2], trip[3], trip[4],trip[7]))
        tblPersons.pack()



        lblPick_up = Label(root, text="Pick Up: ",background="grey",foreground="black")
        lblDrop_off = Label(root, text="Drop Off: ",background="grey",foreground="black")
        lblDate = Label(root,text="Date: ",background="grey",foreground="black")
        lblTime = Label(root,text="Time: ",background="grey",foreground="black")


        txtPick_up = Entry(root,width=20)
        txtDrop_off = Entry(root,width=20)
        txtDate = DateEntry(root,width=20)
        txtTime = Entry(root, width=20)

        lblPick_up.place(x=350, y=550)
        txtPick_up.place(x=400, y=550)

        lblDrop_off.place(x=1040, y=550)
        txtDrop_off.place(x=1100, y=550)

        lblDate.place(x=350, y=580)
        txtDate.place(x=400, y=580)

        lblTime.place(x=1040, y=580)
        txtTime.place(x=1100, y=580)

        def Update():
            selectedItem = tblPersons.selection()[0]
            pick_up = txtPick_up.get()
            drop_off = txtDrop_off.get()
            date = txtDate.get()
            time = txtTime.get()
            tid = tblPersons.item(selectedItem)['values'][0]
            print(tid)
            result = update_booking(pick_up,drop_off,date,time,tid)
            if (result != None):
                messagebox.showinfo("Booking Updated", "Booking Update Successful")

            else:
                messagebox.showerror(":(", "Update Unsuccessful")

        btnUpdate = Button(root,text="Update",background="#ff9999",command=Update)
        btnUpdate.place(x=650,y=600)
        def maketrip1():
            root.destroy()
            from trips.tripgui import MakeBooking
            MakeBooking.__init__(self)
        btnBack = Button(root,text="Back",background="#ff9999",command=maketrip1)
        btnBack.place(x=750,y=600)
        def Delete():
            selectedItem = tblPersons.selection()[0]
            tid = tblPersons.item(selectedItem)['values'][0]
            result = delete_booking([tid])
            if (result != None):
                messagebox.showinfo("Booking Deleted", "Booking Deletion Successful")

            else:
                messagebox.showerror(":(", "Deletion Unsuccessful")
        btnDelete = Button(root,text="Delete Booking",background="#ff9999",command=Delete)
        btnDelete.place(x=850,y=600)

        def displaySelectedItem(a):
            txtDate.delete(0,END)
            txtDrop_off.delete(0,END)
            txtPick_up.delete(0,END)
            txtTime.delete(0,END)


            selectedItem = tblPersons.selection()[0]
            txtPick_up.insert(0, tblPersons.item(selectedItem)['values'][1])
            txtDrop_off.insert(0, tblPersons.item(selectedItem)['values'][2])
            txtDate.insert(0, tblPersons.item(selectedItem)['values'][3])
            txtTime.insert(0, tblPersons.item(selectedItem)['values'][4])
            tblPersons.selection()[0].insert("pending", tblPersons.item(selectedItem)['values'][5])
        tblPersons.bind("<<TreeviewSelect>>", displaySelectedItem)




        root.mainloop()

