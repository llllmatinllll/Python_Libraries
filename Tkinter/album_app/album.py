from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Tkinter')

img1 = ImageTk.PhotoImage(Image.open('images/1.jpg'))
img2= ImageTk.PhotoImage(Image.open('images/2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('images/3.jpg'))
img4 = ImageTk.PhotoImage(Image.open('images/4.jpg'))
img5 = ImageTk.PhotoImage(Image.open('images/5.jpg'))
img6 = ImageTk.PhotoImage(Image.open('images/6.jpg'))
img7 = ImageTk.PhotoImage(Image.open('images/7.jpg'))
img8 = ImageTk.PhotoImage(Image.open('images/8.jpg'))

img_list = [0, img1, img2, img3, img4, img5, img6, img7, img8]

show = Label(image=img_list[2])
show.grid(row=0, column=0, columnspan=3)

def forward(img_n):
    global show
    global btn_back
    global btn_forward
    
    show.grid_forget()
    show = Label(image=img_list[img_n+1])
    print(img_n)
    btn_forward = Button(root, text=">>", command=lambda: forward(img_n+1))
    btn_back = Button(root, text="<<", command=lambda:back(img_n-1))
    
    if img_n == 7:
        btn_forward = Button(root, text=">>", state=DISABLED)
    
    show.grid(row=0, column=0, columnspan=3)
    btn_forward.grid(row=1, column=2)
    btn_back.grid(row=1, column=0)

def back(img_n):
    global show
    global btn_back
    global btn_forward
    
    show.grid_forget()
    show = Label(image=img_list[img_n-1])
    print(img_n)
    btn_forward = Button(root, text=">>", command=lambda: forward(img_n+1))
    btn_back = Button(root, text="<<", command=lambda:back(img_n-1))
    
    if img_n == 3:
        btn_back = Button(root, text="<<", state=DISABLED)

    show.grid(row=0, column=0, columnspan=3)
    btn_forward.grid(row=1, column=2)
    btn_back.grid(row=1, column=0)

btn_back = Button(root, text="<<", command=lambda:back(3))
btn_exit = Button(root, text="Exit", command=root.quit)
btn_forward = Button(root, text=">>", command=lambda: forward(3))

btn_back.grid(row=1, column=0)
btn_exit.grid(row=1, column=1)
btn_forward.grid(row=1, column=2)


root.mainloop()