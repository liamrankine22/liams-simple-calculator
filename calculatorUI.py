##################################################################
#|--------------------------------------------------------------|#
#| NAME: calculatorUI.py                                        |#
#|                                                              |#
#| AUTHOR: Liam Rankine                                         |#
#|                                                              |#
#| DESCRIPTION: Graphical User Interface for the calculator     |#
#|                                                              |#
#| NOTES:                                                       |#
#|                                                              |#
#| DATE:                                                        |#
#|______________________________________________________________|#
##################################################################

from calculatorArithmetic import *
from tkinter import *

#Methods for calculator functionality
operation_stack = []

def clickedButton(value):
    currentVal = outputLabel.get()
    outputLabel.delete(0, END)
    outputLabel.insert(0, str(currentVal) + str(value))

def clearAll():
    outputLabel.delete(0, END)
    titleLabel.delete(0, END)

    while(len(operation_stack) != 0):
        operation_stack.pop()

def clearEntry():
    outputLabel.delete(0,END)

def typeFunction():
    currentVal = outputLabel.get()
    outputLabel.delete(0, END)
    firstChar = currentVal[0]
    if firstChar != "-":
        outputLabel.insert(0, "-" + currentVal)

    else:
        currentVal = currentVal.replace('-', '')
        outputLabel.insert(0, currentVal)

def decimalFunction():
    currentVal = outputLabel.get()
    outputLabel.delete(0, END)
    outputLabel.insert(0, currentVal + ".")

def additionFunction():
    firstVal = outputLabel.get()
    operation_stack.append(float(firstVal))
    outputLabel.delete(0, END)
    titleLabel.insert(0, str(firstVal) + " + ")
    operation_stack.append("+")

def subtrationFunction():
    firstVal = outputLabel.get()
    operation_stack.append(float(firstVal))
    outputLabel.delete(0, END)
    titleLabel.insert(0, str(firstVal) + " - ")
    operation_stack.append("-")

def multiplicationFunction():
    firstVal = outputLabel.get()
    operation_stack.append(float(firstVal))
    outputLabel.delete(0, END)
    titleLabel.insert(0, str(firstVal) + " x ")
    operation_stack.append("*")

def divisionFunction():
    firstVal = outputLabel.get()
    operation_stack.append(float(firstVal))
    outputLabel.delete(0, END)
    titleLabel.insert(0, str(firstVal) + " / ")
    operation_stack.append("/")

def squaredFunction():
    firstVal = outputLabel.get()
    outputLabel.delete(0, END)
    titleLabel.insert(0, str(firstVal) + "^2")
    result = squared(float(firstVal))
    outputLabel.insert(0, "= " + str(result))

def powerOfTwoNums():
    firstVal = outputLabel.get()
    operation_stack.append(float(firstVal))
    outputLabel.delete(0, END)
    titleLabel.insert(0, str(firstVal) + "^")
    operation_stack.append("^")

def squareRootFunction():
    firstVal = outputLabel.get()
    operation_stack.append(float(firstVal))
    outputLabel.delete(0, END)
    titleLabel.insert(0, "2√" + str(firstVal))
    result = squareroot(float(firstVal))
    outputLabel.insert(0, "= " + str(result))

def fractionFunction():
    firstVal=outputLabel.get()
    title=titleLabel.get()
    outputLabel.delete(0, END)
    firstVal = fraction(float(firstVal))
    titleLabel.insert(0, title + str(firstVal))

def percentageFunction():
    firstVal=outputLabel.get()
    title=titleLabel.get()
    outputLabel.delete(0, END)
    firstVal = percentage(float(firstVal))
    outputLabel.insert(0, title + str(firstVal))

def equals():
    operation = titleLabel.get()
    secondVal = outputLabel.get()
    operation_stack.append(float(secondVal))
    outputLabel.delete(0, END)
    titleLabel.delete(0, END)
    titleLabel.insert(0, str(operation) + str(secondVal))

    secondVal = operation_stack.pop()
    operation = operation_stack.pop()
    firstVal = operation_stack.pop()

    if operation == "+":
        result = addition(firstVal, secondVal)

    elif operation == "-":
        result = subtraction(firstVal, secondVal)

    elif operation == "*":
        result = multiplication(firstVal, secondVal)

    elif operation == "/":
        result = division(firstVal, secondVal)

    elif operation == "^":
        result = exponent(firstVal, secondVal)


    outputLabel.insert(0, "= " + str(result))

#GUI for calculator

root = Tk()

titleLabel = Entry(root, width=35, borderwidth=5)
inputTemp = Label(root, text="Formula:")
inputTemp.grid(row=0, column=0)
titleLabel.grid(row=0, column=1, columnspan=3, padx=10)

outputLabel = Entry(root, width=35, borderwidth=5)
outputTemp = Label(root, text="Input/Output:")
outputTemp.grid(row=1, column=0)
outputLabel.grid(row=1, column=1, columnspan=3, padx=10)

