
import tkinter as tk
from tkinter import messagebox
import sqlite3
import csv
from datetime import date

def submit_attendance():
    student = student_name.get()
    status = status_var.get()
    today = date.today().isoformat()

    if not student or not status:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    conn = sqlite3.connect("edudata.db")
    cur = conn.cursor()
    cur.execute("SELECT student_id FROM students WHERE full_name = ?", (student,))
    result = cur.fetchone()
    if result:
        student_id = result[0]
        cur.execute("INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
                    (student_id, today, status))
        conn.commit()

        cur.execute("SELECT a.date, s.full_name, a.status FROM attendance a JOIN students s ON a.student_id = s.student_id")
        rows = cur.fetchall()
        headers = ["Date", "Full Name", "Status"]
        conn.close()

        with open("attendance_export.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)

        with open("attendance_export.txt", "w") as f:
            f.write("\t".join(headers) + "\n")
            for row in rows:
                f.write("\t".join(str(i) for i in row) + "\n")

        messagebox.showinfo("Success", "Attendance recorded and exported!")
    else:
        messagebox.showerror("Student Not Found", "No student found with that name.")

root = tk.Tk()
root.title("EduDataSystem - Attendance")
root.geometry("500x350")

tk.Label(root, text="Mark Student Attendance", font=("Arial", 16, "bold")).pack(pady=10)
form = tk.Frame(root)
form.pack(pady=10)

tk.Label(form, text="Student Full Name", anchor="w", width=20).grid(row=0, column=0, pady=5)
student_name = tk.Entry(form, width=40)
student_name.grid(row=0, column=1, pady=5)

tk.Label(form, text="Status", anchor="w", width=20).grid(row=1, column=0, pady=5)
status_var = tk.StringVar()
status_menu = tk.OptionMenu(form, status_var, "Present", "Absent")
status_menu.config(width=37)
status_menu.grid(row=1, column=1, pady=5)

tk.Button(root, text="Submit Attendance", command=submit_attendance).pack(pady=20)
root.mainloop()
