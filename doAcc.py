# importing
from tkinter import LEFT, RIGHT, TOP, BOTTOM, Tk, Button,Toplevel
from tkinter.font import Font
from tkinter import*
import sqlite3
from imp import reload
from tkinter import Tk, StringVar, ttk, END, IntVar, DISABLED, NORMAL
from PIL import ImageTk,Image
from tkinter import messagebox

# Define Function and import in page2
def page_2():
    window = Tk()
    window.title("Blood Bank Management System")
     
# set center screen window with following coordination
    window.geometry("1199x600+100+50")
    window.iconbitmap('images\\icon1.ico')
    window.configure(bg="#f1053c")
    def home_page():
        window.destroy()
        import index1
        reload(index1)
# create a Menubar
    menubar = Menu(window)
    window.config(menu=menubar)
    user_menu = Menu(menubar, tearoff=0)

# add menu items to the File menu
    menubar.add_cascade(label='HOME',command=home_page)

# BackGround Image
    img1 = Image.open("images\\donregis.png")
    img1 = img1.resize((600,630))
    my1 =ImageTk.PhotoImage(img1)
    label = Label(image=my1).place(x=600,y=0)

# define font
    myFont = Font(family='Courier', size=15, weight='bold')

# Button Functions
    def regis_donar():
        window.destroy()
        import registrationdonar
        reload(registrationdonar)
    def regis_acceptor():
        window.destroy()
        import registrationacceptor
        reload (registrationacceptor)

# Buttons
    b1 = Button(window, text="DONAR REGISTRATION",command=regis_donar, foreground="#f1053c", activebackground="orange",bg='white', width=40, height=2, font=("times new roman", 10, "bold")).place(x=140, y=190)
    b2 = Button(window, text="RECEIVER REGISTRATION",command=regis_acceptor, foreground="#f1053c", activebackground="orange",bg='white', width=40, height=2, font=("times new roman", 10, "bold")).place(x=140, y=260)

    
    window.mainloop()
page_2()