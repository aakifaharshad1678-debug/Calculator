import tkinter as tk

# Create window
root = tk.Tk()
root.title("Pink Calculator")
root.geometry("350x500")
root.configure(bg="#FFC0CB")
root.resizable(False, False)

expression = ""

# Display
display = tk.Entry(
    root,
    font=("Arial", 24),
    bd=5,
    relief="flat",
    justify="right",
    bg="#FFF0F5",
    fg="#C71585"
)
display.pack(fill="both", padx=10, pady=20, ipady=15)

# Functions
def press(num):
    global expression
    expression += str(num)
    display.delete(0, tk.END)
    display.insert(0, expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(0, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        expression = ""

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def backspace():
    global expression
    expression = expression[:-1]
    display.delete(0, tk.END)
    display.insert(0, expression)

# Buttons
buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

frame = tk.Frame(root, bg="#FFC0CB")
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame, bg="#FFC0CB")
    row_frame.pack()

    for btn in row:
        if btn == "":
            tk.Label(row_frame, width=6, bg="#FFC0CB").pack(side="left", padx=3, pady=3)
            continue

        if btn == "=":
            cmd = equal
            color = "#FF1493"
        elif btn == "C":
            cmd = clear
            color = "#E91E63"
        elif btn == "⌫":
            cmd = backspace
            color = "#FF69B4"
        else:
            cmd = lambda x=btn: press(x)
            color = "#FFB6C1"

        tk.Button(
            row_frame,
            text=btn,
            width=6,
            height=2,
            font=("Arial", 16, "bold"),
            bg=color,
            fg="white",
            relief="flat",
            activebackground="#FF1493",
            activeforeground="white",
            command=cmd
        ).pack(side="left", padx=3, pady=3)

root.mainloop()