from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox

import mysql.connector

def logout():
    management.destroy()
    import login

def srch():
    import date

management = Tk()
management.attributes("-fullscreen", True)

class Hospital:
    def __init__(self, management):
        management = management
        management.title("Hospital Management System")
        management.geometry("1000x500")
        management.resizable(False,False)


Email=StringVar()
Phone=StringVar()
DoctorID=StringVar()
DoctorName=StringVar()
Specialization=StringVar()
Status=StringVar()
Patients=StringVar()
combo_var = StringVar()

def on_combobox_change(event):
    selected_value = combo_var.get()

lbltitle=Label(management,
                       bd=8,
                       relief=RIDGE,
                       text="HOSPITAL MANAGEMENT ADMIN",
                       fg="blue",
                       bg="coral1",
                       font=("times new roman",30)
                       )
lbltitle.pack(side=TOP, fill=X)
###################------------DATA-----------#################

Dataframe=Frame(management,bg="coral1",bd=10,relief=RIDGE,padx=5)
Dataframe.place(x=0,y=65,width=1366,height=702,)


DataframeLeft=LabelFrame(Dataframe,bg="coral1",bd=5,relief=RIDGE,padx=5,
                         font=("times new roman",11,"bold"),text="Patient Appointment")
DataframeLeft.place(x=0,y=5,width=505,height=385)

DataframeRight=LabelFrame(Dataframe,bg="coral1",bd=5,relief=RIDGE,padx=5,
                         font=("times new roman",11,"bold"),text="Doctors")
DataframeRight.place(x=500,y=5,width=840,height=385)

BotFrame=LabelFrame(management,bd=7,bg="coral1",relief=RIDGE,font=("times new roman",11,"bold"),text="List of Appointment")
BotFrame.place(x=10,y=515,width=1345,height=240)

BttnFrame=Frame(management,bd=10,bg="coral1",relief=RIDGE)
BttnFrame.place(x=10,y=465,width=1345,height=55)

img= Image.open("hms.png")
bg_img= ImageTk.PhotoImage(img)
bg_lbl= Label(DataframeLeft,bg="coral1",image=bg_img)
bg_lbl.place(x=250, y=150)
###################------------DATALEFT-----------################
lbldoctid=Label(DataframeLeft,bg="coral1",font=("arial",11),text="Doctor ID:",padx=2,pady=4)
lbldoctid.grid(row=1,column=0)
txtdoctid=Entry(DataframeLeft,font=("arial",11),textvariable=DoctorID,width=20)
txtdoctid.grid(row=1,column=1)

lbldoctname=Label(DataframeLeft,bg="coral1",font=("arial",11),text="Doctor Name:",padx=2,pady=4)
lbldoctname.grid(row=2,column=0)
txtdoctname=Entry(DataframeLeft,font=("arial",11),textvariable=DoctorName,width=20)
txtdoctname.grid(row=2,column=1)

lblemail1=Label(DataframeLeft,bg="coral1",font=("arial",11),text="Email:",padx=2,pady=4)
lblemail1.grid(row=3,column=0)
txtemail1=Entry(DataframeLeft,font=("arial",11),textvariable=Email,width=20)
txtemail1.grid(row=3,column=1)

lblphone1=Label(DataframeLeft,bg="coral1",font=("arial",11),text="Phone Number:",padx=2,pady=4)
lblphone1.grid(row=4,column=0)
txtphone1=Entry(DataframeLeft,font=("arial",11),textvariable=Phone,width=20)
txtphone1.grid(row=4,column=1)

lblspecial=Label(DataframeLeft,bg="coral1",font=("arial",11),text="Specialization:",padx=2,pady=4)
lblspecial.grid(row=5,column=0)
txtspecial = ttk.Combobox(DataframeLeft, textvariable=Specialization,width=24, state='readonly')
txtspecial['values'] = ('Surgeon', 'Cardiologist','Psychiatrist','Pediatricians','Ophthalmologist','Neurosurgeons',
                        'Dermatologist','Endocrinologists','Hematologists','Physiatrists','Pulmonologists','Urologists',
                        'Podiatrists','Plastic Surgeons','Pathologists','Osteopaths','Nephrologists')
