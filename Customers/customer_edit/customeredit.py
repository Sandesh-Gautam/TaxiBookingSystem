from tkinter import *
from tkinter import messagebox

from ceditdata import editCustomer


def save():
    #Get values from textboxes
    name = txtName.get()
    address = txtAddress.get()
    phone = txtPhone.get()
    email = txtEmail.get()
    password = txtPassword.get()
    #Call editCustomer function to update values
    result = editCustomer(name, phone,email, password, address)
    if result == True:
        #Show success message
        messagebox.showinfo("Title", "Customer Edited")

    else:
        #Show error message
        messagebox.showerror(":(", "Customer Update Unsuccessful")

root = Tk()
root.title("Update Customer")
root.geometry("1700x1070")
root.resizable(False,False)
C = Canvas(root)
bgimage = PhotoImage(file="taxipng.png")
background_label = Label(root, image=bgimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

d = Canvas(root, height=370, width=1050, bg="grey")
d.pack(padx=700, pady=280)

d.pack()
C.pack()
lblApp = Label(root,text="Yourstaxi",font=("Snell",60),background="black",foreground="White")
lblApp.place(x=1290,y=50)

#Create labels
lblName = Label(root, text="Full name: ",background="grey")
lblPhone = Label(root, text="Phone: ",background="grey")
lblAddress = Label(root,text="Address: ",background="grey")
lblEmail = Label(root,text="Email: ",background="grey")
lblPassword = Label(root, text="Password: ",background="grey")

#Create textboxes
txtName = Entry(root,width=20)
txtPhone = Entry(root,width=20)
txtAddress = Entry(root,width=20)
txtEmail = Entry(root, width=20)
txtPassword = Entry(root, width=20)

#Create buttons
btnSave = Button(root, text="Update",background="#ff9999",command=save)
btnClose = Button(root, text="Close",background="#ff9999",command=exit)

#Place labels and textboxes on window
lblName.place(x=725, y=300)
txtName.place(x=825, y=300)

lblAddress.place(x=725, y=350)
txtAddress.place(x=825, y=350)

lblPhone.place(x=725, y=400)
txtPhone.place(x=825, y=400)

lblEmail.place(x=725, y=450)
txtEmail.place(x=825, y=450)

lblPassword.place(x=725, y=500)
txtPassword.place(x=825, y=500)

#Place buttons on window
btnSave.place(x=755, y=600)
btnClose.place(x=910,y=600)

#Start the main loop
lblName.mainloop()
root.mainloop()
