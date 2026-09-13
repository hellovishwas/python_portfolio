from tkinter import *
def addition():
    x=float(first.get())
    y=float(second.get())
    z=x+y
    th.set(z)
def subtraction():
    x=float(first.get())
    y=float(second.get())
    z=x-y
    th.set(z)
def multiplication():
    x=float(first.get())
    y=float(second.get())
    z=x*y
    th.set(z)
def division():
    try:
        x=float(first.get())
        y=float(second.get())
        z=x/y
        th.set(z)
    except ZeroDivisionError:th.set("INVALID INPUT")
#Main           
window=Tk()
window.geometry("325x400")
window.title("vishwas")

first=StringVar()
second=StringVar()
th=StringVar()

lb1=Label(text="First No.",font=("calibre",10,"bold"),fg='red')
lb1.grid(row=0,column=0)
first=Entry(window,textvariable=first)
first.grid(row=0,column=1)
lb2=Label(text="Second No.",font=("calibre",10,"bold"),fg='red')
lb2.grid(row=1,column=0)
second=Entry(window,textvariable=second)
second.grid(row=1,column=1)
lb3=Label(text="Answer",font=("calibre",10,"bold"),fg='red')
lb3.grid(row=6,column=0)
third=Entry(window,textvariable=th)
third.grid(row=6,column=1)
btn1=Button(text="Add",command=addition)
btn1.grid(row=2)
btn2=Button(text="sub",command=subtraction)
btn2.grid(row=3)
btn3=Button(text="mul",command=multiplication)
btn3.grid(row=4)
btn4=Button(text="div",command=division)
btn4.grid(row=5)

window.mainloop()