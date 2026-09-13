# from tkinter import *
# window=Tk()
# window.geometry("325x400")
# window.title("Calculator")
# f=Frame(window,width=400,height=400,bg="grey")
# f.propagate(0)
# f.pack()
def btn(w,h,b,t,p,l,c=0):
    import tkinter
    b=tkinter.Button(f,width=w,height=h,bg=b,text=t,command=c)
    b.place(x=p,y=l)
# btn(2,4,"blue","kite",20,30)
# window.mainloop()

'''

from tkinter import*
window=Tk()
window.geometry("300x200")
window.title("greet")
f=Frame(window,width=300,height=200,bg="grey")
f.propagate(0)
f.pack()
def gret():
    print("hello Vishwas")
btn(10,10,"white","greet",150,100,gret)
window.mainloop()
'''
'''
from tkinter import*
window=Tk()
window.geometry("200x200")
window.title("recycle")
f=Frame(window,height=200,width=200,bg="grey")
f.propagate(0)
f.pack()
def rec():
    btn(6,2,"yellow","new text",20,20)

btn(6,2,"yellow","old text",20,20)
btn(5,2,"white","change",100,100,rec)
window.mainloop()
'''
from tkinter import*
root=Tk()
entry=Entry(root,width=30,)
entry.pack()
root.mainloop()