txtspecial.set('Surgeon') 
txtspecial.grid(row=5,column=1)
txtspecial.bind("<<ComboboxSelected>>", on_combobox_change)

lblstats=Label(DataframeLeft,bg="coral1",font=("arial",11),text="Status:",padx=2,pady=4)
lblstats.grid(row=6,column=0)
txtstats = ttk.Combobox(DataframeLeft, textvariable=Status,width=24, state='readonly')
txtstats['values'] = ('Available', 'NotAvailable')
txtstats.set('Available') 
txtstats.grid(row=6,column=1)
txtstats.bind("<<ComboboxSelected>>", on_combobox_change)
###################------------add-----------#################

def show_data():
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="finalproj")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from patient")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                list_table.delete(*list_table.get_children())
                for i in rows:
                    list_table.insert("",END,values=i)
                conn.commit()
                conn.close()

def doct_data():
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="finalproj")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from doctlist")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                doct_table.delete(*doct_table.get_children())
                for i in rows:
                    doct_table.insert("",END,values=i)
                conn.commit()
                conn.close()


###################------------SCROLLBAR-----------#################
scroll=ttk.Scrollbar(BotFrame,cursor="hand2",orient=VERTICAL)
list_table=ttk.Treeview(BotFrame,column=("patientid","patientname","email","phone","apptid","apptdate","doctorid"),xscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)

scroll=ttk.Scrollbar(command=list_table.yview)

list_table.heading("patientid",text="PatientID")
list_table.heading("patientname",text="PatientName")
list_table.heading("email",text="Email")
list_table.heading("phone",text="Phone#")
list_table.heading("apptid",text="Appt.ID")
list_table.heading("apptdate",text="Appt.Date")
list_table.heading("doctorid",text="DoctorID")

list_table["show"]="headings"

list_table.column("patientid",width=100)
list_table.column("patientname",width=100)
list_table.column("email",width=100)
list_table.column("phone",width=100)
list_table.column("apptid",width=100)
list_table.column("apptdate",width=100)
list_table.column("doctorid",width=100)

list_table.pack(fill=BOTH,expand=1)
show_data()

scroll_doct=ttk.Scrollbar(DataframeRight,cursor="hand2",orient=VERTICAL)
doct_table=ttk.Treeview(DataframeRight,column=("doctorid","doctorname","email","phone","special","stats"),xscrollcommand=scroll_doct.set)
scroll_doct.pack(side=RIGHT, fill=Y)

scroll_doct=ttk.Scrollbar(command=doct_table.yview)

doct_table.heading("doctorid",text="DoctorID")
doct_table.heading("doctorname",text="DoctorName")
doct_table.heading("email",text="Email")
doct_table.heading("phone",text="Phone#")
doct_table.heading("special",text="Specialization")
doct_table.heading("stats",text="Status")

doct_table["show"]="headings"

doct_table.column("doctorid",width=80,minwidth=80)
doct_table.column("doctorname",width=80,minwidth=80)
doct_table.column("email",width=80,minwidth=80)
doct_table.column("phone",width=80,minwidth=80)
doct_table.column("special",width=80,minwidth=80)
doct_table.column("stats",width=80,minwidth=80)

doct_table.pack(fill=BOTH,expand=1)
doct_data()

content = txtdoctname.get()
content = txtemail1.get()
content = txtphone1.get()
content = txtspecial.get()

######################-----------------Database--------------###################
def iAddDoct():
    if DoctorName.get() == "" or Email.get() == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        conn = mysql.connector.connect(host="localhost",user="root",password="",database="finalproj")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into doctlist (DoctorName,Email,Phone,Specialization,Status) values(%s,%s,%s,%s,%s)",(
                                                                            DoctorName.get(),
                                                                            Email.get(),
                                                                            Phone.get(),
                                                                            Specialization.get(),
                                                                            Status.get()
        ))
        conn.commit()
        show_data()
        doct_data()
        conn.close()
        messagebox.showinfo("Succes","Appointment has been recorded")

    txtdoctname.delete(0, "end")
    txtemail1.delete(0, "end")
    txtphone1.delete(0, "end")
    txtspecial.delete(0, "end")

