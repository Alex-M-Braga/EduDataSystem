
import tkinter as tk
from tkinter import messagebox
import sqlite3
import csv

def submit_student():
    data = (
        name_entry.get(),
        dob_entry.get(),
        grade_entry.get(),
        address_entry.get(),
        zone_entry.get(),
        emergency_entry.get(),
        needs_entry.get(),
        transport_entry.get(),
        pickup_entry.get(),
        observations_entry.get()
    )

    conn = sqlite3.connect("edudata.db")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO students (
            full_name, date_of_birth, grade_level, address, geo_zone,
            emergency_contact, special_needs, transport_method,
            authorized_pickups, observations
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()

    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    headers = [desc[0] for desc in cur.description]
    conn.close()

    with open("students_export.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    with open("students_export.txt", "w") as f:
        f.write("\t".join(headers) + "\n")
        for row in rows:
            f.write("\t".join(str(item) for item in row) + "\n")

    messagebox.showinfo("Success", "Student registered and exported successfully!")

root = tk.Tk()
root.title("EduDataSystem - Student Registration")
root.geometry("700x600")

tk.Label(root, text="Register New Student", font=("Arial", 16, "bold")).pack(pady=10)
form = tk.Frame(root)
form.pack(pady=10)

fields = [
    ("Full Name", "name_entry"),
    ("Date of Birth", "dob_entry"),
    ("Grade Level", "grade_entry"),
    ("Address", "address_entry"),
    ("Geo Zone", "zone_entry"),
    ("Emergency Contact", "emergency_entry"),
    ("Special Needs", "needs_entry"),
    ("Transport Method", "transport_entry"),
    ("Authorized Pickups", "pickup_entry"),
    ("Observations", "observations_entry"),
]

entries = {}
for idx, (label_text, var_name) in enumerate(fields):
    tk.Label(form, text=label_text, anchor="w", width=20).grid(row=idx, column=0, sticky="w", pady=4)
    entry = tk.Entry(form, width=50)
    entry.grid(row=idx, column=1, pady=4)
    entries[var_name] = entry

name_entry = entries["name_entry"]
dob_entry = entries["dob_entry"]
grade_entry = entries["grade_entry"]
address_entry = entries["address_entry"]
zone_entry = entries["zone_entry"]
emergency_entry = entries["emergency_entry"]
needs_entry = entries["needs_entry"]
transport_entry = entries["transport_entry"]
pickup_entry = entries["pickup_entry"]
observations_entry = entries["observations_entry"]

tk.Button(root, text="Submit", command=submit_student).pack(pady=15)

root.mainloop()
