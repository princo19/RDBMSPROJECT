from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class Login():
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        
        
        self.bg_icon=ImageTk.PhotoImage(file="bg.jpg")
        self.user_icon=PhotoImage(file="main.png")
        self.pass_icon=PhotoImage(file="pass.png")
        self.logo_icon=ImageTk.PhotoImage(file="user.jpg")
        self.uname=StringVar()
        self.pass_=StringVar()
        
        bg_lbl=Label(self.root,image=self.bg_icon).pack()
        
        title=Label(self.root,text="Welcome To Student Database",font=("times new roman",40,"bold"),bg="yellow",fg="blue",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
         
        
        Login_win=Frame(self.root,bg="white")
        Login_win.place(x=400,y=150)
        logolbl=Label(Login_win,image=self.logo_icon,bd=0)
        logolbl.grid(row=0,columnspan=3,pady=20)
        
        lbluser=Label(Login_win,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_win,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)
        
        lblpass=Label(Login_win,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(Login_win,bd=5,textvariable=self.pass_,show='*',relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)
         
        btn_log=Button(Login_win,text="Login",width=15,command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)

        
        
    def login(self):
        def is_valid_password(password):
            import hashlib
            password_hash = hashlib.sha256(password.encode("utf=8")).hexdigest()
            return password_hash == "0300dc429eeb82775c426d87a5fd72c1bba7a35f56a4804df8b3c35c38df6813"
        
        if self.uname.get()=="" or self.pass_.get()=="" :
            messagebox.showerror("Error","All fields are required!!")
        elif self.uname.get()=="ACET" and is_valid_password(self.pass_.get()):
            messagebox.showinfo("Successfull",f"Welcome {self.uname.get()}")  
            self.pass_.set("")
            self.Student1()
        else:
            messagebox.showerror("Error","Invalid Username or Password")
            print('invalid')


    def Student1(self):
        from pk import Student
        root4=Toplevel()
        ob4=Student(root4)
        root4.mainloop()

        
root=Tk()
obj=Login(root)
root.mainloop()
