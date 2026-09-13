from tkinter import *
# def display1():
#     fm["bg"]="red"
# def display2():
#     fm["bg"]="green"
# def display3():
#     fm["bg"]="pink"
my_root=Tk()
my_root.geometry("700x700")
my_root.title("colours")
fm=Frame(my_root,width=700,height=700,bg="white")#for various other colours go to colour code picker and write code of colour
fm.propagate(0)
fm.pack()

# #for button
# btn1=Button(fm,width=15,height=2,text="Red colour",fg="black",bg="red",command=display1)
# btn1.pack()
# btn2=Button(fm,width=15,height=2,text="green colour",fg="black",bg="green",command=display2)
# btn2.pack()
# btn3=Button(fm,width=15,height=2,text="pink colour",fg="black",bg="pink",command=display3)
# btn3.pack()
# my_root.mainloop()

##for check box
def show():
    if v1.get()==1 and  v2.get()==1 and  v3.get()==1 :
        fm["bg"]="#A9A9A9"
    elif v1.get()==1 and  v2.get()==1 :
        fm["bg"]="purple"
    elif v1.get()==1 and  v3.get()==1 :
        fm["bg"]="brown"
    elif v2.get()==1 and  v3.get()==1 :
        fm["bg"]="#008080"
    elif v1.get()==1:
        fm["bg"]='red'
    elif v2.get()==1:
        fm["bg"]="blue"
    elif v3.get()==1:
        fm["bg"]="green"  
    else:fm["bg"]="white"
v1=IntVar()
chk1=Checkbutton(fm, text="Red colour",variable=v1,command=show)
chk1.pack()
v2=IntVar()
chk2=Checkbutton(fm, text="blue colour",variable=v2,command=show)
chk2.pack()
v3=IntVar()
chk3=Checkbutton(fm, text="green colour",variable=v3,command=show)
chk3.pack()
my_root.mainloop()
