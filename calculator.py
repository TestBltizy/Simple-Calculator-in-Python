# Simple Calculator in Python

# This calculator performs basic arithmetic operations:
# Addition, Subtraction, Multiplication, and Division

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

# Display available operations
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take user input for operation
choice = input("Enter choice (1/2/3/4): ")

# Take user input for numbers
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
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
else:
    print("Invalid input. Please choose a valid operation.")