def update():
    doctor_id = txtdoctid.get()
    doctor_name = txtdoctname.get()
    email = txtemail1.get()
    phone = txtphone1.get()
    special = txtspecial.get()
    stats = txtstats.get()
    

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="finalproj"
        )
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM doctlist WHERE DoctorID = %s", (doctor_id,))
        existing_patient = cursor.fetchone()

        if existing_patient:
            update_query = "UPDATE doctlist SET DoctorName=%s, Email=%s, Phone=%s,Specialization=%s, Status=%s WHERE DoctorID=%s"
            data = (doctor_name, email, phone, special, stats, doctor_id)
            cursor.execute(update_query, data)

            connection.commit()

            txtdoctname.delete(0, "end")
            txtdoctname.insert(0, doctor_name)

            txtemail1.delete(0, "end")
            txtemail1.insert(0, email)

            txtphone1.delete(0, "end")
            txtphone1.insert(0, phone)

            txtspecial.delete(0, "end")
            txtspecial.insert(0, special)

            txtstats.delete(0, "end")
            txtstats.insert(0, stats)

            messagebox.showinfo("Success", "Record updated successfully!")
            update_treeview()
        else:
            messagebox.showerror("Error", "Doctor ID does not exist!")

        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

def update_treeview():
    for row in doct_table.get_children():
        doct_table.delete(row)

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="finalproj"
        )
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM doctlist")
        doctors = cursor.fetchall()

        for doctor in doctors:
            doct_table.insert("", "end", values=doctor)

    except mysql.connector.Error as err:
        messagebox.showerror(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()

def dlt():
    doctor_id = txtdoctid.get()

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="finalproj"
        )
        cursor = connection.cursor()

        delete_query = "DELETE FROM doctlist WHERE DoctorID = %s"
        cursor.execute(delete_query, (doctor_id,))

        connection.commit()

        reset_auto_increment_query = "ALTER TABLE doctlist AUTO_INCREMENT = 1"
        cursor.execute(reset_auto_increment_query)

        connection.commit()

        messagebox.showinfo("Success", "Appointment deleted successfully!")
        update_treeview1()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        cursor.close()
        connection.close()

def update_treeview1():
    for row in doct_table.get_children():
        doct_table.delete(row)

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="finalproj"
        )
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM doctlist")
        doctors = cursor.fetchall()

        for doctor in doctors:
            doct_table.insert("", "end", values=doctor)

    except mysql.connector.Error as err:
        messagebox.showerror(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()


def listdoct(event=""):
        cursor_row=doct_table.focus()
        content=doct_table.item(cursor_row)
        row=content["values"]
        DoctorID.set(row[0])
        DoctorName.set(row[1])
        Email.set(row[2])
        Phone.set(row[3])
        Specialization.set(row[4])
        Status.set(row[5])
        

doct_table.bind("<ButtonRelease-1>",listdoct)

#######-------------------------Button---------------------------#######
Button(BttnFrame,width=10,pady=7,text="Logout",border=0,bg="#57a1f8",cursor="hand2",fg="white",command=logout).place(x=1245,y=0)
List=Button(BttnFrame,width=15,pady=7,text="Add Doctor",border=0,bg="#57a1f8",cursor="hand2",fg="white",command=iAddDoct).place(x=500,y=0)
List1=Button(BttnFrame,width=15,pady=7,text="Update Doctor",border=0,bg="#57a1f8",cursor="hand2",fg="white",command=update).place(x=620,y=0)
List2=Button(BttnFrame,width=15,pady=7,text="Search DoctAppts",border=0,bg="#57a1f8",cursor="hand2",fg="white",command=srch).place(x=740,y=0)
List3=Button(BttnFrame,width=15,pady=7,text="Remove Doctor",border=0,bg="#57a1f8",cursor="hand2",fg="white",command=dlt).place(x=860,y=0)

ob=Hospital(management)
management.mainloop()