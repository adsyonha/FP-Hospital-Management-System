from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import ImageTk,Image
import mysql.connector

def logout():
    management.destroy()
    import login

def doct():
     import add


management = Tk()
management.attributes('-fullscreen', True)

class Hospital:
    def __init__(self, management):
        management = management
        management.title("Hospital Management System")
        management.geometry("1000x500")
        management.resizable(False,False)

PatientID=StringVar()
PatientName=StringVar()
Email=StringVar()
Phone=StringVar()
ApptID=StringVar()
ApptDate=StringVar()
DoctorID=StringVar()


lbltitle=Label(management,
                       bd=8,
                       relief=RIDGE,
                       text="HOSPITAL MANAGEMENT SYSTEM",
                       fg="black",
                       bg="indian red2",
                       font=("times new roman",30)
                       )
lbltitle.pack(side=TOP, fill=X)
###################------------DATA-----------#################

Dataframe=Frame(management,bg="indian red1",bd=10,relief=RIDGE,padx=5)
Dataframe.place(x=0,y=65,width=1366,height=702,)


DataframeLeft=LabelFrame(Dataframe,bg="indian red1",bd=5,relief=RIDGE,padx=5,
                         font=("times new roman",11,"bold"),text="Patient Appointment")
DataframeLeft.place(x=0,y=5,width=505,height=385)

DataframeRight=LabelFrame(Dataframe,bg="indian red1",bd=5,relief=RIDGE,padx=5,
                         font=("times new roman",11,"bold"),text="Doctors")
DataframeRight.place(x=500,y=5,width=840,height=385)

BotFrame=LabelFrame(management,bd=7,bg="indian red1",relief=RIDGE,font=("times new roman",11,"bold"),text="List of Appointment")
BotFrame.place(x=10,y=515,width=1345,height=240)

BttnFrame=Frame(management,bd=10,bg="indian red1",relief=RIDGE)
BttnFrame.place(x=10,y=465,width=1345,height=55)

img= Image.open("hms.png")
bg_img= ImageTk.PhotoImage(img)
bg_lbl= Label(DataframeLeft,bg="indian red1",image=bg_img)
bg_lbl.place(x=250, y=150)

###################------------DATALEFT-----------#################
lblPatient=Label(DataframeLeft,bg="indian red1",font=("times new roman",13,"bold"),text="Patient Appointment",padx=2,pady=6)
lblPatient.grid(row=0,column=0,sticky=W)

lblid=Label(DataframeLeft,bg="indian red1",font=("times new roman",11),text="Patient ID:",padx=2,pady=4)
lblid.grid(row=1,column=0)
txtid=Entry(DataframeLeft,font=("times new roman",11),textvariable=PatientID,width=20)
txtid.grid(row=1,column=1)

lblname=Label(DataframeLeft,bg="indian red1",font=("times new roman",11),text="Patient Name:",padx=2,pady=4)
lblname.grid(row=2,column=0)
txtname=Entry(DataframeLeft,font=("times new roman",11),textvariable=PatientName,width=20)
txtname.grid(row=2,column=1)

lblemail=Label(DataframeLeft,bg="indian red1",font=("times new roman",11),text="Email:",padx=2,pady=4)
lblemail.grid(row=3,column=0)
txtemail=Entry(DataframeLeft,font=("times new roman",11),textvariable=Email,width=20)
txtemail.grid(row=3,column=1)

lblphone=Label(DataframeLeft,bg="indian red1",font=("times new roman",11),text="Phone Number:",padx=2,pady=4)
lblphone.grid(row=4,column=0)
txtphone=Entry(DataframeLeft,font=("times new roman",11),textvariable=Phone,width=20)
txtphone.grid(row=4,column=1)

lblappt=Label(DataframeLeft,bg="indian red1",font=("times new roman",11),text="Appt. ID:",padx=2,pady=4)
lblappt.grid(row=5,column=0)
txtappt=Entry(DataframeLeft,font=("times new roman",11),textvariable=ApptID,width=20)
txtappt.grid(row=5,column=1)

