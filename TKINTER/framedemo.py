# framedemo.py
from tkinter import *

top = Tk()
top.geometry("300x200")

tframe = Frame(top, width="100", height="100", bg="yellow")
tframe.pack()

lframe = Frame(top, width="100", height="50", bg="blue")
lframe.pack(side=LEFT)

rframe = Frame(top, width="100", height="50", bg="green")
rframe.pack(side=RIGHT)

btn1 = Button(tframe, text="Submit", fg="red")
btn1.place(x=10, y=10)

top.mainloop()