from tkinter import *
from textblob import TextBlob
root= Tk()
root.title("Spelling Checker")
root.geometry("900x900")
root.configure(background="lightblue")
root.resizable(False,False)

def check():
    word= spell.get()
    s=TextBlob(word)
    correct= str(s.correct())
    Label(root,text=correct,bg="lightblue").place(x=420,y=390)


lab= Label(root, text="Spelling Checker",font="Lucida 22 italic", fg="red",bg="lightgrey")
lab.place(x=320, y=250)

spell= StringVar()
e= Entry(root,textvariable=spell,justify=CENTER)
e.place(x=370,y=310)
e.focus()

b= Button(root, text="Check", fg="Red", bg="lightgrey",command=check)
b.place(x=410, y=350)

lab1= Label(root, text="Did you mean:",bg="lightblue")
lab1.place(x=340,y=390)

root.mainloop()