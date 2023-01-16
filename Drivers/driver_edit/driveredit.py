import tkinter
from tkinter import *
from tkinter import messagebox
from dedit import editDriver
from PIL import Image,ImageTk

# function to update the driver's information
def update():
    # get the entered information from the entry fields
    name = txtName.get()
    address = txtAddress.get()
    licenseno = txtLicenseno.get()
    email = txtEmail.get()
    password = txtPassword.get()
    # call the editDriver function with the entered information
    result = editDriver(name,licenseno,email, password, address)
    # check if the result is true, display a message box with "Driver Edited"
    if result == True:
        messagebox.showinfo("Title", "Driver Edited")
    # if the result is false, display a message box with "Invalid ID"
    else:
        messagebox.showerror("Title", "Invalid ID")

# create the main window
root = Tk()
root.title("Update Driver")
root.geometry("1700x1070")
root.resizable(False,False)

# open and display the background image
img = Image.open('taxipng.png')
bg = ImageTk.PhotoImage(img)
label = Label(root, image=bg)
label.place(x=0, y=0)

# create a canvas to hold the form
d = Canvas(root, height=370, width=1050, bg="grey")
d.pack(padx=700, pady=280)
d.pack()

# create labels for the form
lblName = Label(root, text="Full name: ",background="grey")
lblLicenseno = Label(root, text="License no: ",background="grey")
lblAddress = Label(root,text="Address: ",background="grey")
lblEmail = Label(root,text="Email: ",background="grey")
lblPassword = Label(root, text="Password: ",background="grey")

# create entry fields for the form
txtName = Entry(root,width=20)
txtLicenseno = Entry(root,width=20)
txtAddress = Entry(root,width=20)
txtEmail = Entry(root, width=20)
txtPassword = Entry(root, width=20)

# create buttons for the form
btnSave = Button(root, text="Update",background="#ff9999",command=update)
btnClose = Button(root, text="Close",background="#ff9999",command=exit)

# place the labels and entry fields on the canvas
lblName.place(x=725, y=300)
txtName.place(x=825, y=300)

lblAddress.place(x=725, y=350)
txtAddress.place(x=825, y=350)

lblLicenseno.place(x=725, y=400)
txtLicenseno.place(x=825, y=400)

lblEmail.place(x=725, y=450)
txtEmail.place(x=825, y=450)
lblPassword.place(x=725, y=500)
txtPassword.place(x=825, y=500)

btnSave.place(x=755, y=600)
btnClose.place(x=910, y=600)

lblApp = Label(root,text="Yourstaxi",font=("Snell",60),background="black",foreground="White")
lblApp.place(x=1290,y=50)

lblName.mainloop()
root.mainloop()