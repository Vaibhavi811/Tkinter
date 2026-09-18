from tkinter import *
root= Tk()
root.title("Scrollbar in tkinter")
root.geometry("827x827")


scroll= Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

txt= Text(root, font="Lucida 15 italic", yscrollcommand=scroll.set)
txt.pack()

scroll.config(command=txt.yview)
root.mainloop()