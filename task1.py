import tkinter as tk
from tkinter import messagebox
import json

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Add task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks(tasks)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Remove selected task
def remove_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
        tasks.pop(selected_task)
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to remove!")

# Load existing tasks
tasks = load_tasks()

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Load tasks into listbox
for task in tasks:
    task_listbox.insert(tk.END, task)

root.mainloop()
