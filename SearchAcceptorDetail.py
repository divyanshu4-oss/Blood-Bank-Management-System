# Importing
import sqlite3
from imp import reload
from tkinter import Tk, StringVar, messagebox, ttk, END, GROOVE, Entry, Label, Frame
from tkinter import *
from PIL import Image, ImageTk

root_search = Tk()
root_search.title("SEARCHING")                 # set Title
root_search.iconbitmap('images\\icon1.ico')    # set icon
root_search.geometry("1199x600+100+50")        # set center screen window with following coordination
root_search.configure(bg="#f1053c")            # BackGround Color

# Menu Function
def back():
    root_search.destroy()
    import viewallreceiver
    reload(viewallreceiver)

# create a Menubar
menubar = Menu(root_search)
root_search.config(menu=menubar)
user_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='BACK',command=back)  # add menu items to the File menu

root_search.resizable(False, False)             # Disable the resizable Property

# BackGround Image
img1 = Image.open("images\\donregis.png")
img1 = img1.resize((600,670))
my1 =ImageTk.PhotoImage(img1)
label = Label(image=my1).place(x=600,y=0)

fullname = StringVar()     # Create Variable

# Search Function
def search_record():
    print(fullname.get())
    clear_frame()
    if fullname.get() == "":
        messagebox.showerror("Error !", "Email Fields are Required !")
    else:
        import dbconnect
        conn = dbconnect.getsqliteconnection()  # Connect to sqlite database
        try:
            cur = conn.cursor()
            cur.execute("select * from Receiver_detail where Fullname=?", (fullname.get(),))
            allrows = cur.fetchall()
            print(allrows)
            #print(cur.description)
            field_names = [i[0] for i in cur.description]
            print(field_names)
            if len(allrows) > 0:
                rowno = 0
                for x in field_names:
                    e = Entry(frame, width=10, foreground='black',borderwidth=10)
                    e.grid(row=rowno, column=0)
                    rowno = rowno+1
                    e.insert(END, x)
                    e.configure(state="readonly")

                j = 1  # row value inside the loop
                for userinfo_record in allrows:
                    for i in range(len(userinfo_record)):
                        e = Entry(frame, width=10, foreground='blue',borderwidth=10)
                        e.grid(row=i, column=j)
                        e.insert(END, userinfo_record[i])
                        e.configure(state="readonly")

                        # e = Label(root_search, width=10, text=userinfo_record[j],
                        #           borderwidth=2, relief='ridge', anchor="w")
                        # e.grid(row=i, column=j)
                    j = j + 1
            else:
                txt_fullname.delete(0, END)
                messagebox.showerror("ERROR !", "NOT FOUND !")

        except sqlite3.Error as error:
                print("Problem with SQlite table", error)
        finally:
            if conn:
                conn.commit()
                conn.close()
                print("The SQLite connection is closed")

def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()

title = Label(root_search, text="SEARCH  RECEIVER  DETAILS ", font=("times new roman", 20, "bold"), foreground="white",bg="#f1053c")
title.place(x=120, y=30)

# --------First Row
l_name = Label(root_search, text="FULL NAME", font=("times new roman", 15, "bold"), foreground="white",bg="#f1053c")
l_name.place(x=50, y=100)
txt_fullname = Entry(root_search, textvar=fullname, font=("times new roman", 15,))
txt_fullname.place(x=220, y=100, width=250)

# Create style Object
style = ttk.Style()
style.configure('TButton', font=('calibri', 10, 'bold'), foreground='#a81829')
reg_btn = ttk.Button(root_search, text='SEARCH', style='TButton', command=search_record)
reg_btn.place(x=300, y=140)

frame = Frame(root_search)
frame.place(x=30, y=240)
# mainloop() is used to load the GUI Window
root_search.mainloop()

