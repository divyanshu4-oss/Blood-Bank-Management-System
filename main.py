from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
root=Tk()
root.title("Blood Bank Management System")   # Set Title
root.geometry("1199x600+100+50")             # Set Geometry
root.resizable(False,False)                  # Disable the resizable Property
root.iconbitmap('images\\icon1.ico')         # Set Icon

# ----BackGround Image---->
img = Image.open("images\\admin.png")
img = img.resize((550,620))
my =ImageTk.PhotoImage(img)
label = Label(image=my).place(x=650,y=0)
root.configure(bg="#f1053c")
def home_page():
    root.destroy()
    import index1

# create a Menubar
menubar = Menu(root)
root.config(menu=menubar)
user_menu = Menu(menubar, tearoff=0)
# add menu items to the File menu
menubar.add_cascade(label='HOME', command=home_page)

# Login Class
class Login:
    def __init__(self,root):
        self.root=root
        #----Frame----------->
        Frame_login=Frame(self.root,bg="#e6acba",highlightthickness=5,highlightbackground="white")
        Frame_login.place(x=70,y=40,height=510,width=500)
        

        title=Label(Frame_login,text="Login Here",font=("times new roman",35,"bold"),fg="#C70039",bg="white").place(x=80,y=30)
        desc=Label(Frame_login,text="Admin Login Area",font=("times new roman",15,"bold"),fg="#C70039",bg="white").place(x=80,y=100)

        lb1_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="darkgray",bg="white").place(x=80,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=80,y=170,width=350,height=35)

        lb2_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="darkgray",bg="white").place(x=80,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),show="*" ,bg="lightgray")
        self.txt_pass.place(x=80,y=240,width=350,height=35)

        forget_btn=Button(Frame_login,text="Forget Password?",cursor="hand2",bg="white",bd=0,fg="#C70039",font=("times new roman",12)).place(x=80,y=280)
        login_btn=Button(self.root,command=self.login_function,cursor="hand2",text="Login",bg="#C70039",fg="white",font=("times new roman",20)).place(x=195,y=527,width=180,height=40)
    
    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get=="":
            messagebox.showerror("Error","All fields are required !",parent=self.root)
        elif self.txt_pass.get()=="12345" and self.txt_user.get()=="admin":
            self.root.destroy()
            import page2
        else:
            self.txt_pass.delete(0,END)
            self.txt_user.delete(0,END)
            messagebox.showerror("Error","Invalid Username/Password !",parent=self.root) 
obj=Login(root)
root.mainloop()    
























# from tkinter import *
# from PIL import ImageTk
# from tkinter import messagebox
# class Login:
#     def __init__(self,root):
#         self.root=root
#         self.root.title("Blood Bank Management System")
#         self.root.geometry("1199x600+100+50")
#         self.root.resizable(False,False)
#         #----BG Image---->
#         self.bg= ImageTk.PhotoImage(file="images\\main.jpg")
#         self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

#         #----Frame----------->
#         Frame_login=Frame(self.root,bg="white")
#         Frame_login.place(x=150,y=150,height=340,width=500)
        

#         title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=30)
#         desc=Label(Frame_login,text="Admin Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)

#         lb1_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="darkgray",bg="white").place(x=90,y=140)
#         self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
#         self.txt_user.place(x=90,y=170,width=350,height=35)

#         lb2_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="darkgray",bg="white").place(x=90,y=210)
#         self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
#         self.txt_pass.place(x=90,y=240,width=350,height=35)

#         forget_btn=Button(Frame_login,text="Forget Password?",cursor="hand2",bg="white",bd=0,fg="#d77337",font=("times new roman",12)).place(x=90,y=280)
#         login_btn=Button(self.root,command=self.login_function,cursor="hand2",text="Login",bg="#d77337",fg="white",font=("times new roman",20)).place(x=300,y=470,width=180,height=40)
    
#     def login_function(self):
#         if self.txt_pass.get()=="" or self.txt_user.get=="":
#             messagebox.showerror("Error","All fields are required !",parent=self.root)
#         elif self.txt_pass.get()=="12345" and self.txt_user.get()=="admin":
#             self.root.destroy()
#             import page2
#         else:
#             self.txt_pass.delete(0,END)
#             self.txt_user.delete(0,END)
#             messagebox.showerror("Error","Invalid Username/Password !",parent=self.root) 
# root=Tk()
# obj=Login(root)
# root.mainloop()    