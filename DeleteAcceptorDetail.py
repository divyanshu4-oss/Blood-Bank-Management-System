import sqlite3
from imp import reload
from tkinter import Tk, StringVar, messagebox, ttk, END, GROOVE, Entry, Label, Frame
from tkinter import *
from PIL import ImageTk,Image
root_del = Tk()

# title() method is used to change the title
root_del.title("SEARCHING")
root_del.iconbitmap('images\\icon1.ico')

# set center screen window with following coordination
root_del.geometry("1199x600+100+50")
def back():
    root_del.destroy()
    import viewallreceiver
    reload(viewallreceiver)
    # create a Menubar
menubar = Menu(root_del)
root_del.config(menu=menubar)
user_menu = Menu(menubar, tearoff=0)
# add menu items to the File menu
menubar.add_cascade(label='BACK',command=back)

# Disable the resizable Property
root_del.resizable(False, False)
root_del.configure(bg="#f1053c")
img1 = Image.open("images\\donregis.png")
img1 = img1.resize((600,670))
my1 =ImageTk.PhotoImage(img1)
label = Label(image=my1).place(x=600,y=0)

# img2 = Image.open("images\\recregis.jpg")
# img2 = img2.resize((600,700))
# my2 =ImageTk.PhotoImage(img2)
# label2 = Label(image=my2).place(x=0,y=0)

email = StringVar()

def delete_record():
    print(email.get())
    if email.get() == "":
        messagebox.showerror("Error !", "Email Fields are Required !")
    else:
        import dbconnect

        # Connect to sqlite database
        conn = dbconnect.getsqliteconnection()
        try:
            cur = conn.cursor()
            cur.execute("delete from Receiver_detail where Emailid=?", (email.get(),))

            if cur.rowcount == 0:
                txt_email.delete(0, END)
                messagebox.showerror("Error !", "Invalid Email ! Try with another one.")
            else:
                messagebox.showinfo("Info !", "Record Deleted")
        except sqlite3.Error as error:
                print("Problem with SQlite table", error)
        finally:
            if conn:
                conn.commit()
                conn.close()
                print("The SQLite connection is closed")

def home_page():
    root_del.destroy()
    import index1
    reload(index1)


title = Label(root_del, text="DELETE  RECEIVER  BY  EMAIL", font=("times new roman", 20, "bold"), foreground="white",bg="#f1053c")
title.place(x=80, y=30)

# --------First Row
l_name = Label(root_del, text="EMAIL ID", font=("times new roman", 15, "bold"), foreground="white",bg="#f1053c")
l_name.place(x=50, y=100)

txt_email = Entry(root_del, textvar=email, font=("times new roman", 15,))
txt_email.place(x=200, y=100, width=250)

# -------8th Row
# Create style Object
style = ttk.Style()
style.configure('TButton', font=('calibri', 10, 'bold'), foreground='#a81829')
reg_btn = ttk.Button(root_del, text='DELETE', style='TButton', command=delete_record)
reg_btn.place(x=280, y=140)



# mainloop() is used to load the GUI Window
root_del.mainloop()