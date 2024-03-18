#Task 1- To do list
from tkinter import *
from tkinter import messagebox
#add task
def add_task():
    task=e1.get()
    if task !="":
        listbox.insert(END,task)
        e1.delete(0,"end")
    else:
        messagebox.showinfo("ATTENTION!","Kindly,enter a task.")
#delete task
def delete_task():
    listbox.delete(ANCHOR)
#Main window
m=Tk()
m.title("My To-do List")
m.geometry("400x600+100+100")
m.config(bg="#E64398")
m.resizable(False,False)
icon=PhotoImage(file="to do list icon.png")
m.iconphoto(False,icon)
heading=Label(m,text="Things To do",bg="#E64398",fg="Black",font="Arial 20 bold" )
heading.pack(side=TOP,fill=X)
frame=Frame(m,width=400,height=500,bg="#E64398")
frame.place(x=0,y=80)
l1=Label(frame,text="Enter Task Here!",fg="Black",font="Arial 12",bg="#E64398")
l1.place(x=2,y=20)
e1=Entry(frame,font="Arial 20",bg="#00BFFF",fg="Black",width=26,bd=1,relief=SUNKEN)
e1.place(x=4,y=50)
b1=Button(frame,text="Add Task",bg="#00BFFF",fg="Black",width=10,command=add_task)
b1.place(x=64,y=450)
b2=Button(frame,text="Delete Task",bg="#00BFFF",fg="Black",width=10,command=delete_task)
b2.place(x=250,y=450)
frame_2=Frame(frame,width=360,height=340,bg="#E64398",bd=10)
frame_2.place(x=7,y=100)
listbox=Listbox(frame_2,font="Arial 10",bg="#00BFFF",fg="black",width=49,height=18,cursor="hand2")
listbox.pack(side=RIGHT,fill=BOTH,padx=1)
scrollbar=Scrollbar(frame_2)
scrollbar.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
all_tasks = ["Pray Tahajudd","Eat Suhoor","Pray Fajr","Recite Quran","Recite Morning Supplication","Read book","Practice Programming","Pray Zuhr","Take a power nap","Study Tafseer","Pray Asr","Recite Evening Supplication","Break fast","Perform Maghrib","Perform Isha","Perform Taraweeh","Perform Witr","Recite Night Supplication","Sleep"]
for each_task in all_tasks:
    listbox.insert(END,each_task)
m.mainloop()
