from tkinter import *
from tkinter import messagebox
from random import randint
import pyperclip
def generate_pass():
    e2.delete(0,END)
    pass_length=int(e1.get())
    password=""
    for i in range(pass_length):
        password +=chr(randint(33,126))
        e2.insert(0,password)
    messagebox.showinfo("Congrats!", "Password Generated Successfully!")
def copy():
    rand_pass=e2.get()
    pyperclip.copy(rand_pass)
    messagebox.showinfo("Done!","Password successfully copied!")
def reset():
    e1.delete(0,END)
    e2.delete(0,END)
    messagebox.showinfo("Done!", "Password successfully reset!")
m=Tk()
m.title("My Password Generator")
m.geometry("500x500+100+100")
m.config(bg="#fb6f92")
m.resizable(False,False)
icon=PhotoImage(file="password generator icon.png")
m.iconphoto(False,icon)
heading=Label(m,text="My Password Generator",bg="#fb6f92",fg="Black",font="comicsansms 20 underline",bd=10)
heading.pack(side=TOP,fill=X)
l1=Label(m,text="Enter Password's Length",bg="#00b4d8",fg="Black",width=20,height=2,font="Arial 10 bold")
l1.place(x=30,y=150)
e1=Entry(m,font="Arial 25",fg="Black",bg="#00b4d8",width=10)
e1.place(x=290,y=150)
b1=Button(m,text="Generate Password",fg="Black",bg="#00b4d8",width=20,height=2,font="Arial 10 bold",command=generate_pass)
b1.place(x=30,y=250)
e2=Entry(m,font="Arial 25",fg="Black",bg="#00b4d8",width=10)
e2.place(x=290,y=250)
b2=Button(m,text="Copy to Clipboard",fg="Black",bg="#00b4d8",width=20,height=2,font="Arial 10 bold",command=copy)
b2.place(x=30,y=350)
b3=Button(m,text="Reset Password",fg="Black",bg="#00b4d8",width=20,height=2,font="Arial 10 bold",command=reset)
b3.place(x=290,y=350)
m.mainloop()
