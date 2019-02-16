from tkinter import *
from login import do_login
from registration import do_register

if __name__ == '__main__':
    root = Tk()
    root.configure(background='black')
    root.title("Home Page")
    root.geometry("500x400")

    headingfont = ('arial', 20, 'bold')
    heading = Label(root, text="Home", bg="black")
    heading.config(fg="blue",height=3, width=20,font=headingfont)
    heading.grid(row=0, column=1)
    login = Button(root, text="Login", fg="Black",bg="Red", command=do_login)
    login.grid(row=1,column=1,sticky=N,padx=200,pady=40)
    register = Button(root, text="Register", fg="Black",bg="Red", command=do_register)
    register.grid(row=2,column=1,sticky=N,padx=200,pady=40)
    root.mainloop()
