# Enhanced Scientific Calculator in Python
import math

# This calculator performs basic arithmetic operations and scientific functions:
# Addition, Subtraction, Multiplication, Division, Power, Square Root, 
# Sine, Cosine, and Natural Logarithm

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

# Scientific Functions using math module

def power(x, y):
    """Function to calculate x raised to the power of y"""
    return math.pow(x, y)

def square_root(x):
    """Function to calculate square root with domain validation"""
    if x < 0:
        return "Error! Cannot calculate square root of negative number."
    return math.sqrt(x)

def sine(x):
    """Function to calculate sine of x (in radians)"""
    return math.sin(x)

def cosine(x):
    """Function to calculate cosine of x (in radians)"""
    return math.cos(x)

def logarithm(x):
    """Function to calculate natural logarithm with domain validation"""
    if x <= 0:
        return "Error! Cannot calculate logarithm of zero or negative number."
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
print("9. Logarithm")

# Take user input for operation
choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

# Take user input for numbers based on operation type
try:
    if choice in ['1', '2', '3', '4', '5']:
        # Operations requiring two operands
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    elif choice in ['6', '7', '8', '9']:
        # Operations requiring single operand
        num1 = float(input("Enter number: "))
        num2 = None  # Not needed for single-operand operations
    else:
        print("Invalid input. Please choose a valid operation.")
        exit()
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

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
elif choice == '6':
    print("Result:", square_root(num1))
elif choice == '7':
    print("Result:", sine(num1))
elif choice == '8':
    print("Result:", cosine(num1))
elif choice == '9':
    print("Result:", logarithm(num1))
else:
    print("Invalid input. Please choose a valid operation.")