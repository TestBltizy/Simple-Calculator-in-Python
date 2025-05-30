# Enhanced Scientific Calculator in Python
import math

# This calculator performs arithmetic and scientific operations:
# Addition, Subtraction, Multiplication, Division, Power, Square Root, Sine, Cosine, and Logarithm

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

def power(x, y):
    """Function to raise first number to the power of second number"""
    return math.pow(x, y)

def square_root(x):
    """Function to calculate square root of a number"""
    if x < 0:
        return "Error! Cannot compute square root of negative number."
    return math.sqrt(x)

def sine(x):
    """Function to calculate sine of a number (in radians)"""
    return math.sin(x)

def cosine(x):
    """Function to calculate cosine of a number (in radians)"""
    return math.cos(x)

def logarithm(x):
    """Function to calculate natural logarithm of a number"""
    if x <= 0:
        return "Error! Logarithm undefined for non-positive values."
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
        # Two-operand operations (arithmetic and power)
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    elif choice in ['6', '7', '8', '9']:
        # Single-operand operations (scientific functions)
        num1 = float(input("Enter number: "))
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