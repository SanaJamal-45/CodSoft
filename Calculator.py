from tkinter import *
def click(value):
    ex=e1.get()
    ans=""
    try:
        if value =="C":
            ex=ex[0:len(ex)-1]
            e1.delete(0,END)
            e1.insert(0,ex)
            return
        elif value==chr(247):
            e1.insert(END,"/")
            return
        elif value=="=":
            ans=eval(ex)
        else:
            e1.insert(END,value)
            return
        e1.delete(0, END)
        e1.insert(0, ans)

    except SyntaxError:
        pass
m=Tk()
m.title("My Simple Calculator")
m.geometry("500x500+100+100")
m.config(bg="#FF34B3")
icon=PhotoImage(file="calculator icon.png")
m.iconphoto(False,icon)
m.resizable(False,False)
e1=Entry(m,bg="#D15FEE",fg="white",width=29,bd=10,relief=SUNKEN,font="comicsansms 20 bold")
e1.grid(row=0,column=0,columnspan=5,padx=20,pady=20)
buttons_list=["7","8","9","+","4","5","6","-","1","2","3","*","C","0","=",chr(247)]  #chr(247)=/
rowvalue=2
colvalue=1
for i in buttons_list:
    b1=Button(m,width=5,height=2,borderwidth=2,bg="#D15FEE",fg="white",text=i,font="comicsansms 20 bold",activebackground="Hot Pink",command=lambda b1=i: click(b1))
    b1.grid(row=rowvalue,column=colvalue,pady=5,padx=5)
    colvalue+=1
    if colvalue>4:
        rowvalue+=1
        colvalue=1
m.mainloop()