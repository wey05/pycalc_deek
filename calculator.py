import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("计算器 wyx 2.0")
        self.root.geometry("360x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Display variables
        self.current_expression = ""
        
        # Display frame
        display_frame = tk.Frame(self.root, bg="#f0f0f0")
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.display_label = tk.Label(
            display_frame, 
            text="", 
            anchor="e", 
            bg="#ffffff", 
            fg="#333333", 
            font=("Arial", 28, "bold"),
            relief="sunken",
            bd=2
        )
        self.display_label.pack(expand=True, fill="both")

        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Button layout
        buttons = [
            ('C', 0, 0, 1), ('(', 0, 1, 1), (')', 0, 2, 1), ('/', 0, 3, 1),
            ('7', 1, 0, 1), ('8', 1, 1, 1), ('9', 1, 2, 1), ('*', 1, 3, 1),
            ('4', 2, 0, 1), ('5', 2, 1, 1), ('6', 2, 2, 1), ('-', 2, 3, 1),
            ('1', 3, 0, 1), ('2', 3, 1, 1), ('3', 3, 2, 1), ('+', 3, 3, 1),
            ('0', 4, 0, 2), ('.', 4, 2, 1), ('=', 4, 3, 1)
        ]

        for button in buttons:
            text = button[0]
            row = button[1]
            col = button[2]
            colspan = button[3]

            if text in ['=', 'C']:
                bg_color = "#ff9999" if text == 'C' else "#99ff99"
                fg_color = "#000000"
            elif text in ['+', '-', '*', '/', '(', ')']:
                bg_color = "#e6e6e6"
                fg_color = "#333333"
            else:
                bg_color = "#ffffff"
                fg_color = "#000000"

            tk.Button(
                buttons_frame,
                text=text,
                font=("Arial", 18),
                bg=bg_color,
                fg=fg_color,
                activebackground="#cccccc",
                command=lambda t=text: self.on_button_click(t)
            ).grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=3, pady=3)

        # Configure grid weights
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.current_expression = ""
            self.update_display()
        elif char == '=':
            try:
                # Safe evaluation
                result = str(eval(self.current_expression))
                self.current_expression = result
                self.update_display()
            except ZeroDivisionError:
                messagebox.showerror("错误", "除数不能为0")
                self.current_expression = ""
                self.update_display()
            except Exception as e:
                messagebox.showerror("错误", "无效的数学表达式")
                self.current_expression = ""
                self.update_display()
        else:
            self.current_expression += str(char)
            self.update_display()

    def update_display(self):
        self.display_label.config(text=self.current_expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
