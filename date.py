from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
import mysql.connector

date = tk.Tk()
date.title("Doctor Appointments Search")
date.geometry("800x300")
date.resizable(False,False)
date.configure(bg="coral1")

def search_patients_by_doctor():
    doctor_id = entry_doctor_id.get()

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="finalproj"
        )
        cursor = connection.cursor()

        search_query = "SELECT PatientID, PatientName, Email, Phone, ApptDate, ApptID FROM patient WHERE DoctorID = %s"
        cursor.execute(search_query, (doctor_id,))

        display_search_results(cursor.fetchall())

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        cursor.close()
        connection.close()

def display_search_results(results):
    for row in tree.get_children():
        tree.delete(row)

    for patient in results:
        tree.insert("", "end", values=patient)

tk.Label(date,bg="coral1", text="Doctor ID:",font=("times new roman",13)).pack()
entry_doctor_id = tk.Entry(date)
entry_doctor_id.pack(pady=4)

search_button = tk.Button(date,bg="light sky blue", text="Search Appointments",font=("times new roman",10), command=search_patients_by_doctor)
search_button.pack(pady=10)

columns = ("PatientID", "PatientName", "Email", "Phone", "ApptDate", "ApptID")
tree = ttk.Treeview(date, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=130, minwidth=130)

tree.pack(pady=10)
icon_image = PhotoImage(file="hams.ico")
date.iconphoto(True, icon_image)

date.mainloop()
