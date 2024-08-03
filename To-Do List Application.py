import tkinter as tk
from tkinter import messagebox

# Data structure to store tasks
tasks = []
def add_task():
    """Add a new task to the list."""
    task_description = task_entry.get()
    if task_description:
        tasks.append({"description": task_description, "completed": False})
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task description.")

def delete_task():
    """Delete the selected task from the list."""
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def complete_task():
    """Mark the selected task as complete."""
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["completed"] = True
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to complete.")

def update_task_list():
    """Update the displayed list of tasks."""
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_status = "✓" if task["completed"] else "✗"
        task_description = task["description"]
        if task["completed"]:
            task_description = f"({task_description})"
        task_listbox.insert(tk.END, f"[{task_status}] {task_description}")
        # Apply color based on task status
        color = "light green" if task["completed"] else "light coral"
        task_listbox.itemconfig(tk.END, {'bg': color})

# Set up the main application window
root = tk.Tk()
root.title("To-Do List Application")
root.configure(bg="white")

# Title
title_label = tk.Label(root, text="TASKS FOR TODAY", font=("Helvetica", 24, "bold"), bg="white")
title_label.pack(pady=10)

# Task entry
task_entry_frame = tk.Frame(root, bg="white")
task_entry_frame.pack(pady=10)
task_entry = tk.Entry(task_entry_frame, width=40)
task_entry.pack(side=tk.LEFT, padx=5)
add_task_button = tk.Button(task_entry_frame, text="Add Task", command=add_task, bg="light blue")
add_task_button.pack(side=tk.LEFT, padx=5)

# Task listbox with scrollbar
task_listbox_frame = tk.Frame(root, bg="white")
task_listbox_frame.pack(pady=10)
scrollbar = tk.Scrollbar(task_listbox_frame, orient=tk.VERTICAL)
task_listbox = tk.Listbox(task_listbox_frame, width=50, height=10, yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Buttons
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)
delete_task_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="light blue")
delete_task_button.pack(side=tk.LEFT, padx=5)
complete_task_button = tk.Button(button_frame, text="Complete Task", command=complete_task, bg="light blue")
complete_task_button.pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop()
