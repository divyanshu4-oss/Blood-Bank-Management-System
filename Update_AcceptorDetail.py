# Importing
import sqlite3
from imp import reload
from tkinter import Tk, StringVar, messagebox, ttk, END, IntVar, DISABLED, NORMAL
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Registration Window")     # set title
root.iconbitmap('images\\icon1.ico')  # set icon
root.configure(bg='#f1053c')          # set bg color
root.geometry("1199x600+100+50")      # set geometry

# Menu Function


def home_page():
    root.destroy()
    import viewallreceiver
    reload(viewallreceiver)


# create a Menubar
menubar = Menu(root)
root.config(menu=menubar)
user_menu = Menu(menubar, tearoff=0)
# add menu items to the File menu
menubar.add_cascade(label='BACK', command=home_page)

root.resizable(False, False)  # Disable the resizable Property

# Background Image
img1 = Image.open("images\\donregis.png")
img1 = img1.resize((600, 670))
my1 = ImageTk.PhotoImage(img1)
label = Label(image=my1).place(x=600, y=0)

# Create Variables
email = StringVar()
mobile = StringVar()
fullname = StringVar()
bloodunit = StringVar()

# Clear Form Data After Update


def clear_data():
    txt_email.delete(0, END)
    txt_mobile.delete(0, END)
    txt_name.delete(0, END)
    txt_blood.delete(0, END)

# Update Function


def update_record():
    print(email.get(), mobile.get(), fullname.get(), bloodunit.get())

    if email.get() == "" or mobile.get() == "" or fullname.get() == "" or bloodunit.get() == "":
        messagebox.showerror("Error !", "All Fields are Required !")
    else:
        import dbconnect
        conn = dbconnect.getsqliteconnection()  # Connect to sqlite database
        try:
            cur = conn.cursor()
            cur.execute(
                "select * from Receiver_detail where Emailid=?", (email.get(),))
            row = cur.fetchone()
            if row is None:
                txt_email.delete(0, END)
                messagebox.showerror("Error !", "INVALID Email !")
            else:
                cur.execute('update Receiver_detail set Fullname = ?, MobileNo = ?, Blood_unit = ? where Emailid = ?',
                            (fullname.get(), mobile.get(), bloodunit.get(), email.get()))
                conn.commit()
                messagebox.showinfo("Success !", "UPDATE Completed !")
                clear_data()
        except sqlite3.Error as error:
            print("Problem with SQlite table", error)
        finally:
            if conn:
                conn.close()
                print("The SQLite connection is closed")


title = Label(root, text="UPDATE RECEIVER DETAILS", font=(
    "times new roman", 20, "bold"), foreground="white", bg="#f1053c")
title.place(x=100, y=30)

# --------1st Row
l_email = Label(root, text="EMAIL ID", font=("times new roman",
                15, "bold"), foreground="white", bg="#f1053c")
l_email.place(x=50, y=100)
txt_email = Entry(root, textvar=email, font=("times new roman", 15,))
txt_email.place(x=220, y=100, width=250)

# --------2nd Row
l_name = Label(root, text="FULL NAME", font=("times new roman",
               15, "bold"), foreground="white", bg="#f1053c")
l_name.place(x=50, y=140)
txt_name = Entry(root, textvar=fullname, font=("times new roman", 15))
txt_name.place(x=220, y=140, width=250)

# ---------3rd Row
l_mobile = Label(root, text="MOBILE NO.", font=(
    "times new roman", 15, "bold"), foreground="white", bg="#f1053c")
l_mobile.place(x=50, y=180)
txt_mobile = Entry(root, textvar=mobile, font=("times new roman", 15))
txt_mobile.place(x=220, y=180, width=250)

# ---------4th Row
l_blood = Label(root, text="BLOOD UNIT", font=(
    "times new roman", 15, "bold"), foreground="white", bg="#f1053c")
l_blood.place(x=50, y=220)
txt_blood = Entry(root, textvar=bloodunit, font=("times new roman", 15))
txt_blood.place(x=220, y=220, width=250)

# --------Button-------------------------->
b1 = Button(root, text="UPDATE", command=update_record, foreground="#f1053c", activebackground="orange",
            bg='white', width=10, height=1, font=("times new roman", 14, "bold")).place(x=280, y=266)

# mainloop() is used to load the GUI Window
root.mainloop()
