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

def additionButton():
    firstVal = outputLabel.get()
    operation_stack.append(int(firstVal))
    outputLabel.delete(0, END)
    titleLabel.insert(0, str(firstVal) + " + ")
    operation_stack.append("+")

def equals():
    operation = titleLabel.get()
    secondVal = outputLabel.get()
    operation_stack.append(int(secondVal))
    outputLabel.delete(0, END)
    titleLabel.delete(0, END)
    titleLabel.insert(0, str(operation) + str(secondVal))

    secondVal = operation_stack.pop()
    operation = operation_stack.pop()
    firstVal = operation_stack.pop()

    if operation == "+":
        result = addition(firstVal, secondVal)

    outputLabel.insert(0, "= " + str(result))

#GUI for calculator

root = Tk()

titleLabel = Entry(root, width=35, borderwidth=5)
inputTemp = Label(root, text="Input:")
inputTemp.grid(row=0, column=0)
titleLabel.grid(row=0, column=1, columnspan=3, padx=10)

outputLabel = Entry(root, width=35, borderwidth=5)
outputTemp = Label(root, text="Output:")
outputTemp.grid(row=1, column=0)
outputLabel.grid(row=1, column=1, columnspan=3, padx=10)

#Percentage Function
percentageButton = Button(root, text="%", padx=38, pady=20)
percentageButton.grid(row=2, column=0)

#Clear entry function
clearEntryButton = Button(root, text="CE", padx=35, pady=20)
clearEntryButton.grid(row=2, column=1)

#Clear all function
clearAllButton = Button(root, text="C", padx=39, pady=20, command=clearAll)
clearAllButton.grid(row=2, column=2)

#Power of two nums function
powerOfMultButton = Button(root, text="x^y", padx=32, pady=20)
powerOfMultButton.grid(row=2, column=3)

#fraction Function
fractionButton = Button(root, text="1/x", padx=35, pady=20)
fractionButton.grid(row=3, column=0)

#Squared function
squaredButton = Button(root, text="x^2", padx=33, pady=20)
squaredButton.grid(row=3, column=1)

#square root function
sqrtButton = Button(root, text="2√x", padx=33, pady=20)
sqrtButton.grid(row=3, column=2)

#division function
powerOfMultButton = Button(root, text="/", padx=40, pady=20)
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
multiplicationButton = Button(root, text="x", padx=39, pady=20)
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
subtractionButton = Button(root, text="-", padx=40, pady=20)
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
additionButton = Button(root, text="+", padx=40, pady=20, command=additionButton)
additionButton.grid(row=6, column=3)

#type Button
typeButton = Button(root, text="+/-", padx=34, pady=20)
typeButton.grid(row=7, column=0)

#0 Button
zeroButton = Button(root, text="0", padx=40, pady=20, command=lambda: clickedButton(0))
zeroButton.grid(row=7, column=1)

#decimal Button
decimalButton = Button(root, text=".", padx=41, pady=20)
decimalButton.grid(row=7, column=2)

#equal function
equalButton = Button(root, text="=", padx=40, pady=20, command=equals)
equalButton.grid(row=7, column=3)

root.mainloop()
