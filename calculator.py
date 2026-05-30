from tkinter import *

# main window
root = Tk()
root.title("Calculator")
root.geometry("320x400")
root.resizable(False, False)

# variable to store input
calculation = ""

# function for addition
def add(a, b):
    return a + b

# function for subtraction
def subtract(a, b):
    return a - b

# function for multiplication
def multiply(a, b):
    return a * b

# function for division
def divide(a, b):
    if b == 0:
        return "Error"
    return a / b

# function to show values on screen
def press(value):
    global calculation
    calculation += str(value)
    screen_text.set(calculation)

# clear screen
def clear_screen():
    global calculation
    calculation = ""
    screen_text.set("")

# calculate result without eval()
def calculate_result():
    global calculation

    try:
        operator = ""
        first_num = ""
        second_num = ""

        # find operator
        for ch in calculation:
            if ch in "+-*/":
                operator = ch
                break

        # split numbers
        parts = calculation.split(operator)

        first_num = float(parts[0])
        second_num = float(parts[1])

        # call functions
        if operator == "+":
            result = add(first_num, second_num)

        elif operator == "-":
            result = subtract(first_num, second_num)

        elif operator == "*":
            result = multiply(first_num, second_num)

        elif operator == "/":
            result = divide(first_num, second_num)

        screen_text.set(result)
        calculation = str(result)

    except:
        screen_text.set("Error")
        calculation = ""

# display box
screen_text = StringVar()

display = Entry(root,
                textvariable=screen_text,
                font=("Arial", 20),
                justify="right",
                bd=8)

display.grid(row=0, column=0, columnspan=4,
             ipadx=8, ipady=12)

# buttons row 1
Button(root, text="7", width=7, height=3,
       command=lambda: press(7)).grid(row=1, column=0)

Button(root, text="8", width=7, height=3,
       command=lambda: press(8)).grid(row=1, column=1)

Button(root, text="9", width=7, height=3,
       command=lambda: press(9)).grid(row=1, column=2)

Button(root, text="/", width=7, height=3,
       command=lambda: press("/")).grid(row=1, column=3)

# row 2
Button(root, text="4", width=7, height=3,
       command=lambda: press(4)).grid(row=2, column=0)

Button(root, text="5", width=7, height=3,
       command=lambda: press(5)).grid(row=2, column=1)

Button(root, text="6", width=7, height=3,
       command=lambda: press(6)).grid(row=2, column=2)

Button(root, text="*", width=7, height=3,
       command=lambda: press("*")).grid(row=2, column=3)

# row 3
Button(root, text="1", width=7, height=3,
       command=lambda: press(1)).grid(row=3, column=0)

Button(root, text="2", width=7, height=3,
       command=lambda: press(2)).grid(row=3, column=1)

Button(root, text="3", width=7, height=3,
       command=lambda: press(3)).grid(row=3, column=2)

Button(root, text="-", width=7, height=3,
       command=lambda: press("-")).grid(row=3, column=3)

# row 4
Button(root, text="C", width=7, height=3,
       command=clear_screen).grid(row=4, column=0)

Button(root, text="0", width=7, height=3,
       command=lambda: press(0)).grid(row=4, column=1)

Button(root, text="=", width=7, height=3,
       command=calculate_result).grid(row=4, column=2)

Button(root, text="+", width=7, height=3,
       command=lambda: press("+")).grid(row=4, column=3)

root.mainloop()