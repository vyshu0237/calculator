import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Classic Calculator")
        self.root.geometry("320x450")
        self.root.configure(bg="#2c3e50")  # Dark background

        # Display styling
        self.display = tk.Entry(
            root, font=("Courier New", 24), justify="right", bd=10,
            relief=tk.FLAT, bg="#ecf0f1", fg="#2c3e50"
        )
        self.display.grid(row=0, column=0, columnspan=4, pady=15, ipady=10)

        self.operator = None
        self.first_operand = 0
        self.operator_pressed = False

        # Button configuration
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "C", "=", "+",
            "sin", "cos", "tan", "π",
            "←"
        ]

        row = 1
        col = 0

        for label in buttons:
            button = tk.Button(
                root, text=label, width=5, height=2, font=("Courier New", 16, "bold"),
                bg="#34495e", fg="#ecf0f1", activebackground="#1abc9c",
                command=lambda l=label: self.on_button_click(l)
            )
            button.grid(row=row, column=col, padx=5, pady=5, ipadx=5, ipady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, command):
        if command.isdigit():
            if self.operator_pressed:
                self.display.delete(0, tk.END)
                self.operator_pressed = False
            self.display.insert(tk.END, command)
        elif command == "C":
            self.display.delete(0, tk.END)
            self.operator = None
            self.first_operand = 0
            self.operator_pressed = False
        elif command == "=":
            try:
                second_operand = float(self.display.get())
                result = self.calculate(self.first_operand, second_operand, self.operator)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.first_operand = result
                self.operator_pressed = False
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif command in ["sin", "cos", "tan"]:
            try:
                operand = float(self.display.get())
                result = self.calculate_trig(operand, command)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.first_operand = result
                self.operator_pressed = False
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif command == "π":
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(math.pi))
        elif command == "←":
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current[:-1])
        else:
            if self.display.get() != "":
                self.first_operand = float(self.display.get())
                self.operator = command
                self.operator_pressed = True

    def calculate(self, a, b, operator):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return 0 if b == 0 else a / b
        return 0

    def calculate_trig(self, operand, func):
        if func == "sin":
            return math.sin(operand)
        elif func == "cos":
            return math.cos(operand)
        elif func == "tan":
            return math.tan(operand)
        return 0

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
