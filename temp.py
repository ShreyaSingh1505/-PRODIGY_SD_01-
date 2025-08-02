
import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp_text = entry_temp.get().strip()
        if not temp_text:
            messagebox.showwarning("Input Missing", "Please enter a temperature value.")
            return

        temp = float(temp_text)
        unit = combo_unit.get()

        if unit == "Celsius":
            f = (temp * 9/5) + 32
            k = temp + 273.15
            result.set(f"{temp:.2f} °C = {f:.2f} °F\n{temp:.2f} °C = {k:.2f} K")
        elif unit == "Fahrenheit":
            c = (temp - 32) * 5/9
            k = c + 273.15
            result.set(f"{temp:.2f} °F = {c:.2f} °C\n{temp:.2f} °F = {k:.2f} K")
        elif unit == "Kelvin":
            c = temp - 273.15
            f = (c * 9/5) + 32
            result.set(f"{temp:.2f} K = {c:.2f} °C\n{temp:.2f} K = {f:.2f} °F")
        else:
            result.set("Please select a valid unit.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric temperature.")

def clear_fields():
    entry_temp.delete(0, tk.END)
    combo_unit.set("Celsius")
    result.set("")

# GUI Setup
root = tk.Tk()
root.title(" Temperature Converter")
root.geometry("400x300")
root.configure(bg="#f0f8ff")
root.resizable(False, False)

# Header Label
tk.Label(root, text="Temperature Converter", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#333").pack(pady=10)

# Frame for Input
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=5)

tk.Label(frame, text="Enter Temperature:", font=("Arial", 11), bg="#f0f8ff").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_temp = tk.Entry(frame, width=20, font=("Arial", 11))
entry_temp.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Select Unit:", font=("Arial", 11), bg="#f0f8ff").grid(row=1, column=0, sticky="e", padx=5, pady=5)
combo_unit = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", font=("Arial", 11))
combo_unit.grid(row=1, column=1, padx=5)
combo_unit.set("Celsius")

# Buttons
btn_frame = tk.Frame(root, bg="#f0f8ff")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Convert", command=convert_temperature, font=("Arial", 11), bg="#4CAF50", fg="white", width=10).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear", command=clear_fields, font=("Arial", 11), bg="#f44336", fg="white", width=10).grid(row=0, column=1, padx=10)

# Result Label
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12, "bold"), fg="#003366", bg="#f0f8ff", justify="center").pack(pady=15)

# Enter key binding
root.bind('<Return>', lambda event: convert_temperature())

root.mainloop()

