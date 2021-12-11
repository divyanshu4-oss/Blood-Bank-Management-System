# Importing
from tkinter import*
import sqlite3
from PIL import ImageTk,Image,ImageDraw
from tkinter import Tk, StringVar,ttk, messagebox, END, IntVar, DISABLED, NORMAL
from imp import reload
from tkinter import messagebox,Canvas

root = Tk()
root.geometry("1199x600+100+50")
root.resizable(False,False)
root.title("REGISTRATION FORM OF DONAR")
root.iconbitmap('images\\icon1.ico')
root.configure(bg='#f1053c')

# BackGround Image
img = Image.open("images\\donregis.png")
img = img.resize((595,630))
my =ImageTk.PhotoImage(img)
label = Label(image=my).place(x=600,y=0)

# Menu Function
def home_page():
    root.destroy()
    import index1
    reload(index1)
# create a Menubar
menubar = Menu(root)
root.config(menu=menubar)
user_menu = Menu(menubar, tearoff=0)
# add menu items to the File menu
menubar.add_cascade(label='HOME',command=home_page)

# Create Variables        
Fullname = StringVar()
email = StringVar()
mobile = StringVar()
address = StringVar()
gender = StringVar()
age = StringVar()
blood_group = StringVar()
blood_unit = StringVar()
chktc = IntVar()

# Function to Clear Form After Submit
def clear_data():
    entry_1.delete(0, END)
    entry_1_1.delete(0, END)
    entry_2.delete(0, END)
    entry_2_1.delete(0, END)
    entry_2_3.delete(0, END)
    combo_gender.current(0)
    combo_blood.current(0)
    entry_6.delete(0, END)

def insert_record():
    print(Fullname.get(), email.get(), mobile.get(), address.get(), gender.get(), age.get() ,blood_group.get(), blood_unit.get())

    if Fullname.get() == "" or email.get() == "" or mobile.get() == "" or address.get() == "" or gender.get() == "" or age.get() == "" or blood_group.get() == "" or blood_unit.get() == "":
        messagebox.showerror("Error !", "All Fields are Required !")
    else:
        import dbconnect

        # Connect to sqlite database
        conn = dbconnect.getsqliteconnection()
        try:
            cur = conn.cursor()

            cur.execute("select * from Donar_detail where Emailid=?", (email.get(),))

            row = cur.fetchone()
            if row != None:
                entry_2_1.delete(0, END)
                messagebox.showerror("Error !", "Already Exists Email ! Try with another one.")
            # elif int(age.get()>=18 and age.get()<=65 :
            #     pass
            # else:
            #     print("\tYou cannot Donate!!!")
              
            # elif len(self.mobileno)==10 and self.mobileno.isdigit() :
            #     pass
            # else:
            #     print("\tEntered wrong number")    
            # elif(self.email.count('@')==1  and '.' in self.email ):
            #     pass
            else:
                print("\tPlease enter Valid email !!!") 
                query = ('insert into Donar_detail(Fullname, Emailid, MobileNo, Address, Gender, Age, Blood_group, Blood_unit)'
                         'values (:fname1, :email1, :mobile1, :addr1, :gender1, :age1, :bloodg, :bloodu);')
                params = {
                    'fname1': Fullname.get(),
                    'email1': email.get(),
                    'mobile1': mobile.get(),
                    'addr1': address.get(),
                    'gender1': gender.get(),
                    'age1': age.get(),
                    'bloodg': blood_group.get(),
                    'bloodu': blood_unit.get()
                        }

                conn.execute(query, params)
                conn.commit()
                messagebox.showinfo("Success !", "Registration Completed !")
                clear_data()
        except sqlite3.Error as error:
                print("Problem with SQlite table", error)
        finally:
            if conn:
                conn.close()
                print("The SQLite connection is closed")
     
# Function that checks chkbox is checked or not   
def isChecked():
        if chktc.get() == 1:
           reg_btn['state'] = NORMAL
           reg_btn.configure(text='Submit')
        elif chktc.get() == 0:
           reg_btn['state'] = DISABLED
           reg_btn.configure(text='Check T & C!')
    
label_0 = Label(root, text="REGISTRATION  FORM",font=("times new roman", 32, "bold"),fg="white",bg="#f1053c")
label_0.place(x=50,y=30)

label_1 = Label(root, text="PATIENT  NAME",font=("times new roman",15,"bold"),fg="white",bg="#f1053c")
label_1.place(x=80,y=110)
entry_1 = Entry(root,textvar=Fullname,width=32)
entry_1.place(x=270,y=110)

label_1_1 = Label(root, text="ADDRESS",font=("times new roman",15,"bold"),fg="white",bg="#f1053c")
label_1_1.place(x=80,y=140)
entry_1_1 = Entry(root,textvar=address,width=32)
entry_1_1.place(x=270,y=140)

label_2 = Label(root, text="MOBILE  NO",font=("times new roman",15,"bold"),fg="white",bg="#f1053c")
label_2.place(x=80,y=170)
entry_2 = Entry(root,textvar=mobile,width=32)
entry_2.place(x=270,y=170)

label_2_1 = Label(root, text="EMAIL",font=("times new roman",15,"bold"),fg="white",bg="#f1053c")
label_2_1.place(x=80,y=200)
entry_2_1 = Entry(root,textvar=email,width=32)
entry_2_1.place(x=270,y=200)

label_3 = Label(root,text="GENDER",font=("times new roman",15,"bold"),fg="white",bg="#f1053c")
label_3.place(x=80,y=230)
combo_gender = ttk.Combobox(root, textvariable=gender)
combo_gender['values'] = ('Male','Female','Transgender')
combo_gender.current(0) # Default 'Male' WILL SELECTED
combo_gender.place(x=270,y=230, width=200)

label_4 = Label(root, text="AGE",font=("times new roman",15,"bold"),fg="white",bg="#f1053c")
label_4.place(x=80,y=270)
entry_2_3 = Entry(root,textvar=age,width=32)
entry_2_3.place(x=270,y=270)

label_5 = Label(root, text="BlOOD  GROUP", font=("times new roman",15,"bold"),fg="white",bg="#f1053c")
label_5.place(x=80, y=310)
combo_blood = ttk.Combobox(root, textvariable=blood_group)
combo_blood['values'] = ('A+','B+','O+','A-','B-','AB+','AB-','O-')
combo_blood.current(0) # Default A+ WILL SELECTED
combo_blood.place(x=270, y=310, width=200)

label_6 = Label(root, text="BlOOD UNIT",font=("times new roman",15,"bold"),fg="white",bg="#f1053c")
label_6.place(x=80,y=340)
entry_6 =Entry(root,textvar=blood_unit,width=32)
entry_6.place(x=270,y=340)

# Chkbox
chk = Checkbutton(root, text="I Agree the Terms & Conditions",font=(("times new roman",15,"bold")),fg="white",bg="#f1053c", variable=chktc, onvalue=1, offvalue=0, command=isChecked)
chk.place(x=130, y=390)

# Style Button
style = ttk.Style()
style.configure('TButton',width=20 ) #foreground='white',bg='brown')
reg_btn = ttk.Button(root, text='Submit', style='TButton', state=DISABLED, command=insert_record)
reg_btn.place(x=200,y=450)
root.mainloop()
print("registration form  seccussfully created...")
