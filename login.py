import tkinter as tk
import sqlite3
import hashlib

def create_account():
    # code for creating a new account

def login():
    # code for logging in

def check_password(entered_password, stored_password):
    # code for checking entered password against stored password

root = tk.Tk()
root.title("Login System")

username_label = tk.Label(root, text="Username")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

password_label = tk.Label(root, text="Password")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0)

create_account_button = tk.Button(root, text="Create Account", command=create_account)
create_account_button.grid(row=2, column=1)

root.mainloop()
