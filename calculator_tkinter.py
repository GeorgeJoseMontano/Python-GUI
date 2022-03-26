from tkinter import *

# function to convert number pressed to display and insert in equation_text
def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

# function to evaluate equation in equation_text
def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""

# function to clear all numbers and equation history
def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

# function to delete last number pressed
def delete():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)

# window setup
window = Tk()
window.title("Calculator - Montano")
window.geometry("300x310")
window.resizable(False, False)

# all numbers and operations are stored in equation_text
equation_text = ""
equation_label = StringVar()

# label for display of equation_text
label = Label(window, textvariable=equation_label, font=("Helvetica", 20), bg="white", width=16, height=1)
label.pack(padx=0 , pady=5)
label.pack()

frame = Frame(window, width=312, height=272.5)
frame.pack()

# Buttons
button1 = Button(frame, text=1, height=2, width=6, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=2, width=6, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=2, width=6, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=2, width=6, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=2, width=6, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=2, width=6, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=2, width=6, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=2, width=6, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=2, width=6, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=2, width=6, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=1)

plus = Button(frame, text='+', height=2, width=6, font=35, command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=2, width=6, font=35, command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=2, width=6, font=35, command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=2, width=6, font=35, command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=2, width=6, font=35, command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=2, width=6, font=35, command=lambda: button_press('.'))
decimal.grid(row=3, column=0)

clear = Button(frame, text='clear', height=2, width=6, font=35, command=clear)
clear.grid(row=4, column=3)           

delete = Button(frame, text='delete', height=2, width=6, font=35, command=delete)
delete.grid(row=4, column=2)

window.mainloop()