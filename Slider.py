from tkinter import *
import tkinter.messagebox as msg

root= Tk()
root.geometry("1000x1000")
root.title("Sliders in Tkinter")

def get_vals():
    msg.showinfo("Slider",f"{sld2.get()} is debited from the account.")

label1= Label(root,text="How many dollars you want to withdraw?").pack()
# sld1= Scale(root, from_=0, to=100)
# sld1.set(8)
# sld1.pack()

sld2= Scale(root,from_=0, to=100, orient=HORIZONTAL,tickinterval=50)
sld2.pack()

b= Button(root, text="Withdraw",command=get_vals).pack()

root.mainloop()