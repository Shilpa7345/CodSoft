import tkinter as tk
from tkinter import messagebox


def press(num):
    current_text = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(tk.END, current_text + str(num))


def equalpress():
    try:
        result = str(eval(entry_field.get()))
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")


def percentage():
    try:
        current_text = entry_field.get()
        result = str(eval(current_text) / 100)
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")


def clear():
    entry_field.delete(0, tk.END)

def cut():
    current_text = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(tk.END, current_text[:-1])

root = tk.Tk()
root.title("Simple Calculator")

entry_field = tk.Entry(root, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
entry_field.grid(row=0, column=0, columnspan=4)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('%', 5, 0), ('C', 5, 1), ('AC', 5, 2)
]


for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=30, pady=20, bd=8, fg="black", font=('Arial', 20),
                           command=equalpress)
    elif text == '%':
        button = tk.Button(root, text=text, padx=28, pady=20, bd=8, fg="black", font=('Arial', 20),
                           command=percentage)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=30, pady=20, bd=8, fg="black", font=('Arial', 20),
                           command=cut)
    elif text == 'AC':
        button = tk.Button(root, text=text, padx=26, pady=20, bd=8, fg="black", font=('Arial', 20),
                           command=clear)
    else:
        button = tk.Button(root, text=text, padx=30, pady=20, bd=8, fg="black", font=('Arial', 20),
                           command=lambda txt=text: press(txt))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
