import secrets
import string
import tkinter as tk
from tkinter import messagebox

#Made By Matthew Colman

def generate_password(length=16, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    required = [secrets.choice(string.ascii_lowercase)]

    if use_upper:
        chars += string.ascii_uppercase
        required.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        chars += string.digits
        required.append(secrets.choice(string.digits))
    if use_symbols:
        chars += string.punctuation
        required.append(secrets.choice(string.punctuation))

    password = required + [secrets.choice(chars) for _ in range(length - len(required))]
    secrets.SystemRandom().shuffle(password)
    return "".join(password)

def on_generate():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a number for length.")
        return
    if length < 4:
        messagebox.showerror("Error", "Length must be at least 4.")
        return
    result_var.set(generate_password(length, upper_var.get(), digits_var.get(), symbols_var.get()))

def on_close():
    if messagebox.askyesno("Confirm", "Are you sure you want to close?"):
        root.destroy()

root = tk.Tk()
root.title("Password Generator")
root.protocol("WM_DELETE_WINDOW", on_close)

tk.Label(root, text="Length:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
length_entry = tk.Entry(root, width=6)
length_entry.insert(0, "16")
length_entry.grid(row=0, column=1, sticky="w", pady=5)

upper_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Uppercase", variable=upper_var).grid(row=1, column=0, sticky="w", padx=10)
tk.Checkbutton(root, text="Numbers", variable=digits_var).grid(row=2, column=0, sticky="w", padx=10)
tk.Checkbutton(root, text="Symbols", variable=symbols_var).grid(row=3, column=0, sticky="w", padx=10)

tk.Button(root, text="Generate", command=on_generate).grid(row=4, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=30, justify="center").grid(row=5, column=0, columnspan=2, padx=10, pady=(0, 10))

root.mainloop()
