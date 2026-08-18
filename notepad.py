from tkinter import *
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

root= Tk()
root.title("Untitled-Notepad")
root.geometry("900x900")
root.wm_iconbitmap("Tkinter\icon.ico")

def new_file():
    global file
    root.title("Untitled-Notepad")
    file=None
    txt.delete(1.0 ,END)

def open_file():
    global file
    file= askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),
                                                             ("Text Documents","*.txt")])
    if(file==""):
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        txt.delete(1.0,END)
        f= open(file,"r")
        txt.insert(1.0,f.read())
        f.close()

def save():
    global file
    if(file==None):
        file= asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if(file==""):
            file=None
        else:
            f= open(file,"w")
            f.write(txt.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
    else:
        f= open(file,"w")
        f.write(txt.get(1.0,END))
        f.close()

def cut():
    txt.event_generate(("<<Cut>>"))

def copy():
    txt.event_generate(("<<Copy>>"))

def paste():
    txt.event_generate(("<<Paste>>"))

def aboutUs():
    msg.showinfo("Notepad","This is a Notepad made using Tkinter.")

file=None

mainmenu= Menu(root)

filemenu= Menu(mainmenu,tearoff=0)
filemenu.add_command(label="New",command=new_file)
filemenu.add_command(label="Open",command=open_file)
filemenu.add_separator()
filemenu.add_command(label="Save",command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)

mainmenu.add_cascade(menu=filemenu, label="File")

edit= Menu(mainmenu,tearoff=0)
edit.add_command(label="Cut",command=cut)
edit.add_command(label="Copy",command=copy)
edit.add_command(label="Paste",command=paste)

mainmenu.add_cascade(menu=edit, label="Edit")

help= Menu(mainmenu,tearoff=0)
help.add_command(label="About us",command=aboutUs)

mainmenu.add_cascade(menu=help, label="Help")

root.config(menu=mainmenu)
scroll= Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

txt= Text(root, yscrollcommand=scroll.set,background="lightgrey")
txt.pack(fill=BOTH,expand=TRUE)

scroll.config(command=txt.yview)
root.mainloop()
