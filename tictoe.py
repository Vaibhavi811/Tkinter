from tkinter import *
import tkinter.messagebox as msg
root= Tk()
root.geometry("500x500")
root.title("Tic-Tac-Toe")

def chance():
    global i
    i+=1
    return i

def click(event):
    text= event.widget.cget("text")
    
    com=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    ch=chance()

    if(ch in [0,2,4,6,8]):
        event.widget.configure(text="X")
        event.widget.configure(background="Red")
        l1.append(int(text))
        for i in range(0,8):
            if(com[i][0] in l1 and com[i][1] in l1 and com[i][2] in l1):
                msg.showinfo("Tic-Tac-Toe","Player 1 wins")
                root.destroy()
    elif(ch in [1,3,5,7]):
        event.widget.configure(text="O")
        event.widget.configure(background="Blue")
        l2.append(int(text))
        for i in range(0,8):
            if(com[i][0] in l2 and com[i][1] in l2 and com[i][2] in l2):
                msg.showinfo("Tic-Tac-Toe","Player 2 wins")
                root.destroy()

    else:
        msg.showinfo("Tic-Tac-Toe","Tie..")
        root.destroy()

l1=[]
l2=[]    
i=-1
f1= Frame(root,relief=SUNKEN, bd=5)
b1=Button(f1,text="0",font="lucida 40 italic")
b1.bind("<Button-1>",click)
b1.pack(side=LEFT,padx=5,pady=5, ipadx=35, ipady=20)
b2= Button(f1, text="1",font="lucida 40 italic")
b2.pack(side=LEFT,padx=5,pady=5, ipadx=35, ipady=20)
b2.bind("<Button-1>",click)
b3= Button(f1, text="2",font="lucida 40 italic")
b3.pack(side=LEFT,padx=5,pady=5, ipadx=35, ipady=20)
b3.bind("<Button-1>",click)
f1.pack()

f2= Frame(root,relief=SUNKEN, bd=5)
b4=Button(f2,text="3",font="lucida 40 italic")
b4.pack(side=LEFT,padx=5,pady=5, ipadx=35, ipady=20)
b4.bind("<Button-1>",click)
b5= Button(f2, text="4",font="lucida 40 italic")
b5.pack(side=LEFT,padx=5,pady=5, ipadx=35, ipady=20)
b5.bind("<Button-1>",click)
b6= Button(f2, text="5",font="lucida 40 italic")
b6.pack(side=LEFT,padx=5,pady=5, ipadx=35, ipady=20)
b6.bind("<Button-1>",click)
f2.pack()

f3= Frame(root,relief=SUNKEN, bd=5)
b7=Button(f3,text="6",font="lucida 40 italic")
b7.pack(side=LEFT,padx=5,pady=5, ipadx=35, ipady=20)
b7.bind("<Button-1>",click)
b8= Button(f3, text="7",font="lucida 40 italic")
b8.pack(side=LEFT,padx=5,pady=5, ipadx=35, ipady=20)
b8.bind("<Button-1>",click)
b9= Button(f3, text="8",font="lucida 40 italic")
b9.pack(side=LEFT,padx=5,pady=5, ipadx=35, ipady=20)
b9.bind("<Button-1>",click)
f3.pack()

root.mainloop()