import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")
        return

    if length < 4:
        messagebox.showwarning("Too Short", "Password length should be at least 4.")
        return

    characters = list(string.ascii_lowercase)
    if uppercase_var.get():
        characters.extend(string.ascii_uppercase)
    if numbers_var.get():
        characters.extend(string.digits)
    if symbols_var.get():
        characters.extend(string.punctuation)

    if not characters:
        messagebox.showwarning("No Options Selected", "Please select at least one character set.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

def copy_to_clipboard():
    password = result_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Title
tk.Label(root, text="🔐 Password Generator", font=("Arial", 16)).pack(pady=10)

# Length input
tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Checkboxes for character types
uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor="w", padx=30)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Output
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, font=("Arial", 12), justify="center").pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

# Start GUI loop
root.mainloop()
