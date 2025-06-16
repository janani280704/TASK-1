import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Add new task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        task_entry.delete(0, tk.END)
        refresh_tasks()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

# Mark task as complete
def toggle_complete(index):
    tasks[index]["completed"] = not tasks[index]["completed"]
    refresh_tasks()
    save_tasks(tasks)

# Delete task
def delete_task(index):
    del tasks[index]
    refresh_tasks()
    save_tasks(tasks)

# Refresh the task list display
def refresh_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()
    
    for index, task in enumerate(tasks):
        frame = tk.Frame(task_frame)
        frame.pack(fill="x", pady=2)

        check_var = tk.BooleanVar(value=task["completed"])
        check = tk.Checkbutton(frame, variable=check_var,
                               command=lambda i=index: toggle_complete(i))
        check.pack(side="left")

        label = tk.Label(frame, text=task["task"], anchor="w")
        label.pack(side="left", fill="x", expand=True)
        if task["completed"]:
            label.config(fg="gray", font=("Arial", 10, "overstrike"))

        delete_btn = tk.Button(frame, text="Delete", command=lambda i=index: delete_task(i))
        delete_btn.pack(side="right")

# Main app window
app = tk.Tk()
app.title("To-Do List")

# Task input
task_entry = tk.Entry(app, width=40)
task_entry.pack(padx=10, pady=10)

add_btn = tk.Button(app, text="Add Task", command=add_task)
add_btn.pack(pady=(0, 10))

# Task display area
task_frame = tk.Frame(app)
task_frame.pack(padx=10, pady=10)

# Load and show tasks
tasks = load_tasks()
refresh_tasks()

# Run app
app.mainloop()
