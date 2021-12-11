# Importing
import tkinter as tk
from tkinter import *
from imp import reload
from PIL import ImageTk, Image
from tkinter.font import Font
from tkinter import Tk, StringVar, messagebox, ttk, END, IntVar, DISABLED, NORMAL
import sqlite3

root = tk.Tk()
root.title("Donar")               # set title
root.geometry("1199x600+100+50")  # set geometry
root.resizable(False, False)      # Disable the resizable Property

# Background Image
img1 = Image.open("images\\donregis.png")
img1 = img1.resize((600,670))
my1 =ImageTk.PhotoImage(img1)
label1 = Label(image=my1).place(x=600,y=0)

root.configure(bg="#f1053c")    # set bg color

# Menu Function
def back():
    root.destroy()
    import ViewBloodDetail
    reload(ViewBloodDetail)

# Create Menu Bar
menubar = Menu(root)
root.config(menu=menubar)
user_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='BACK',command=back)   # add menu items to the File menu
bloodgroup = StringVar()                # Create Variable
conn = sqlite3.connect('bms.sqlite')    # Connect database 

#my_img = ImageTk.PhotoImage(Image.open("images\RedBloodCells.jpg"))
# Create a canvas
#canvas=Canvas(root, width=400, height=850)
#canvas.pack(expand=True, fill=BOTH)
# Add the image in the canvas
#canvas.create_image(0, 0, image=my_img, anchor="nw")


# Button Functions
def updateDonateBlood():
    print(txt_Unit.get(), bloodgroup.get())
    cur = conn.cursor()
    cur.execute("update Blood_Stock set Unit = Unit + ? where BloodGroup = ?",(txt_Unit.get(), bloodgroup.get()))
    conn.commit()
    print(cur.rowcount)

def updateReceiveBlood():
    print(txt_Unit.get(), bloodgroup.get())
    cur = conn.cursor()
    cur.execute("update Blood_Stock set Unit = Unit - ? where BloodGroup = ?",(txt_Unit.get(), bloodgroup.get()))
    conn.commit()
    print(cur.rowcount)
    
blood_Group = Label(root, text="UPDATE BLOOD UNIT", font=("times new roman", 25, "bold"),fg="white",bg="#f1053c").place(x=110, y=20)

blood_Group = Label(root, text="BLOOD GROUP", font=("times new roman", 15, "bold"),fg="white",bg="#f1053c").place(x=80, y=100)
combo_bg = ttk.Combobox(root, textvariable=bloodgroup)
combo_bg['values'] = ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')
combo_bg.current(0) # Default INDIA WILL SELECTED
combo_bg.place(x=300, y=100, width=210)

blood_Unit = Label(root, text="BLOOD UNIT", font=("times new roman", 15, "bold"), fg="white",bg="#f1053c").place(x=80, y=140)
txt_Unit = Entry(root, font=("times new roman", 15))
txt_Unit.place(x=300, y=140, width=210)

# Buttons
b1 = Button(root, text="UPDATE DONATE BLOOD", foreground="#f1053c", activebackground="orange", bg='white', font=("times new roman", 14, "bold"), command=updateDonateBlood, cursor = "plus").place(x = 180, y = 210)
b2 = Button(root, text="UPDATE RECEIVER BLOOD", foreground="#f1053c", activebackground="orange", bg='white', font=("times new roman", 14, "bold"), command=updateReceiveBlood,  cursor = "plus").place(x = 180, y = 280)

root.mainloop()