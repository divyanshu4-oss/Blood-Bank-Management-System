# Importing
from tkinter import*
from distutils import command
from tkinter import Tk, Menu, Label
root = Tk()
root.title("Blood Bank Management System")
root.iconbitmap('images\\icon1.ico')
root.geometry("1199x600+100+50")

# Disable the resizable Property
root.resizable(False, False)

def back():
    root.destroy()
    import index1

# create a Menubar
menubar = Menu(root)
root.config(menu=menubar)
user_menu = Menu(menubar, tearoff=0)
# add menu items to the File menu
menubar.add_cascade(label='EXIT', command=root.destroy)
menubar.add_cascade(label="BACK", command=back)  
root.configure(bg="#f1053c")

label1 = Label(root, text="       ABOUT", font= ('"Times New Roman" 25 bold'),fg="white",bg="#f1053c").place(x=450,y=20)
label2 = Label(root, text="Blood bank management project is a useful application for organizations(managing blood bank) and the hospitals.\n We will be using Tkinter for GUI development and SQLITE\n for database management to implement this project.\n\nThe aim of the blood bank management system is to simplify and automate the process of searching for blood\n in case of emergency and maintain the records of blood donors and acceptors, recipients,\n and blood stocks in the bank.\nPROGRAMMING LANGUAGE USED: PYTHON 3.9\nGUI Creation: Tkinter\nIDE USED:  PyCharm\n Database: SQLite\nPROCESSOR :-  Intel i3 or i5 1.8 GHz.\nMOTHERBOARD  :- According to the processor requirement\nRAM :-  4GB.\nFREE DISK SPACE :-   100MB\n", font= ('"Times New Roman" 15 bold'),fg="white",bg="#f1053c").place(x=100,y=120)

root.mainloop()