#Percentage Function
percentageButton = Button(root, text="%", padx=38, pady=20, command=percentageFunction)
percentageButton.grid(row=2, column=0)

#Clear entry function
clearEntryButton = Button(root, text="CE", padx=35, pady=20, command=clearEntry)
clearEntryButton.grid(row=2, column=1)

#Clear all function
clearAllButton = Button(root, text="C", padx=39, pady=20, command=clearAll)
clearAllButton.grid(row=2, column=2)

#Power of two nums function
powerOfMultButton = Button(root, text="x^y", padx=32, pady=20, command=powerOfTwoNums)
powerOfMultButton.grid(row=2, column=3)

#fraction Function
fractionButton = Button(root, text="1/x", padx=34, pady=20, command=fractionFunction)
fractionButton.grid(row=3, column=0)

#Squared function
squaredButton = Button(root, text="x^2", padx=32, pady=20, command=squaredFunction)
squaredButton.grid(row=3, column=1)

#square root function
sqrtButton = Button(root, text="2√x", padx=33, pady=20, command=squareRootFunction)
sqrtButton.grid(row=3, column=2)

#division function
powerOfMultButton = Button(root, text="/", padx=40, pady=20, command=divisionFunction)
powerOfMultButton.grid(row=3, column=3)

#7 Button
sevenButton = Button(root, text="7", padx=40, pady=20, command=lambda: clickedButton(7))
sevenButton.grid(row=4, column=0)

#8 Button
eightButton = Button(root, text="8", padx=40, pady=20, command=lambda: clickedButton(8))
eightButton.grid(row=4, column=1)

#9 Button
nineButton = Button(root, text="9", padx=40, pady=20, command=lambda: clickedButton(9))
nineButton.grid(row=4, column=2)

#multiplication function
multiplicationButton = Button(root, text="x", padx=39, pady=20, command=multiplicationFunction)
multiplicationButton.grid(row=4, column=3)

#4 Button
fourButton = Button(root, text="4", padx=40, pady=20, command=lambda: clickedButton(4))
fourButton.grid(row=5, column=0)

#5 Button
fiveButton = Button(root, text="5", padx=40, pady=20, command=lambda: clickedButton(5))
fiveButton.grid(row=5, column=1)

#6 Button
sixButton = Button(root, text="6", padx=40, pady=20, command=lambda: clickedButton(6))
sixButton.grid(row=5, column=2)

#subtraction function
subtractionButton = Button(root, text="-", padx=40, pady=20, command=subtrationFunction)
subtractionButton.grid(row=5, column=3)

#1 Button
oneButton = Button(root, text="1", padx=40, pady=20, command=lambda: clickedButton(1))
oneButton.grid(row=6, column=0)

#2 Button
twoButton = Button(root, text="2", padx=40, pady=20, command=lambda: clickedButton(2))
twoButton.grid(row=6, column=1)

#3 Button
threeButton = Button(root, text="3", padx=40, pady=20, command=lambda: clickedButton(3))
threeButton.grid(row=6, column=2)

#addition function
additionButton = Button(root, text="+", padx=39, pady=20, command=additionFunction)
additionButton.grid(row=6, column=3)

#type Button
typeButton = Button(root, text="+/-", padx=34, pady=20, command=typeFunction)
typeButton.grid(row=7, column=0)

#0 Button
zeroButton = Button(root, text="0", padx=40, pady=20, command=lambda: clickedButton(0))
zeroButton.grid(row=7, column=1)

#decimal Button
decimalButton = Button(root, text=".", padx=42, pady=20, command=decimalFunction)
decimalButton.grid(row=7, column=2)

#equal function
equalButton = Button(root, text="=", padx=39, pady=20, command=equals)
equalButton.grid(row=7, column=3)

#History Buttons
x = "0 + 0 = 0"
history_entry_one = Label(root, text="HISTORY", padx=40, pady=20)
history_entry_one.grid(row= 0, column= 4)
history_entry_two = Button(root, text="TEMP", padx=40, pady=20)
history_entry_two.grid(row= 1, column= 4)
history_entry_three = Button(root, text="TEMP", padx=40, pady=20)
history_entry_three.grid(row= 2, column= 4)
history_entry_four = Button(root, text="TEMP", padx=40, pady=20)
history_entry_four.grid(row= 3, column= 4)
history_entry_five = Button(root, text="TEMP", padx=40, pady=20)
history_entry_five.grid(row= 4, column= 4)
history_entry_six = Button(root, text="TEMP", padx=40, pady=20)
history_entry_six.grid(row= 5, column= 4)
history_entry_seven = Button(root, text="TEMP", padx=40, pady=20)
history_entry_seven.grid(row= 6, column= 4)
history_entry_eight = Button(root, text="TEMP", padx=40, pady=20)
history_entry_eight.grid(row= 7, column= 4)

title_terminal = Label(root, text="Terminal")
title_terminal.grid(row=8, columnspan=5)

terminal = Entry(root, width=70, borderwidth=5)
terminal.grid(row=9, columnspan=5)


root.mainloop()
