# 🧮 Simple Python Calculator

This is a comprehensive calculator program written in Python that performs basic arithmetic operations and advanced scientific computing functions including trigonometric, exponential, root extraction, and logarithmic calculations.

## 🚀 Features

### Basic Arithmetic Operations
- Add two numbers
- Subtract two numbers
- Multiply two numbers
- Divide two numbers (with division by zero handling)

### Scientific Computing Functions
- Calculate power (x**y) - exponential operations
- Extract square root (√x) - root calculation with domain validation for non-negative inputs
- Compute sine (sin x) - trigonometric function for radian input values
- Compute cosine (cos x) - trigonometric function for radian input values
- Calculate natural logarithm (ln x) - logarithmic operations with domain validation for positive inputs

## 📦 Requirements

- Python 3.x
- Python's built-in `math` module (included in standard library)

*Note: This calculator maintains zero third-party dependency philosophy while utilizing Python's standard library math module for advanced scientific operations.*

## 🛠️ How to Run

1. Clone the repository or download the `calculator.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the calculator using:

```bash
python calculator.py
```

## 📋 Usage Instructions

The calculator presents an interactive menu with nine operational choices plus an exit option:

```
Simple Calculator
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power (x**y)
6. Square Root
7. Sine
8. Cosine
9. Logarithm
10. Exit
```

### Operation Types

**Dual-Operand Operations** (require two numbers):
- Addition, Subtraction, Multiplication, Division, Power

**Single-Operand Operations** (require one number):
- Square Root, Sine, Cosine, Logarithm

### Usage Examples

#### Basic Arithmetic
```
Enter your choice (1-10): 1
Enter first number: 15
Enter second number: 25
Result: 15.0 + 25.0 = 40.0
```

#### Scientific Computing
```
Enter your choice (1-10): 6
Enter number: 16
Result: √16.0 = 4.0

Enter your choice (1-10): 7
Enter number (in radians): 1.5708
Result: sin(1.5708) = 1.0

Enter your choice (1-10): 9
Enter number: 2.718
Result: ln(2.718) = 0.999896...
```

### Domain Constraints

- **Square Root**: Input must be non-negative (≥ 0)
- **Logarithm**: Input must be positive (> 0)
- **Trigonometric Functions**: Accept any real number (input in radians)
- **Power Operations**: Accept any real numbers for base and exponent
- **Division**: Divisor cannot be zero

### Error Handling

The calculator provides comprehensive error handling for:
- Invalid numeric input with graceful error recovery
- Division by zero protection
- Mathematical domain violations (negative square roots, non-positive logarithms)
- User-friendly error messages for all edge cases

## 🎯 Educational Purpose

This calculator serves as an educational tool demonstrating:
- Pure function implementation patterns
- Python's math module integration
- Comprehensive input validation and error handling
- Variable-arity function signatures
- Conditional program flow control
- Scientific computing concepts in Python