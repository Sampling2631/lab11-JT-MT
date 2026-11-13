"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example

import math

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('value b cannot be 0.')
    return b / a

def log(a, b):
    if a <= 0:
        raise ValueError('invalid base cannot be 0 or negative')
    if a == 1:
        raise ValueError('invalid base cannot be 1')
    return math.log(b, a)

def exp(a, b):
    return a ** b
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a == 1 or a <= 0:
        raise ValueError("Base must be a positive number not equal to one.")
    elif b <= 0:
        raise ValueError("Input must be a positive number.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b
