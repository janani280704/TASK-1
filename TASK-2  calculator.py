import tkinter as tk
from tkinter import messagebox

# Main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field to display expression
expression = ""
entry_text = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Function to update the expression
def press(key):
    global expression
    expression += str(key)
    entry_text.set(expression)

# Function to clear the input
def clear():
    global expression
    expression = ""
    entry_text.set("")

# Function to calculate the result
def equal():
    global expression
    try:
        result = str(eval(expression))
        entry_text.set(result)
        expression = result
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        expression = ""
        entry_text.set("")
    except:
        messagebox.showerror("Error", "Invalid input.")
        expression = ""
        entry_text.set("")

# Button layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=equal)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=95, pady=20, font=("Arial", 14), command=clear)
        btn.grid(row=row, column=col, columnspan=4)
        continue
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: press(t))
    btn.grid(row=row, column=col)

# Run the GUI loop
root.mainloop()
