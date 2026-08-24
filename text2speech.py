from tkinter import *
import pyttsx3
root= Tk()
root.geometry("827x827")
root.configure(background="Lightgrey")
root.title("Text to Speech GUI")
root.resizable(False,False)

def convert():
    engine= pyttsx3.init()
    s= ishu.get()
    engine.say(s)
    engine.runAndWait()

lab= Label(root, text="Text-to-Speech", font="Lucida 29 bold",anchor=N)
lab.pack(padx=12,pady=8,fill=BOTH,expand=TRUE)

lab1= Label(lab, text="Text",font="timesnewroman 18 italic")
lab1.pack(side=LEFT,padx=5)

ishu= StringVar()
e1= Entry(lab,textvariable=ishu)
e1.pack(side=LEFT, padx=10)

b= Button(lab,text="Convert",font="Timesnewroman 12 italic",command=convert)
b.pack(side=LEFT,padx=5)



root.mainloop()