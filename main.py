# main python file (password generator)
from tkinter import *
from functional import *
from tkinter import messagebox
def main_algo():
    x = int(passlen.get())
    generated.delete(0, END)
    obj = Func(x)
    generated.insert(0, obj.generate(x))
def copy():
    root.clipboard_clear()
    root.clipboard_append(generated.get())
    messagebox.showinfo("Accept", "Password Coppied!!")
def reset():
    b =messagebox.askquestion("Confirm", "Are you sure?")
    if b=="yes":
        print(b)
        userentry.delete(0, END)
        lenentry.delete(0, END)
        generated.delete(0, END)
root = Tk()
root.title('Password generator')
root.geometry('600x400')

a = Label(text="Password Generator", font="Times 20 italic bold underline", fg="blue", justify='center')
a.grid(row=0, column=1)

un = Label(text="Enter User Name:", font="18")
un.grid(padx=10, pady=10)
name = StringVar()
userentry = Entry(root, textvariable=name, relief=SUNKEN, border=4, width=26)
userentry.grid(row=1, column=1)

pl = Label(text="Enter Password Length:", font="18")
pl.grid(padx=10, pady=10)
passlen = StringVar()
lenentry = Entry(root, textvariable=passlen, relief=SUNKEN, border=4, width=26)
lenentry.grid(row=2, column=1)

gp = Label(text="Generated Password:", font="18")
gp.grid(padx=10, pady=10)
genpass = StringVar()
generated = Entry(root, textvariable=genpass, relief=SUNKEN, border=4, width=26)
generated.grid(row=3, column=1)

b1 = Button(root, text="GENERATE PASSWORD", bg="blue", fg="white", 
            font="18", border=3, relief=GROOVE, command=main_algo)
b1.config(highlightbackground="black", highlightcolor="black")
b1.grid(row=4, column=1, pady=10)

b2 = Button(root, text="ACCEPT", fg="black",
            font="18", border=3, relief=GROOVE, command=copy)
b2.config(highlightbackground="black", highlightcolor="black")
b2.grid(row=5, column=1, pady=10)

b3 = Button(root, text="RESET", fg="black",
            font="18", border=3, relief=GROOVE, command=reset)
b3.config(highlightbackground="black", highlightcolor="black")
b3.grid(row=6, column=1, pady=10)

root.mainloop()
