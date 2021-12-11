# importing
import tkinter as tk
from itertools import count, cycle
from tkinter import*
from tkinter import ttk # pip3 install pillow
from distutils import command
from tkinter import Tk, Menu, Label, Toplevel, Canvas, BOTH, messagebox
from PIL import ImageTk, Image
from imp import reload


root = tk.Tk()
root.title("Blood Bank Management System")       # Set Title
root.iconbitmap('images\\icon1.ico')             # Set Icon
root.geometry("1199x600+100+50")                 # set center screen window with following coordination
root.resizable(False, False)                     # Disable the resizable Property

# Menu Function
def about():
    root.destroy()
    import about
    
# create a Menubar
menubar = Menu(root)
root.config(menu=menubar)
user_menu = Menu(menubar, tearoff=0)
# add menu items to the File menu
menubar.add_cascade(label='EXIT', command=root.destroy)
menubar.add_cascade(label="ABOUT", command=about)  
root.configure(bg="#f1053c")

# # my_img = ImageTk.PhotoImage(Image.open("images\homeback.png"))
# # Create a canvas
# canvas=Canvas(root, width=400, height=400)
# #canvas.configure(bg)
# canvas.pack(expand=False, fill=BOTH)
# # Add the image in the canvas
# # canvas.create_image(0, 0, image=my_img, anchor="nw")

# # Add a text in canvas
# canvas.create_text(195, 50,fill="#f1053c", text="BLOOD", font= ('Courier 50 bold'))
# canvas.create_text(175, 120,fill="#f1053c", text="BANK", font= ('Courier 50 bold'))
# canvas.create_text(295, 190,fill="#f1053c", text="MANAGEMENT", font= ('Courier 50 bold'))
# canvas.create_text(208, 260,fill="#f1053c", text="SYSTEM", font= ('Courier 50 bold'))

# Labels
label1 = Label(root, text="BLOOD", font= ('"Times New Roman" 50 bold'),fg="white",bg="#f1053c").place(x=155,y=50)
label2 = Label(root, text="BANK", font= ('"Times New Roman" 50 bold'),fg="white",bg="#f1053c").place(x=155,y=120)
label3 = Label(root, text="MANAGEMENT", font= ('"Times New Roman" 50 bold'),fg="white",bg="#f1053c").place(x=155,y=190)
label4 = Label(root, text="SYSTEM", font= ('"Times New Roman" 50 bold'),fg="white",bg="#f1053c").place(x=155,y=260)

# Button Functions
def admin_login_window():
    root.destroy()
    import main
    #reload(main)
def donar_require():
    root.destroy()
    import doAcc
    reload(doAcc)

# Buttons
b1 = Button(root, text="USER",command=donar_require, foreground="#f1053c", activebackground="orange",bg='white', width=25, height=1, font=("times new roman", 14, "bold")).place(x=120, y=380)
b2 = Button(root, text="ADMIN LOGIN",command=admin_login_window, foreground="#f1053c", activebackground="orange",bg='white', width=25, height=1,font=("times new roman", 14, "bold")).place(x=420, y=380)

#------------------GIF CLass----------------------------------->
class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

# Load GIF :
lbl = ImageLabel(root)
lbl.pack()
lbl.load('images\\emoji.gif')
lbl.place(x=720, y = 50,height=300, width=420)

# lbl2 = ImageLabel(root)
# lbl2.pack()
# lbl2.load('images\\tenor.gif')
# lbl2.place(x=720, y = 150,height=300)


root.mainloop()