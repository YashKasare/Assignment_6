from tkinter import *

# Function to update expression
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate final expression
def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total

    except:
        equation.set("Error")
        expression = ""

# Function to clear the entry field
def clear():
    global expression
    expression = ""
    equation.set("")

# Main window
if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="light blue")

    gui.title("Calculator")

    gui.geometry("300x400")

    expression = ""

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation, font=('Arial', 20), justify='right')
    expression_field.grid(columnspan=4, ipadx=8, ipady=15)

    # Number buttons
    Button(gui, text='1', fg='black', bg='white',
           command=lambda: press(1), height=2, width=7).grid(row=2, column=0)

    Button(gui, text='2', fg='black', bg='white',
           command=lambda: press(2), height=2, width=7).grid(row=2, column=1)

    Button(gui, text='3', fg='black', bg='white',
           command=lambda: press(3), height=2, width=7).grid(row=2, column=2)

    Button(gui, text='+', fg='black', bg='orange',
           command=lambda: press("+"), height=2, width=7).grid(row=2, column=3)

    Button(gui, text='4', fg='black', bg='white',
           command=lambda: press(4), height=2, width=7).grid(row=3, column=0)

    Button(gui, text='5', fg='black', bg='white',
           command=lambda: press(5), height=2, width=7).grid(row=3, column=1)

    Button(gui, text='6', fg='black', bg='white',
           command=lambda: press(6), height=2, width=7).grid(row=3, column=2)

    Button(gui, text='-', fg='black', bg='orange',
           command=lambda: press("-"), height=2, width=7).grid(row=3, column=3)

    Button(gui, text='7', fg='black', bg='white',
           command=lambda: press(7), height=2, width=7).grid(row=4, column=0)

    Button(gui, text='8', fg='black', bg='white',
           command=lambda: press(8), height=2, width=7).grid(row=4, column=1)

    Button(gui, text='9', fg='black', bg='white',
           command=lambda: press(9), height=2, width=7).grid(row=4, column=2)

    Button(gui, text='*', fg='black', bg='orange',
           command=lambda: press("*"), height=2, width=7).grid(row=4, column=3)

    Button(gui, text='C', fg='black', bg='red',
           command=clear, height=2, width=7).grid(row=5, column=0)

    Button(gui, text='0', fg='black', bg='white',
           command=lambda: press(0), height=2, width=7).grid(row=5, column=1)

    Button(gui, text='=', fg='black', bg='green',
           command=equalpress, height=2, width=7).grid(row=5, column=2)

    Button(gui, text='/', fg='black', bg='orange',
           command=lambda: press("/"), height=2, width=7).grid(row=5, column=3)

    gui.mainloop()