from tkinter import *
from tkinter import messagebox
import pickle

headingfont = ('arial', 20, 'bold')
labelfont = ('arial', 15)

class Login:
    def __init__(self):
        self.root = Tk()
        self.root.configure(background='black')
        self.root.title("Login Page")
        self.root.geometry("700x400")


        self.heading = Label(self.root, text="Login", bg="black",fg="blue",font=headingfont)
        self.Username = Label(self.root, text="Username",bg="black",fg="blue",font=labelfont)
        self.Password = Label(self.root, text="Password", bg="black",fg="blue",font=labelfont)

        self.uname = Entry(self.root)
        self.pw = Entry(self.root,show="*")

        self.submit = Button(self.root, text="Submit", fg="Black",bg="Red", command=self.login)
        self.reset = Button(self.root, text="Reset", fg="Black",bg="Red", command=self.clear)

    def clear(self):
        self.uname.delete(0, END)
        self.pw.delete(0, END)

    def login(self):
        if (self.uname.get() == "" or self.pw.get() == ""):
            messagebox.showwarning("Username or Passwod cannot be empty!",parent=self.root)
        else:
            u = self.uname.get()
            p = self.pw.get()
            try:
                with open("file.txt", "rb") as fp:
                    while True:
                        try:
                            b = pickle.load(fp)
                            if(b[3] == u):
                                if(b[4] == p):
                                    messagebox.showinfo("Success!","Hello " + str(b[0]) + "! Welcome to Booking.com!",parent=self.root)
                                    break
                        except:
                            messagebox.showwarning("Failed!","Sorry. User not found!",parent=self.root)
                            break
                self.clear()
            except:
                messagebox.showwarning("Database Empty!","No users were found. Please Register.",parent=self.root)
                self.root.destroy()

    def render(self):
        self.heading.grid(row=0, column=1,pady="20")
        self.Username.grid(row=1, column=0)
        self.Password.grid(row=2, column=0)

        self.uname.grid(row=1, column=1, ipadx="100",ipady="10",padx="10")
        self.pw.grid(row=2, column=1,ipadx="100",ipady="10",padx="10")

        self.submit.grid(row=3,column=1,columnspan=2,sticky=W,padx="20",pady="20")
        self.reset.grid(row=3,column = 1 ,columnspan=2,sticky=E,padx="20",pady="20")

        self.root.mainloop()

def do_login():
    x=Login()
    x.render()
