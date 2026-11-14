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

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('value b cannot be 0.')
    return b / a

def logarithm(a, b):
    if a == 1 or a <= 0:
        raise ValueError("Base must be a positive number not equal to one.")
    elif b <= 0:
        raise ValueError("Input must be a positive number.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)
