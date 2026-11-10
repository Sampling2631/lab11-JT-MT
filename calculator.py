"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def logarithm(a, b):
    if a == 1 or a <= 0:
        raise ValueError("Base must be a positive number not equal to one.")
    elif b <= 0:
        raise ValueError("Input must be a positive number.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b
