
import tkinter as tk
from tkinter import messagebox
import sqlite3
import csv

def submit_grade():
    student = student_name.get()
    subject = subject_entry.get()
    term = term_entry.get()
    score = score_entry.get()

    if not student or not subject or not term or not score:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    try:
        score_float = float(score)
    except ValueError:
        messagebox.showerror("Input Error", "Grade must be a number.")
        return

    conn = sqlite3.connect("edudata.db")
    cur = conn.cursor()

    cur.execute("SELECT student_id FROM students WHERE full_name = ?", (student,))
    result = cur.fetchone()
    if result:
        student_id = result[0]
        cur.execute("INSERT INTO grades (student_id, subject, term, score) VALUES (?, ?, ?, ?)",
                    (student_id, subject, term, score_float))
        conn.commit()

        cur.execute("SELECT s.full_name, g.subject, g.term, g.score FROM grades g JOIN students s ON g.student_id = s.student_id")
        rows = cur.fetchall()
        headers = ["Full Name", "Subject", "Term", "Grade"]
        conn.close()

        with open("grades_export.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)

        with open("grades_export.txt", "w") as f:
            f.write("\t".join(headers) + "\n")
            for row in rows:
                f.write("\t".join(str(i) for i in row) + "\n")

        messagebox.showinfo("Success", "Grade recorded and exported!")
    else:
        messagebox.showerror("Student Not Found", "No student found with that name.")

root = tk.Tk()
root.title("EduDataSystem - Grades")
root.geometry("550x400")

tk.Label(root, text="Add Student Grade", font=("Arial", 16, "bold")).pack(pady=10)
form = tk.Frame(root)
form.pack(pady=10)

tk.Label(form, text="Student Full Name", anchor="w", width=20).grid(row=0, column=0, pady=5)
student_name = tk.Entry(form, width=40)
student_name.grid(row=0, column=1, pady=5)

tk.Label(form, text="Subject", anchor="w", width=20).grid(row=1, column=0, pady=5)
subject_entry = tk.Entry(form, width=40)
subject_entry.grid(row=1, column=1, pady=5)

tk.Label(form, text="Term", anchor="w", width=20).grid(row=2, column=0, pady=5)
term_entry = tk.Entry(form, width=40)
term_entry.grid(row=2, column=1, pady=5)

tk.Label(form, text="Grade", anchor="w", width=20).grid(row=3, column=0, pady=5)
score_entry = tk.Entry(form, width=40)
score_entry.grid(row=3, column=1, pady=5)

tk.Button(root, text="Submit Grade", command=submit_grade).pack(pady=20)
root.mainloop()
