from tkinter import *
import sys
def login():
  username="vishwas"
  password="123"
  if username==name.get() and password==pas.get():
      print("welcome")
      sys.exit()
  else:
        print("Invalid user")
        sys.exit()
window=Tk()
window.geometry("325x400")
window.title("Login Page")
username=Label(text="username:",font=("calibre",10,"bold"),fg="black")
password=Label(text="password:",font=("calibre",10,"bold"),fg="black")
username.grid()
password.grid(row=1)
name=StringVar()
pas=StringVar()
userentry=Entry(window,textvariable=name)
userentry.grid(row=0,column=1)
pasentry=Entry(window,textvariable=pas)
pasentry.grid(row=1,column=1)
btn1=Button(text="Submit",command=login)
btn1.grid(row=2)
window.mainloop()