lbldate=Label(DataframeLeft,bg="indian red1",font=("times new roman",11),text="Appt. Date:",padx=2,pady=4)
lbldate.grid(row=6,column=0)
txtdate = DateEntry(DataframeLeft, width=20, background='darkblue',textvariable=ApptDate,state="readonly", foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
txtdate.grid(row=6,column=1)
txtdate.bind("<<DateEntrySelected>>", lbldate)

lbldoct=Label(DataframeLeft,bg="indian red1",font=("times new roman",11),text="Doctor ID:",padx=2,pady=4)
lbldoct.grid(row=7,column=0)
txtdoct=Entry(DataframeLeft,font=("times new roman",11),textvariable=DoctorID,width=20)
txtdoct.grid(row=7,column=1)

content = txtname.get()
content = txtemail.get()
content = txtphone.get()
content = txtappt.get()
content = txtdate.get()
content = txtdoct.get()

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
            my_cursor.execute("select * from doctlist where Status = 'Available' ")
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
list_table.heading("phone",text="Phone")
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
doct_table=ttk.Treeview(DataframeRight,column=("doctorid","doctorname","email","phone","nop","special","stats"),xscrollcommand=scroll_doct.set)
scroll_doct.pack(side=RIGHT, fill=Y)

scroll_doct=ttk.Scrollbar(command=doct_table.yview)

doct_table.heading("doctorid",text="DoctorID")
doct_table.heading("doctorname",text="DoctorName")
doct_table.heading("email",text="Email")
doct_table.heading("phone",text="Phone#")
doct_table.heading("nop",text="No.ofPatient")
doct_table.heading("special",text="Specialization")
doct_table.heading("stats",text="Status")

doct_table["show"]="headings"

doct_table.column("doctorid",width=80)
doct_table.column("doctorname",width=80)
doct_table.column("email",width=80)
doct_table.column("phone",width=80)
doct_table.column("nop",width=80)
doct_table.column("special",width=80)
doct_table.column("stats",width=80)

doct_table.pack(fill=BOTH,expand=1)
doct_data()


######################-----------------DatabaseADD--------------###################
def iAddAppointment():
    if PatientName.get() == "" or Email.get() == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        conn = mysql.connector.connect(host="localhost",user="root",password="",database="finalproj")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into patient (PatientName,Email,Phone,ApptID,ApptDate,DoctorID) values(%s,%s,%s,%s,%s,%s)",(
                                                                              PatientName.get(),
                                                                              Email.get(),
                                                                              Phone.get(),
                                                                              ApptID.get(),
                                                                              ApptDate.get(),
                                                                              DoctorID.get()
        ))
        conn.commit()
        show_data()
        conn.close()
        messagebox.showinfo("Succes","Appointment has been recorded")
   
    txtname.delete(0, "end")
    txtemail.delete(0, "end")
    txtphone.delete(0, "end")
    txtappt.delete(0, "end")
    txtdate.delete(0, "end")
    txtdoct.delete(0, "end")

######################-----------------DatabaseUPDATE--------------###################

def update():
    patient_id = txtid.get()
    patient_name = txtname.get()
    email = txtemail.get()
    phone = txtphone.get()
    appt_id = txtappt.get()
    appt_date = txtdate.get()
    doctor_id = txtdoct.get()

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="finalproj"
        )
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM patient WHERE PatientID = %s", (patient_id,))
        existing_patient = cursor.fetchone()

        if existing_patient:
            update_query = "UPDATE patient SET PatientName=%s, Email=%s, Phone=%s, ApptID=%s, ApptDate=%s, DoctorID=%s WHERE PatientID=%s"
            data = (patient_name, email, phone, appt_id, appt_date, doctor_id, patient_id)
            cursor.execute(update_query, data)

            connection.commit()

            txtname.delete(0, "end")
            txtname.insert(0, patient_name)

            txtemail.delete(0, "end")
            txtemail.insert(0, email)

            txtphone.delete(0, "end")
            txtphone.insert(0, phone)

            txtappt.delete(0, "end")
            txtappt.insert(0, appt_id)

            txtdate.delete(0, "end")
            txtdate.insert(0, appt_date)

            txtdoct.delete(0, "end")
            txtdoct.insert(0, doctor_id)

            messagebox.showinfo("Success", "Record updated successfully!")
            update_treeview()
        else:
            messagebox.showerror("Error", "Patient ID does not exist!")

        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

def update_treeview():
    for row in list_table.get_children():
        list_table.delete(row)

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="finalproj"
        )
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM patient")
        patients = cursor.fetchall()

        for patient in patients:
            list_table.insert("", "end", values=patient)

    except mysql.connector.Error as err:
        messagebox.showerror(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()

######################-----------------DatabaseDELETE--------------###################

def deleteappt():
    patient_id = txtid.get()

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="finalproj"
        )
        cursor = connection.cursor()

        delete_query = "DELETE FROM patient WHERE PatientID = %s"
        cursor.execute(delete_query, (patient_id,))

        connection.commit()

        reset_auto_increment_query = "ALTER TABLE patient AUTO_INCREMENT = 1"
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
    for row in list_table.get_children():
        list_table.delete(row)

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="finalproj"
        )
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM patient")
        patients = cursor.fetchall()

        for patient in patients:
            list_table.insert("", "end", values=patient)

    except mysql.connector.Error as err:
        messagebox.showerror(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()


def patient(event=""):
        cursor_row=list_table.focus()
        content=list_table.item(cursor_row)
        row=content["values"]
        PatientID.set(row[0])
        PatientName.set(row[1])
        Email.set(row[2])
        Phone.set(row[3])
        ApptID.set(row[4])
        ApptDate.set(row[5])
        DoctorID.set(row[6])

list_table.bind("<ButtonRelease-1>",patient)

def listdoct(event=""):
        cursor_row=doct_table.focus()
        content=doct_table.item(cursor_row)
        row=content["values"]
        DoctorID.set(row[0])
        

doct_table.bind("<ButtonRelease-1>",listdoct)

#######-------------------------Button---------------------------#######

AddAppointment=Button(BttnFrame,width=15,padx=2,pady=7,text="Add Appointment",border=0,bg="#57a1f8",cursor="hand2",fg="white",command=iAddAppointment).place(x=0,y=0)
UpdateAppointment=Button(BttnFrame,width=20,padx=2,pady=7,text="Update Appointment",border=0,bg="#57a1f8",cursor="hand2",fg="white",command=update).place(x=120,y=0)
SearchAppointment=Button(BttnFrame,width=20,padx=2,pady=7,text="Delete Appointment",border=0,bg="#57a1f8",cursor="hand2",fg="white",command = deleteappt).place(x=275,y=0)
Button(BttnFrame,width=10,padx=2,pady=7,text="Logout",border=0,bg="#57a1f8",cursor="hand2",fg="white",command=logout).place(x=1245,y=0)



ob=Hospital(management)
management.mainloop()