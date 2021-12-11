# Importing
from tkinter import LEFT, RIGHT, TOP, BOTTOM, Tk, Button,Toplevel
from tkinter.font import Font
from tkinter import*
import sqlite3
from imp import reload
from tkinter import Tk, StringVar, ttk, END, IntVar, DISABLED, NORMAL
from PIL import ImageTk,Image
from tkinter import messagebox

def page_2():
    window = Tk()
    window.title("Blood Bank Management System")
     
# set center screen window with following coordination
    window.geometry("1199x600+100+50")
    window.iconbitmap('images\\icon1.ico')
    window.configure(bg="#f1053c")
    window.resizable(False,False)                  # Disable the resizable Property
# Menu Functions
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

    img1 = Image.open("images\\donregis.png")
    img1 = img1.resize((600,630))
    my1 =ImageTk.PhotoImage(img1)
    label = Label(image=my1).place(x=600,y=0)

# define font
    myFont = Font(family='Courier', size=15, weight='bold')

# Button Functions
    def donarCall():
        window.destroy()
        import viewalldonar
        viewalldonar.viewall_record()

    def accepterCall():
        window.destroy()
        import viewallreceiver
        viewallreceiver.viewall_record()
    def bloodCall():
        window.destroy()
        import ViewBloodDetail
        ViewBloodDetail.viewall_record()

# Buttons
    b1 = Button(window, text="DONAR DEATILS",command=donarCall, foreground="#f1053c", activebackground="orange",bg='white', width=40, height=2, font=("times new roman", 10, "bold")).place(x=120, y=200)
    b2 = Button(window, text="RECEIVER DETAILS",command=accepterCall, foreground="#f1053c", activebackground="orange",bg='white', width=40, height=2,font=("times new roman", 10, "bold")).place(x=120, y=260)
    b3 = Button(window, text="CHECK BLOOD AVAILABILITY",command=bloodCall, foreground="#f1053c" , activebackground="orange", bg='white', width=40, height=2,font=("times new roman", 10, "bold")).place(x=120, y=320)

# apply font to the button label
#b3['font'] = myFont


# b1.pack(side=LEFT)
# b2.pack(side=RIGHT)
# b3.pack(side=TOP)
# b4.pack(side=BOTTOM)
    
    window.mainloop()
page_2()




