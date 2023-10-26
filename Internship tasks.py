import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

def add_task():
    task = entry.get()
    due_date = due_date_entry.get()
    
    if task:
        task_with_due_date = {"task": task, "due_date": due_date}
        tasks_listbox.insert(tk.END, format_task_with_due_date(task_with_due_date))
        task_data.append(task_with_due_date)
        entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
        task_data.pop(selected_task_index)
    except IndexError:
        pass

def update_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        updated_task = entry.get()
        updated_due_date = due_date_entry.get()
        
        if updated_task:
            task_data[selected_task_index]["task"] = updated_task
            task_data[selected_task_index]["due_date"] = updated_due_date
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, format_task_with_due_date(task_data[selected_task_index]))
            entry.delete(0, tk.END)
            due_date_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    except IndexError:
        pass

def clear_tasks():
    tasks_listbox.delete(0, tk.END)
    task_data.clear()

def format_task_with_due_date(task_dict):
    task_name = task_dict["task"]
    due_date = task_dict["due_date"]
    if due_date:
        return f"{task_name} (Due: {due_date})"
    else:
        return task_name

root = tk.Tk()
root.title("To-Do List App")

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

entry = tk.Entry(frame, font=("Helvetica", 14))
entry.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

due_date_label = tk.Label(frame, text="Due Date (optional):", font=("Helvetica", 12))
due_date_label.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

due_date_entry = tk.Entry(frame, font=("Helvetica", 12))
due_date_entry.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

add_button = tk.Button(frame, text="Add Task", command=add_task, bg="#0078d4", fg="white", font=("Helvetica", 12))
add_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

delete_button = tk.Button(frame, text="Delete Task", command=delete_task, bg="#e74c3c", fg="white", font=("Helvetica", 12))
delete_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

update_button = tk.Button(frame, text="Update Task", command=update_task, bg="#2ecc71", fg="white", font=("Helvetica", 12))
update_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

clear_button = tk.Button(frame, text="Clear All Tasks", command=clear_tasks, bg="#f39c12", fg="white", font=("Helvetica", 12))
clear_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

tasks_listbox = tk.Listbox(root, font=("Helvetica", 12), selectmode=tk.SINGLE)
tasks_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

task_data = []

root.mainloop() 