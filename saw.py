from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage


admin_window = Tk()
icon_image = PhotoImage(file="hams.ico")
admin_window.iconphoto(True, icon_image)
admin_window.title("Admin Log In")
admin_window.geometry("350x240")
admin_window.configure(bg="coral1")
admin_window.resizable(False,False)

############################---------------------------------------------------------
def admin():
    username=user.get()
    password=code.get()

    if (username=="" or password==" "):
        messagebox.showerror("Invalid","Blank Not Allowed")
    elif (username=="Admin" and password=="admin"):
        messagebox.showinfo("Success","Log in Succesfully")
        admin_window.destroy()
        import add
    else:
        messagebox.showerror("","Incorrect Username or Password")

def show_password():
    if code.cget("show") == "*":
        code.config(show="")
    else:
        code.config(show="*")
############################---------------------------------------------------------
frame=Frame(admin_window,width=350,height=350,bg="coral1")
frame.place(x=50,y=10)

heading=Label(admin_window,text="Admin",fg="black",bg="coral1",font=("times new roman",24,"bold"))
heading.place(x=120,y=25)
############################---------------------------------------------------------
def on_enter(e):
    user.delete(0,"end")
def on_leave(e):
    name=user.get()
label=Label(frame,text="UserName",fg="black",bg="coral1",font=("times new roman",9))
label.place(x=0,y=58)
user = Entry(frame,width=15,fg="black",border=1,bg="white",font=("times new roman",11))
user.place(x=65,y=60)
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)
############################---------------------------------------------------------
def on_enter(e):
    code.delete(0,"end")
def on_leave(e):
    name=code.get()
label=Label(frame,text="Password",fg="black",bg="coral1",font=("times new roman",9))
label.place(x=5,y=88)
code = Entry(frame,width=15,fg="black",border=1,bg="white",font=("times new roman",11),show="*")
code.place(x=65,y=90)
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)
############################---------------------------------------------------------
check_button=Checkbutton(admin_window,cursor="hand2",bg="coral1",text="Show password",font=("times new roman",10),command=show_password)
check_button.place(x=110,y=140)

log_in=Button(frame,width=10,pady=7,text="Log In",bg="#57a1f8",cursor="hand2",fg="white",font=("times new roman",10),border=0,command=admin)
log_in.place(x=80,y=170)

admin_window.mainloop()