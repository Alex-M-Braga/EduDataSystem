
import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
import subprocess

# Banco e inicialização de usuários padrão
def initialize_users():
    conn = sqlite3.connect("edudata.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    """)
    cur.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cur.fetchone():
        cur.execute("INSERT INTO users (username, password, role) VALUES ('admin', 'admin123', 'Admin')")
    conn.commit()
    conn.close()

def login():
    user = username.get()
    pwd = password.get()

    conn = sqlite3.connect("edudata.db")
    cur = conn.cursor()
    cur.execute("SELECT role FROM users WHERE username = ? AND password = ?", (user, pwd))
    result = cur.fetchone()
    conn.close()

    if result:
        role = result[0]
        login_window.destroy()
        open_menu(role)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_menu(role):
    root = tk.Tk()
    root.title("EduDataSystem - Main Menu")
    root.geometry("400x400")

    tk.Label(root, text=f"Welcome, {role}", font=("Arial", 14)).pack(pady=20)
    tk.Button(root, text="Register Student", width=25, command=lambda: subprocess.Popen(["python", "edudatasystem_register.py"])).pack(pady=10)
    tk.Button(root, text="Mark Attendance", width=25, command=lambda: subprocess.Popen(["python", "edudatasystem_attendance.py"])).pack(pady=10)
    tk.Button(root, text="Add Grades", width=25, command=lambda: subprocess.Popen(["python", "edudatasystem_grades.py"])).pack(pady=10)
    tk.Button(root, text="Exit", width=25, command=root.destroy).pack(pady=20)

    root.mainloop()

# Interface de login
initialize_users()
login_window = tk.Tk()
login_window.title("EduDataSystem - Login")
login_window.geometry("350x250")

tk.Label(login_window, text="Login", font=("Arial", 16)).pack(pady=10)
form = tk.Frame(login_window)
form.pack(pady=10)

tk.Label(form, text="Username").grid(row=0, column=0, pady=5)
username = tk.Entry(form)
username.grid(row=0, column=1, pady=5)

tk.Label(form, text="Password").grid(row=1, column=0, pady=5)
password = tk.Entry(form, show="*")
password.grid(row=1, column=1, pady=5)

tk.Button(login_window, text="Login", command=login).pack(pady=20)

login_window.mainloop()
