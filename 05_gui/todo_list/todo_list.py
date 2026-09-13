from tkinter import *
window=Tk()
window.geometry("300x300")
window.title("To Do List")
window.config(bg="grey")
lb1=Label(text="Be Disciplined!",font=("calibre",10,"bold"),fg='red')
lb1.grid(row=0,column=4)



def add_task():
    win=Tk()
    win.geometry("300x300")
    win.title("Add task")
    win.config(bg="sky blue")
    entry=Entry(win,width=100,bg="white")
    entry.place(x=0,y=0)
    def save():
        tsk=entry.get()
        with open("to_do_list.txt",'a')as f:
            f.write(f"{tsk}\n")
    btn2=Button(win,text="Save",command=save)
    btn2.place(x=0,y=18)
    
def view_task():
    win=Toplevel()
    win.geometry("300x300")
    win.title("View task")
    win.config(bg="white")
    with open("to_do_list.txt",'r')as f:
        data=f.read()
        lbl=Label(win,text=data,font=("calibre",10,"bold"),fg='black')
        lbl.grid(row=1)
    win.mainloop()
def clear_task():
    with open("to_do_list.txt",'w')as f:
        f.write("")
    lbl=Label(window,text="All tasks deleted successfully!",font=("calibre",10,"bold"),fg='red')
    lbl.place(x=75,y=250)
    
def exit():
    window.destroy()



btn1=Button(width=10,height=2,text="Add Task",command=add_task)
btn1.grid(row=1)
btn1=Button(width=10,height=2,text="View Task",command=view_task)
btn1.grid(row=2)
btn1=Button(width=10,height=2,text="Clear Task",command=clear_task)
btn1.grid(row=3)
btn1=Button(width=10,height=2,text="Exit",command=exit)
btn1.grid(row=4)
window.mainloop()
