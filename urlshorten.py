from tkinter import *
import pyshorteners
root= Tk()
root.geometry("827x827")
root.title("Shorten Url Link")
root.configure(background="lightgrey")

def convert():
    shorten=pyshorteners.Shortener()
    url= shorten.tinyurl.short(long.get())
    e2.insert(0, url)

lab1= Label(root, text="Enter Long URL", font="Lucida 22 italic")
lab1.pack(pady=8)

long= StringVar()
e1= Entry(root,textvariable=long,font="timesnewroman 15 italic",justify=CENTER)
e1.pack(pady=5)
e1.focus()

lab2= Label(root, text="Short URL",font="Lucida 22 italic")
lab2.pack(pady=8)

short= StringVar()
e2= Entry(root,textvariable=short,font="timesnewroman 15 italic")
e2.pack(pady=5)

b= Button(root, text="Convert", bg="grey",fg="Red",font="Lucida 20 italic",command=convert)
b.pack(pady=8)
root.mainloop()