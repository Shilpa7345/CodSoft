import tkinter as tk
from tkinter import messagebox
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.mark_as_completed_button = tk.Button(root, text="Mark as Completed", command=self.mark_as_completed)
        self.mark_as_completed_button.pack(pady=5)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            self.save_tasks()
        except:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_as_completed(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(tk.END, f"{task} (Completed)")
            self.save_tasks()
        except:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            tasks = self.task_listbox.get(0, tk.END)
            for task in tasks:
                file.write(task + "\n")

    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    self.task_listbox.insert(tk.END, task.strip())

root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
