import tkinter as tk
import math

class GUICalculator:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Calculator")
        
        # Display
        self.display = tk.Entry(master, width=30, justify='right', font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '√', '^', 'sin',
            'cos', '!', '(', ')'
        ]
        
        # Create buttons
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(master, text=button, command=cmd, width=7, height=2).grid(row=row, column=col, padx=3, pady=3)
            col += 1
            if col > 3:
                col = 0
                row += 1
    
    def click(self, key):
        if key == '=':
            # Safely evaluate the expression
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        
        elif key == 'C':
            self.display.delete(0, tk.END)
        
        elif key == '√':
            try:
                result = math.sqrt(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        
        elif key == '^':
            self.display.insert(tk.END, '**')
        
        elif key == 'sin':
            try:
                result = math.sin(math.radians(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        
        elif key == 'cos':
            try:
                result = math.cos(math.radians(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        
        elif key == '!':
            try:
                result = math.factorial(int(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        
        else:
            self.display.insert(tk.END, key)

def main():
    root = tk.Tk()
    calculator = GUICalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
