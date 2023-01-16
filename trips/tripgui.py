import tkinter
from tkinter import *
from trips.tripcrud import makeBooking
from tkinter import messagebox
from PIL import Image,ImageTk
from tkcalendar import DateEntry
import Global
import re

class MakeBooking():

    def __init__(self):

        def save():
            pick_up= txtPick_up.get()
            drop_off = txtDrop_off.get()
            date = txtDate.get()
            time = txtTime.get()
            cid = Global.customeracc[0]
            result = makeBooking(pick_up,drop_off,date, time, cid=cid)
            if (result == None):
                messagebox.showinfo("Booked", "Trip Booked Successfully")
            else:
                messagebox.showerror(":(", "Booking Unsuccessful")

        def Validate():
            validate_PickUpAddress = txtPick_up.get()
            pickupaddressRegex = re.compile(r'^[a-zA-Z0-9 ,]+$')
            validate_PickUpTime = txtTime.get()
            pickuptimeRegex = re.compile(r'^([01]?[0-9]|2[0-3]):[0-5][0-9] (AM|PM)$')
            validate_DropOffAddress = txtDrop_off.get()
            dropoffaddressRegex = re.compile(r'^[a-zA-Z0-9 ,]+$')

            if re.match(pickupaddressRegex, validate_PickUpAddress) and \
                    re.match(pickuptimeRegex, validate_PickUpTime) and re.match(dropoffaddressRegex,
                                                                                validate_DropOffAddress):
                save()
            else:
                messagebox.showwarning("Title", "Please enter the field correctly")
        root = Tk()
        root.title("Make your Booking")
        root.geometry("1700x1070")
        root.resizable(False,False)

        self.img = Image.open('taxipng.png')
        self.bg = ImageTk.PhotoImage(self.img)

        self.label = Label(root, image=self.bg)
        self.label.place(x=0, y=0)
        d = Canvas(root, height=500, width=1050, bg="grey")
        d.pack(padx=700, pady=280)

        d.pack()

        lblTitle = Label(root, text="Make your Booking Here", font=("Times New Roman", 18), background="grey")
        lblTitle.place(x=720, y=350)

        lblPick_up = Label(root, text="Pick Up: ",background="grey")
        lblDrop_off = Label(root, text="Drop Off: ",background="grey")
        lblDate = Label(root,text="Date: ",background="grey")
        lblTime = Label(root,text="Time: ",background="grey")



        txtPick_up = Entry(root,width=20)
        txtDrop_off = Entry(root,width=20)
        txtDate = DateEntry(root,width=20)
        txtTime = Entry(root, width=20)


        btnSave = Button(root, text="Make Booking",background="#ff9999",command=Validate)
        btnClose = Button(root, text="Close",background="#ff9999",command=exit)
        def ViewBooking12():
            root.destroy()
            from Customers.customer_viewbooking.cviewbooking import ViewBook
            ViewBook()
        btnView = Button(root, text="View Booking",background="#ff9999",command=ViewBooking12)

        def logon():
            root.destroy()
            from Login.logingui import Logingui
            Logingui()
        btnBack = Button(root, text="Back",background="#ff9999",command=logon)
        btnBack.place(x=820,y=700)


        lblPick_up.place(x=725, y=400)
        txtPick_up.place(x=825, y=400)

        lblDrop_off.place(x=725, y=450)
        txtDrop_off.place(x=825, y=450)

        lblDate.place(x=725, y=500)
        txtDate.place(x=825, y=500)

        lblTime.place(x=725, y=550)
        txtTime.place(x=825, y=550)



        btnSave.place(x=755, y=600)
        btnClose.place(x=910, y=600)
        btnView.place(x=800, y=650)

        lblApp = Label(root, text="Yourstaxi", font=("Snell", 60), background="black", foreground="White")
        lblApp.place(x=1290, y=50)


        lblPick_up.mainloop()
        root.mainloop()




