import tkinter as tk
from tkinter import messagebox

def convert_case():
    input_str = entry_input.get()
    converted = []
    for c in input_str:
        if c.isupper():
            converted.append(c.lower())
        elif c.islower():
            converted.append(c.upper())
        else:
            converted.append(c)
    result = ''.join(converted)
    
    # Temporarily enable the result entry to display output
    entry_result.config(state='normal')
    entry_result.delete(0, tk.END)
    entry_result.insert(0, result)
    entry_result.config(state='readonly')

def about():
    messagebox.showinfo("About", "Case Converter\nAuthor: yueyue\nVersion: 1.5")

# Create main window
root = tk.Tk()
root.title("Case Converter by yueyue")
root.geometry("500x250")

# Create menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)
helpmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

# UI components
frame = tk.Frame(root)
frame.pack(pady=20)

# Input section
tk.Label(frame, text="Input text:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_input = tk.Entry(frame, width=40)
entry_input.grid(row=0, column=1, padx=5, pady=5)

# Convert button
btn_convert = tk.Button(frame, text="Convert Case", command=convert_case)
btn_convert.grid(row=1, column=0, columnspan=2, pady=10)

# Output section
tk.Label(frame, text="Result:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
entry_result = tk.Entry(frame, width=40, state='readonly')
entry_result.grid(row=2, column=1, padx=5, pady=5)

# Set focus to input field
entry_input.focus_set()

root.mainloop()