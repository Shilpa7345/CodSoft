import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())  
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the length.")
        return

    if length < 1:
        messagebox.showerror("Invalid Length", "Password length should be at least 1.")
        return


    characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(random.choice(characters) for _ in range(length))
    

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")


length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack(pady=10)


length_entry = tk.Entry(root)
length_entry.pack(pady=5)


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=20)

password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

root.mainloop()
