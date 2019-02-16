from tkinter import *
from tkinter import messagebox
from login import do_login
import pickle

headingfont = ('arial', 20, 'bold')
labelfont = ('arial', 15)

class Register:
    def __init__(self):
        self.root = Tk()
        self.root.configure(background='black')
        self.root.title("Registration Form")
        self.root.geometry("700x400")

        self.heading = Label(self.root, text="Register", bg="black",fg="blue",font=headingfont)

        self.Name = Label(self.root, text="Name",bg="black",fg="blue",font=labelfont)
        self.Username = Label(self.root, text="Username",bg="black",fg="blue",font=labelfont)
        self.Phone_no = Label(self.root, text="Phone",bg="black",fg="blue",font=labelfont)
        self.Email_Id = Label(self.root, text="Email Id", bg="black",fg="blue",font=labelfont)
        self.Password = Label(self.root, text="Password", bg="black",fg="blue",font=labelfont)
        self.Confirm = Label(self.root, text="Confirm Password", bg="black",fg="blue",font=labelfont)

        self.name = Entry(self.root)
        self.email_id = Entry(self.root)
        self.phone = Entry(self.root)
        self.uname = Entry(self.root)
        self.pw = Entry(self.root,show="*")
        self.pw2 = Entry(self.root,show="*")

        self.submit = Button(self.root, text="Submit", fg="Black",bg="Red", command=self.insert)

        self.reset = Button(self.root, text="Reset", fg="Black",bg="Red", command=self.clear)

    def clear(self):
        self.name.delete(0, END)
        self.uname.delete(0, END)
        self.phone.delete(0, END)
        self.email_id.delete(0, END)
        self.pw.delete(0, END)
        self.pw2.delete(0, END)

    def insert(self):
        #f = open('file.txt','a')
        if (self.name.get() == "" or
            self.uname.get() == "" or
            self.phone.get() == "" or
            self.email_id.get() == "" or
            self.pw.get() == "" or
            self.pw2.get() == ""):
            messagebox.showwarning("Empty Input!","Please fill all the details.",parent=self.root)

        else:
            if(self.pw.get()!=self.pw2.get()):
                messagebox.showwarning("Confirmation Error","Passwords do not match. Please try again!",parent=self.root)
            else:
                entry=[]
                entry.append(self.name.get())
                entry.append(self.email_id.get())
                entry.append(self.phone.get())
                entry.append(self.uname.get())
                entry.append(self.pw.get())
                # f.write(str(entry))
                # f.write(";")
                with open("file.txt", "ab") as fp:   #Pickling
                        pickle.dump(entry,fp)
                #f.close()
                messagebox.showinfo("Account created.","Please login using new credentials. :)",parent=self.root)
                self.root.destroy()
                do_login()

    def render(self):

        self.heading.grid(row=0, column=1,pady="20")
        self.Name.grid(row=1, column=0)
        self.Email_Id.grid(row=2, column=0)
        self.Phone_no.grid(row=3, column=0)
        self.Username.grid(row=4, column=0)
        self.Password.grid(row=5, column=0)
        self.Confirm.grid(row=6, column=0)
        self.name.grid(row=1, column=1, ipadx="100",ipady="10",padx="10")
        self.email_id.grid(row=2, column=1, ipadx="100",ipady="10",padx="10")
        self.phone.grid(row=3, column=1, ipadx="100",ipady="10",padx="10")
        self.pw.grid(row=5, column=1, ipadx="100",ipady="10",padx="10")
        self.uname.grid(row=4, column=1, ipadx="100",ipady="10",padx="10")
        self.pw2.grid(row=6, column=1, ipadx="100",ipady="10",padx="10")

        self.submit.grid(row=9,column=1,columnspan=2,sticky=W,padx="20",pady="20")

        self.reset.grid(row=9,column = 1 ,columnspan=2,sticky=E,pady="20",padx="20")
        self.root.mainloop()

def do_register():
    x=Register()
    x.render()
