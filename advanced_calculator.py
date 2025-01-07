import tkinter as tk  # Import tkinter module for creating GUI
from math import sin, cos, tan, sqrt, log, exp, factorial, asin, acos, atan  # Import math functions

# Define the AdvancedCalculator class
class AdvancedCalculator:
    def __init__(self, root):
        self.root = root  # Initialize the root window
        self.root.title("Advanced Calculator")  # Set the window title
        self.root.geometry("400x600")  # Set the window size
        
        self.result = tk.StringVar()  # Create a StringVar to store the result
        self.memory = None  # Initialize memory variable
        
        self.create_widgets()  # Create the calculator widgets
        self.bind_keys()  # Enable keyboard support

    def create_widgets(self):
        # Create an entry widget for displaying the result
        result_entry = tk.Entry(self.root, 
                                textvariable=self.result, 
                                font=("Arial", 24), bd=10, 
                                insertwidth=4, 
                                width=14, 
                                justify='right')
        result_entry.grid(row=0, 
                          column=0, 
                          columnspan=4)
        
        # Define the calculator buttons and their positions
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('sqrt', 5, 3),
            ('log', 6, 0), ('exp', 6, 1), ('C', 6, 2), ('(', 6, 3),
            (')', 7, 0), ('^', 7, 1), ('%', 7, 2), ('//', 7, 3),
            ('M+', 8, 0), ('M-', 8, 1), ('MR', 8, 2), ('MC', 8, 3)  # Memory buttons
        ]
        
        # Create the buttons and place them on the grid
        for (text, row, col) in buttons:
            tk.Button(self.root, 
                      text=text, 
                      padx=20, 
                      pady=20, 
                      font=("Arial", 14), 
                      command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col)
    
    def bind_keys(self):
        # Bind keyboard keys to the calculator functions
        self.root.bind('<Return>', lambda event: self.on_button_click('='))
        self.root.bind('<BackSpace>', lambda event: self.on_button_click('C'))
        for key in '1234567890+-*/().^%':
            self.root.bind(key, lambda event, char=key: self.on_button_click(char))

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.result.get()  # Get the current expression
                expression = expression.replace('^', '**')  # Replace '^' with '**' for exponentiation
                result = str(eval(expression))  # Evaluate the expression and convert the result to a string
                self.result.set(result)  # Set the result in the entry widget
            except ZeroDivisionError:
                self.result.set("Division by 0 error")  # Handle division by zero error
            except Exception as e:
                self.result.set("Error")  # Handle other errors
        elif char == 'C':
            self.result.set("")  # Clear the result if 'C' is pressed
        elif char == 'M+':
            self.memory = self.result.get()  # Store the current result in memory
        elif char == 'MR':
            if self.memory is not None:
                self.result.set(self.memory)  # Recall the stored value from memory
        elif char == 'MC':
            self.memory = None  # Clear the memory
        elif char == 'M-':
            if self.memory is not None:
                self.result.set(str(eval(self.memory + '-' + self.result.get())))  # Subtract the current result from memory
        else:
            current_text = self.result.get()  # Get the current text in the entry widget
            self.result.set(current_text + char)  # Append the pressed button's character to the current text

if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    calculator = AdvancedCalculator(root)  # Create an instance of the AdvancedCalculator class
    root.mainloop()  # Start the main loop
