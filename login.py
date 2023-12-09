from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import PhotoImage
from PIL import ImageTk,Image



login_window = tk.Tk()
login_window.title("User Login")
login_window.geometry("565x500")
login_window.configure(bg="coral1")
login_window.resizable(False,False)
icon_image = PhotoImage(file="hams.ico")
login_window.iconphoto(True, icon_image)

############################---------------------------------------------------------
def login():
    username=user.get()
    password=code.get()

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="", 
        database="finalproj"
    )

    mycursor = conn.cursor()

    query = "SELECT * FROM data WHERE username = %s AND password = %s"
    values = (username, password)
    mycursor.execute(query, values)
    result = mycursor.fetchall()

    if result:
        messagebox.showinfo("Login", "Login Successfully!")
        login_window.destroy()
        import home
    else:
        messagebox.showerror("Login", "Invalid username or password")

    mycursor.close()
    conn.close()

def connect_database():
    if user.get()=="" or code.get()=="":
        messagebox.showerror("Error","All Fields are Required")
    else:
        try:
            conn=mysql.connector.connect(host="localhost",
                                user="root",
                                password="",
                                database="finalproj"
                            )
            mycursor=conn.cursor()
            mycursor.execute("insert into data (username,password) values (%s,%s)",(
                user.get(),
                code.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Sign Up Succesfully")
        except:
            messagebox.showerror("Error","Database Connectivity Issue, Please Try Again")
            return
        


def admin():
        login_window.destroy()
        import saw

def show_password():
    if code.cget("show") == "*":
        code.config(show="")
    else:
        code.config(show="*")

############################---------------------------------------------------------
frame=Frame(login_window,bg="coral1",width=350,height=350)
frame.place(x=50,y=10)
img= Image.open(r"hms.png")
bg_img= ImageTk.PhotoImage(img)
bg_lbl= Label(bg="coral1",image=bg_img)
bg_lbl.place(x=130, y=200)
heading=Label(frame,text="Log In",fg="black",bg="coral1",font=("times new roman",25,"bold"))
heading.place(x=180,y=50)

def on_enter(e):
    user.delete(0,"end")
def on_leave(e):
    name=user.get()
label=Label(frame,bg="coral1",text="UserName",fg="black",font=("times new roman",9))
label.place(x=95,y=120)
user = Entry(frame,width=20,fg="black",border=1,bg="white",font=("times new roman",11))
user.place(x=160,y=120)
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(width=295,height=2,bg="black").place(x=120,y=230)
############################---------------------------------------------------------
def on_enter(e):
    code.delete(0,"end")
def on_leave(e):
    name=code.get()
label=Label(frame,bg="coral1",text="Password",fg="black",font=("times new roman",9))
label.place(x=100,y=150)
code = Entry(frame,width=20,fg="black",border=1,bg="white",font=("times new roman",11),show="*")
code.place(x=160,y=150)
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

check_button=Checkbutton(login_window,bg="coral1",text="Show password",cursor="hand2",font=("times new roman",9),command=show_password)
check_button.place(x=230,y=190)
############################---------------------------------------------------------
Button(width=10,pady=7,text="Log In",bg="#57a1f8",fg="white",cursor="hand2",font=("times new roman",10),border=0,command=login).place(x=180,y=250)
Button(width=10,pady=7,text="Sign Up",border=0,bg="#57a1f8",cursor="hand2",fg="white",font=("times new roman",10),command=connect_database).place(x=300,y=250)
Button(width=10,pady=7,text="Admin",border=0,bg="#57a1f8",cursor="hand2",fg="white",font=("times new roman",10),command=admin).place(x=0,y=0)


#########################-------------------------------------------------------



login_window.mainloop()