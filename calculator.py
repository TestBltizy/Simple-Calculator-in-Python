# Simple Scientific Calculator in Python
# This calculator performs both basic arithmetic and scientific operations
# Arithmetic: Addition, Subtraction, Multiplication, Division
# Scientific: Power, Square Root, Sine, Cosine, Natural Logarithm

import math

# Basic Arithmetic Operations
def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract second number from first"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide first number by second"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Scientific Operations
def power(x, y):
    """Function to calculate x raised to the power of y"""
    return x ** y

def sqrt(x):
    """Function to calculate square root of x
    Domain: x >= 0 (non-negative numbers only)"""
    if x < 0:
        return "Error! Square root requires non-negative values."
    return math.sqrt(x)

def sine(x):
    """Function to calculate sine of x (x in radians)"""
    return math.sin(x)

def cosine(x):
    """Function to calculate cosine of x (x in radians)"""
    return math.cos(x)

def logarithm(x):
    """Function to calculate natural logarithm of x
    Domain: x > 0 (positive numbers only)"""
    if x <= 0:
        return "Error! Logarithm requires positive values."
    return math.log(x)

# Display available operations
print("Select operation:")
print("1. Add")
print("2. Subtract") 
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")
print("7. Sine")
print("8. Cosine")
print("9. Natural Logarithm")

# Take user input for operation
choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

# Validate menu choice
if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
    print("Invalid input. Please choose a valid operation.")
    exit()

# Handle input based on operation type (binary vs unary)
try:
    if choice in ['1', '2', '3', '4', '5']:  # Binary operations requiring two operands
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Perform calculation based on user's choice
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
            
    elif choice in ['6', '7', '8', '9']:  # Unary operations requiring single operand
        num1 = float(input("Enter number: "))
        
        # Perform calculation based on user's choice
        if choice == '6':
            print("Result:", sqrt(num1))
        elif choice == '7':
            print("Result:", sine(num1))
        elif choice == '8':
            print("Result:", cosine(num1))
        elif choice == '9':
            print("Result:", logarithm(num1))
            
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()