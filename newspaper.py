from tkinter import *
from PIL import Image, ImageTk

root= Tk()
root.title("Newspaper")
root.maxsize(827,827)

 
l1= Label(root,text="Times of India",font="Lucida 33 bold",bg="lightgrey")
l1.pack(fill=X)
l2= Label(root,text="Thursday,June 11",font="Timesnewroman 13 italic",bg="lightgrey")
l2.pack(fill=X)

f=Frame(root,width=600,height=400,padx=17,pady=17)
img= Image.open(r"D:\python lab\images\newspaper1.jpeg")
img=img.resize((300,200),Image.Resampling.LANCZOS)
photo=ImageTk.PhotoImage(img)

l3= Label(f,image=photo)
l3.pack(anchor=W,side=LEFT,padx=20,pady=17)

l4= Label(f,text="Kuwait closed its airspace on Thursday while Bahrain and Jordan issued safety advisories after air defence systems were activated amid a widening security crisis in West Asia and the Gulf region.\n\nThe alerts came as the Iran-US confrontation entered a more volatile phase, with American forces announcing fresh strikes on Iranian military targets and Iran-linked reports claiming retaliation against US military-related sites in the region.",wraplength=300,font="arial 8 bold")
l4.pack(anchor="ne",side=RIGHT,padx=15,pady=15)
f.pack(side=TOP,anchor=NW)

f1=Frame(root,padx=20,pady=20,width=600,height=400)
img1= Image.open(r"D:\python lab\images\news2.jpeg")
img1= img1.resize((300,200),Image.Resampling.LANCZOS)
photo1=ImageTk.PhotoImage(img1)

l5=Label(f1,image=photo1)
l5.pack(side=RIGHT,anchor=NE)

l6= Label(f1,text="Two Indian seafarers were killed, while one is still missing, after a US military attack on a commercial vessel off the Oman coast, reported ANI, citing the Forward Seamen's Union of India (FSUI).\n\n 21 Indians were rescued after the attack.We have been unable to establish a connection with the ship, General Secretary of FSUI Manoj Yadav told ANI, adding,The latest information I have indicates that two have died, while the Chief Engineer is still reported as missing.",wraplength=300,font="arial 8 bold")
l6.pack(side=LEFT,anchor=N,padx=17,pady=17)
f1.pack(side=TOP,anchor=NE)

f2= Frame(root,width=600,height=400,padx=17,pady=17)
img2= Image.open(r"D:\python lab\images\news3.jpeg")
img2=img2.resize((300,200),Image.Resampling.LANCZOS)
photo2=ImageTk.PhotoImage(img2)

l7= Label(f2,image=photo2)
l7.pack(side=LEFT,anchor=NW,padx=17,pady=17)

l8= Label(f2,text="Trump congratulates Modi on becoming India's longest-serving elected PM.\n\nHe is a strong, healthy, and wise man, and will have many years of greatness and success ahead of him,says the U.S. President",wraplength=300,font="arial 8 bold")
l8.pack(pady=17,side=RIGHT,anchor=E)
f2.pack(side=LEFT,anchor=SE)

root.mainloop()
