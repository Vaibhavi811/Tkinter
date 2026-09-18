from tkinter import *
root= Tk()
root.title("Window Resizer")

def get_vals():
    width= w.get()
    height=h.get()
    root.geometry(f"{width}x{height}")

l1= Label(root,text="Welcome to our Window Resizer Application",bg="Pink",font="Lucida 33 bold")
l1.pack()

f= Frame(root,padx=20,pady=20)
l2= Label(f,text="Enter Width",font="Mscomicsans 17 italic")
l2.grid(row=0,column=0)
l3= Label(f,text="Enter Height",font="Mscomicsans 17 italic")
l3.grid(row=1,column=0)

w= IntVar()
h=IntVar()

e1= Entry(f,textvariable=w)
e1.grid(row=0,column=1)
e2= Entry(f,textvariable=h)
e2.grid(row=1,column=1)

b= Button(f,text="Apply to Layout" ,command=get_vals).grid(row=2,column=0,columnspan=2)
f.pack()


root.mainloop()