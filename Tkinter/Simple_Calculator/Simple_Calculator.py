from tkinter import *

root = Tk()

root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def btn_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def btn_clear():
    e.delete(0, END)
    
def btn_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)
    
def btn_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def btn_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def btn_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divition"
    f_num = int(first_number)
    e.delete(0, END)
    
def btn_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "divition":
        e.insert(0, f_num / int(second_number))
        

#Define btns
btn_0 = Button(root, text="0", padx=40, pady=20, command=lambda: btn_click(0)) 
btn_1 = Button(root, text="1", padx=40, pady=20, command=lambda: btn_click(1))
btn_2 = Button(root, text="2", padx=40, pady=20, command=lambda: btn_click(2))
btn_3 = Button(root, text="3", padx=40, pady=20, command=lambda: btn_click(3))
btn_4 = Button(root, text="4", padx=40, pady=20, command=lambda: btn_click(4))
btn_5 = Button(root, text="5", padx=40, pady=20, command=lambda: btn_click(5))
btn_6 = Button(root, text="6", padx=40, pady=20, command=lambda: btn_click(6))
btn_7 = Button(root, text="7", padx=40, pady=20, command=lambda: btn_click(7))
btn_8 = Button(root, text="8", padx=40, pady=20, command=lambda: btn_click(8))
btn_9 = Button(root, text="9", padx=40, pady=20, command=lambda: btn_click(9))
btn_add = Button(root, text="+", padx=39, pady=20, command=btn_add)
btn_equal = Button(root, text="=", padx=91, pady=20, command=btn_equal)
btn_clear = Button(root, text="C", padx=79, pady=20, command=btn_clear)
btn_subtract = Button(root, text="-", padx=41, pady=20, command=btn_subtract)
btn_multiply = Button(root, text="*", padx=41, pady=20, command=btn_multiply)
btn_divide = Button(root, text="/", padx=41, pady=20, command=btn_divide)

#put the btns on the screen
btn_0.grid(row=4, column=0)

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_add.grid(row=5, column=0)
btn_equal.grid(row=5, column=1, columnspan=2)
btn_clear.grid(row=4, column=1, columnspan=2)

btn_subtract.grid(row=6, column=0)
btn_multiply.grid(row=6, column=1)
btn_divide.grid(row=6, column=2)

root.mainloop()