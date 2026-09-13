from tkinter import *
window=Tk()
window.geometry("400x400")
window.title("Notebook")
f=Frame(window,width=400,height=350,bg="grey")
f.propagate(0)
f.pack()
text_area=Text(f,font=("Arial",16))
text_area.pack(fill="both",expand=True)#expand=True,Ye line window ki puri space me widget ko expand kar deti h.Here textarea
def text(): 
    txt=text_area.get('1.0',"end")
    f=open("ntbk.txt","a")
    f.write(txt)
    f.close()
def clear_txt(): 
    text_area.delete(1.0,"end")
   

btn1=Button(window,text="Save",command=text)
btn1.pack()
btn2=Button(window,text="Clear",command=clear_txt)
btn2.pack()
window.mainloop()