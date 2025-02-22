"""
math_utils.py
Basic mathematical operations.
"""

def add(a, b):
    """This returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """This returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """This returns the product of two numbers."""
    return a * b

def divide(a, b):
    """This returns the quotient. Raises an error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
