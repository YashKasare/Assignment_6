# Simple Calculator using Tkinter

from tkinter import *

# creating main window
window = Tk()
window.title("Simple Calculator")
window.geometry("320x420")
window.resizable(False, False)

# variable to store expression
calculation = ""

# function to add values on screen
def click(number):
    global calculation
    calculation = calculation + str(number)
    input_text.set(calculation)

# function to clear screen
def clear_screen():
    global calculation
    calculation = ""
    input_text.set("")

# function to calculate result
def calculate():
    global calculation
    try:
        answer = str(eval(calculation))
        input_text.set(answer)
        calculation = answer
    except:
        input_text.set("Error")
        calculation = ""

# variable for entry box
input_text = StringVar()

# display box
display = Entry(window, textvariable=input_text,
                font=("Arial", 20),
                justify="right",
                bd=10)
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=12)

# buttons
Button(window, text="7", width=7, height=3,
       command=lambda: click(7)).grid(row=1, column=0)

Button(window, text="8", width=7, height=3,
       command=lambda: click(8)).grid(row=1, column=1)

Button(window, text="9", width=7, height=3,
       command=lambda: click(9)).grid(row=1, column=2)

Button(window, text="/", width=7, height=3,
       command=lambda: click("/")).grid(row=1, column=3)

Button(window, text="4", width=7, height=3,
       command=lambda: click(4)).grid(row=2, column=0)

Button(window, text="5", width=7, height=3,
       command=lambda: click(5)).grid(row=2, column=1)

Button(window, text="6", width=7, height=3,
       command=lambda: click(6)).grid(row=2, column=2)

Button(window, text="*", width=7, height=3,
       command=lambda: click("*")).grid(row=2, column=3)

Button(window, text="1", width=7, height=3,
       command=lambda: click(1)).grid(row=3, column=0)

Button(window, text="2", width=7, height=3,
       command=lambda: click(2)).grid(row=3, column=1)

Button(window, text="3", width=7, height=3,
       command=lambda: click(3)).grid(row=3, column=2)

Button(window, text="-", width=7, height=3,
       command=lambda: click("-")).grid(row=3, column=3)

Button(window, text="C", width=7, height=3,
       command=clear_screen).grid(row=4, column=0)

Button(window, text="0", width=7, height=3,
       command=lambda: click(0)).grid(row=4, column=1)

Button(window, text="=", width=7, height=3,
       command=calculate).grid(row=4, column=2)

Button(window, text="+", width=7, height=3,
       command=lambda: click("+")).grid(row=4, column=3)

# run window
window.mainloop()
