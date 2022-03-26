from tkinter import *

# function to convert from fahrenheit to celsius and kelvin and display
def convert_fahr():
    words = temptext.get()
    ftemp = float(words)
    fahrbox.delete(0, END)
    fahrbox.insert(0, ftemp)
    celbox.delete(0, END)
    celbox.insert(0, '%.2f' % (tocel(ftemp)))
    kelbox.delete(0, END)
    kelbox.insert(0, '%.2f' % (tokel(tocel(ftemp))))
    return

# function to convert from celsius to fahrenheit and kelvin and display
def convert_cel():
    words = temptext.get()
    ctemp = float(words)
    fahrbox.delete(0, END)
    fahrbox.insert(0, '%.2f' % (tofahr(ctemp)))
    celbox.delete(0, END)
    celbox.insert(0, ctemp)
    kelbox.delete(0, END)
    kelbox.insert(0, '%.2f' % (tokel(ctemp)))
    return

# function to convert from kelvin to fahrenheit and celsius and display
def convert_kel():
    words = temptext.get()
    ktemp = float(words)
    fahrbox.delete(0, END)
    fahrbox.insert(0, '%.2f' % (tofahr(ktoc(ktemp))))
    celbox.delete(0, END)
    celbox.insert(0, '%.2f' % (ktoc(ktemp)))
    kelbox.delete(0, END)
    kelbox.insert(0, ktemp)
    return

#function to convert from x temp to y temp
def tocel(fahr):
    return (fahr-32) * 5.0 / 9.0

def tofahr(cel):
    return cel * 9.0 / 5.0 + 32

def ktoc(kel):
    return kel - 273.15

def tokel(cel):
    return cel + 273.15

# window setup
window = Tk()
window.title('Temperature Converter - Montano')
window.geometry("220x180")
window.resizable(False, False)

# labels
templabel = Label(window, text = 'Temperature')
templabel.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

fahrlabel = Label(window, text = 'Fahrenheit')
fahrlabel.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = E)

cellabel = Label(window, text = 'Celsius')
cellabel.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = E)

kellabel = Label(window, text = 'Kelvin')
kellabel.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = E)

# text boxes
temptext = StringVar()
temptext.set(0)
tempbox = Entry(window, textvariable=temptext)
tempbox.grid(row = 0, column = 1, padx = 5, pady = 5)

fbtext = StringVar()
fbtext.set(0)
fahrbox = Entry(window, textvariable=fbtext, )
fahrbox.grid(row = 2, column = 1, padx = 5, pady = 5)

cbtext = StringVar()
cbtext.set(0)
celbox = Entry(window, textvariable=cbtext)
celbox.grid(row = 3, column = 1, padx = 5, pady = 5)

kbtext = StringVar()
kbtext.set(0)
kelbox = Entry(window, textvariable=kbtext)
kelbox.grid(row = 4, column = 1, padx = 5, pady = 5)

# buttons
fgobutton = Button(window, text = 'Fahrenheit', command = convert_fahr, height=1, width=8)
fgobutton.grid(row = 1, column = 0, sticky = E)

cgobutton = Button(window, text = 'Celsius', command = convert_cel, height=1, width=7)
cgobutton.grid(row = 1, column = 1, padx = 5,  sticky = W)

kgobutton = Button(window, text = 'Kelvin', command = convert_kel, height=1, width=7)
kgobutton.grid(row = 1, column = 1, padx = 5, sticky = E)

window.mainloop()