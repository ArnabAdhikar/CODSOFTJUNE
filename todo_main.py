# to do list main file
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle
def delete_item():
    lbox.delete(ACTIVE)
def add_item():
    lbox.insert(END, e.get())
    x.append(e.get())
    e.delete(0, END)
def cross_item():
    lbox.itemconfig(
        lbox.curselection(),
        fg="#dedede"
    )
    lbox.selection_clear(0, END)
def uncross_item():
    lbox.itemconfig(
        lbox.curselection(),
        fg="#464646"
    )
    lbox.selection_clear(0, END)
def del_crossed():
    for i in range(lbox.size()):
        if lbox.itemcget(i, 'foreground') == "#dedede":
            lbox.delete(i)
def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="D:\\to_do_list",
        title="Save File",
        filetypes=((("Dat Files", "*.dat"), 
                    ("All Files", "*.*")))
    )
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name=f'{file_name}.dat'
        # delete crossed off items before saving
        del_crossed()
        elements = lbox.get(0, END)
        # opening the file
        output = open(file_name, 'wb')
        pickle.dump(elements, output)
def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="D:\\to_do_list",
        title="Open File",
        filetypes=((("Dat Files", "*.dat"), 
                    ("All Files", "*.*")))
    )
    if file_name:
        # delete currently opened list
        lbox.delete(0, END)
        input_file = open(file_name, "rb")
        element = pickle.load(input_file)
        for i in element:
            lbox.insert(END, i)
def clear_list():
    lbox.delete(0, END)

root = Tk()
root.title("To-Do-List")
root.geometry("600x500")

# setting up font
my_font = Font(
    family="Gadugi",
    size=15
)

# listbox
frame = Frame(root)
frame.pack(pady=10)
lbox = Listbox(frame,
               font=my_font,
               width=32,
               height=10,
               bg="SystemButtonFace",
               bd=0,
               fg='#464646',
               highlightthickness=0,
               activestyle="none"
               )
lbox.pack(side=LEFT, fill=BOTH)
# test elements
# x = ["Take a nap", "Start DSA", "Go througt the internship messages"]
# for i in x:
#     lbox.insert(END, i)
x = []
# scrollbar
scroll = Scrollbar(frame, orient="vertical", command=lbox.yview)
scroll.pack(side=RIGHT, fill=Y)
scroll2 = Scrollbar(frame, orient="horizontal", command=lbox.xview)
scroll2.pack(side=BOTTOM, fill=X)

# entry box
e = Entry(root, font=("Blackadder ITC", 24), width=35)
e.pack(pady=20)

# menu box
menu1 = Menu(root)
root.config(menu=menu1)
# adding items
file_menu = Menu(menu1, tearoff=False)
menu1.add_cascade(label="File", menu=file_menu)
# adding drop down menu
file_menu.add_command(label="Save_List", command=save_list)
file_menu.add_command(label="Open_List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear_List", command=clear_list)

# bottom frame
frame2 = Frame(root)
frame2.pack(pady=20)
# buttons
d_button = Button(frame2, text="Delete Item", command=delete_item)
a_button = Button(frame2, text="Add Item", command=add_item)
cross_button = Button(frame2, text="Cross Item", command=cross_item)
uncross_button = Button(frame2, text="Uncross Item", command=uncross_item)
del_crossed_btn = Button(frame2, text="Delete Crossed", command=del_crossed)
d_button.grid(row=0, column=0)
a_button.grid(row=0, column=1, padx=20)
cross_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
del_crossed_btn.grid(row=0, column=4)

root.iconbitmap("todo.png")
root.mainloop()
