# building calculator.
from tkinter import *
import math              # for scientific computation
def click(event):
    text = event.widget.cget("text")       # capturing the values
    if text == "=":
        if a.get().isdigit():
            value = int(a.get())
        else:
            try:
                value = eval(a.get())
            except:
                value = "math error"
        a.set(value)
        screen.update()
    elif text == "C":
        a.set("")
        screen.update()
    else:
        a.set(a.get() + text)
        screen.update()
root = Tk()
root.title("Calculator")
root.geometry("344x500")
root.wm_iconbitmap("calc.ico")
a = StringVar()
a.set("")
screen = Entry(root, textvariable=a, font="arial 15 bold")
screen.pack(fill=X, pady=10, padx=10, ipadx=8, ipady=8)
l1 = [7, 8, 9, 4, 5, 6, 1, 2, 3, "+", "-", "=", "/", "*", ".", "0", "^", "C", "**", "(", ")", "math.sin", "math.cos",
      "math.tan"]
j = 0
for i in range(0, 8):
    f1 = Frame(root, bg="black")
    b = Button(f1, text=f"{l1[j]}", font="aharoni 14 bold")
    b.pack(padx=8, pady=8, side=LEFT)
    b.bind("<Button-1>", click)
    j += 1
    b = Button(f1, text=f"{l1[j]}", font="aharoni 14 bold")
    b.pack(padx=8, pady=8, side=LEFT)
    b.bind("<Button-1>", click)
    j += 1
    b = Button(f1, text=f"{l1[j]}", font="aharoni 14 bold")
    b.pack(padx=8, pady=8, side=LEFT)
    b.bind("<Button-1>", click)
    j += 1
    f1.pack()
root.mainloop()
