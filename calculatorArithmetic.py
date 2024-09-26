##################################################################
#|--------------------------------------------------------------|#
#| NAME: calculatorArithmetic.py                                |#
#|                                                              |#
#| AUTHOR: Liam Rankine                                         |#
#|                                                              |#
#| DESCRIPTION: All arithmetic functions used by the calculator |#
#|                                                              |#
#| NOTES:                                                       |#
#|                                                              |#
#| DATE:                                                        |#
#|______________________________________________________________|#
##################################################################

from math import sqrt

def addition(valOne, valTwo):
    result = valOne + valTwo
    return result

def subtraction(valOne, valTwo):
    result = valOne - valTwo
    return result

def multiplication(valOne, valTwo):
    result = valOne * valTwo
    return result

def division(valOne, valTwo):
    try:
        result = valOne / valTwo
        return result

    except ZeroDivisionError:
        print("Error: Divison By 0")
        return

def fraction(valOne):
    result = 1/valOne
    return result

def squared(valOne):
    result = valOne ** 2
    return result

def squareroot(valOne):
    result = sqrt(valOne)
    return result

def exponent(valOne, valTwo):
    result = valOne ** valTwo
    return result

def percentage(val):
    result = val / 100
    return result