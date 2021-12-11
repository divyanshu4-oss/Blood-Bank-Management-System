# Importing
import sqlite3
from itertools import count, cycle
from imp import reload
from tkinter import Tk, StringVar, messagebox, ttk, END, GROOVE, Entry, Label, Frame
from tkinter import *
from PIL import ImageTk,Image

root_viewall = Tk() 
root_viewall.title("VIEW ALL")                  # set title
root_viewall.iconbitmap('images\\icon1.ico')    # set icon
root_viewall.configure(bg='#f1053c')            # set bg color
root_viewall.geometry("1199x600+100+50")        # set geometry

root_viewall.resizable(False, False)  # Disable the resizable Property

# Menu Functions
def back():
    root_viewall.destroy()
    import page2
    reload(page2)
def searh():
    root_viewall.destroy()
    import SearchDonarDetail
    reload(SearchDonarDetail)
def update():
    root_viewall.destroy()
    import Update_DonarDetail
    reload(Update_DonarDetail)
def delete():
    root_viewall.destroy()
    import DeleteDonarDetail
    reload(DeleteDonarDetail)

# Create Menubar
menubar = Menu(root_viewall)
root_viewall.config(menu=menubar)
user_menu = Menu(menubar, tearoff=0)

# add menu items to the File menu
menubar.add_cascade(label='BACK',command=back)
menubar.add_cascade(label='SEARCH',command=searh)
menubar.add_cascade(label='UPDATE',command=update)
menubar.add_cascade(label='DELETE',command=delete)
menubar.add_cascade(label='EXIT',command=root_viewall.destroy)

# View Function
def viewall_record():
    import dbconnect
    conn = dbconnect.getsqliteconnection()    # Connect to sqlite database
    try:
        cur = conn.cursor()
        cur.execute("select * from Donar_detail")
        allrows = cur.fetchall()
        print(allrows)
        #print(cur.description)
        field_names = [i[0] for i in cur.description]
        print(field_names)
        if len(allrows) > 0:
            rowno = 0
            for x in field_names:
                e = Entry(frame, width=12, foreground='black',font=("bold",10),borderwidth=10)
                e.grid(row=rowno,column=0)
                rowno = rowno +1
                e.insert(END, x)
                e.configure(state="readonly")

            j = 1  # row value inside the loop
            for userinfo_record in allrows:
                for i in range(len(userinfo_record)):
                    e = Entry(frame, width=12, foreground='blue',borderwidth=10)
                    e.grid(row=i, column=j)
                    e.insert(END, userinfo_record[i])
                    e.configure(state="readonly")

                    # e = Label(root_search, width=10, text=userinfo_record[j],
                    #           borderwidth=2, relief='ridge', anchor="w")
                    # e.grid(row=i, column=j)
                j = j + 1
    except sqlite3.Error as error:
        print("Problem with SQlite table", error)
    finally:
        if conn:
            conn.commit()
            conn.close()
            print("The SQLite connection is closed")
#--------Button-------------------------->
b1 = Button(root_viewall, text="VIEW ALL DONAR DETAIL",command=viewall_record, foreground="#f1053c", activebackground="orange",bg='white', width=25, height=1, font=("times new roman", 14, "bold")).place(x=730, y=100)

frame = Frame(root_viewall)
frame.place(x=550, y=200)

#------------------GIF CLass----------------------------------->
class ImageLabel(Label):
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

# Load GIF
lbl = ImageLabel(root_viewall)
lbl.pack()
lbl.load('images\\bloodbottle.gif')
lbl.place(x=0, y =0,height=580, width=550)

# mainloop() is used to load the GUI Window
root_viewall.mainloop()