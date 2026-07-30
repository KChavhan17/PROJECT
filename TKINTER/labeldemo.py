# labeldemo.py
from tkinter import *

top = Tk()
top.geometry("300x200")

lbl1 = Label(top, text="Name")
lbl1.place(x=10, y=10)

lbl2 = Label(top, text="Password", fg="red", bg="yellow")
lbl2.place(x=10, y=40)

lbl3 = Label(top, text="Age", padx=10, pady=10, bg="green")
lbl3.place(x=10, y=70)

top.mainloop()