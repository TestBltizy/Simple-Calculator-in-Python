# 🧮 Simple Python Calculator

This is a comprehensive scientific calculator program written in Python that performs both basic arithmetic operations and advanced scientific computing functions. Originally designed as a basic arithmetic tool, it has been enhanced to serve as an educational programming demonstration showcasing mathematical function implementation and proper error handling practices.

## 🚀 Features

### Basic Arithmetic Operations
- **Addition**: Add two numbers with floating-point precision
- **Subtraction**: Subtract two numbers with accurate difference calculation
- **Multiplication**: Multiply two numbers with mathematical precision
- **Division**: Divide two numbers with comprehensive division-by-zero handling

### Advanced Scientific Computing Capabilities
- **Power Operations**: Calculate exponential values (base^exponent) supporting both integer and floating-point exponents
- **Square Root**: Compute square root calculations with domain validation for non-negative inputs
- **Sine**: Perform trigonometric sine calculations accepting angle values in radians
- **Cosine**: Execute trigonometric cosine calculations accepting angle values in radians
- **Logarithm**: Calculate natural logarithm with domain validation for positive inputs

## 📦 Requirements

- Python 3.x
- Python math module (included in standard library - no external dependencies required)

The calculator maintains a zero external dependency philosophy by utilizing only Python's built-in functions and the standard library math module for scientific operations.

## 🛠️ How to Run

1. Clone the repository or download the `calculator.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the calculator using:

```bash
python calculator.py
```

## 📋 Usage Instructions

The calculator features an interactive menu-driven interface with options 1-9 for comprehensive mathematical operations:

### Menu Options
1. **Addition** - Enter two numbers to add
2. **Subtraction** - Enter two numbers to subtract
3. **Multiplication** - Enter two numbers to multiply
4. **Division** - Enter two numbers to divide
5. **Power** - Enter base and exponent for exponential calculation
6. **Square Root** - Enter a non-negative number for square root calculation
7. **Sine** - Enter an angle in radians for sine calculation
8. **Cosine** - Enter an angle in radians for cosine calculation
9. **Logarithm** - Enter a positive number for natural logarithm calculation
0. **Exit** - Terminate the calculator program

### Mathematical Domain Constraints

**Square Root Operations:**
- Requires non-negative input values (x ≥ 0)
- Negative inputs will result in domain error messaging
- Example: √16 = 4, but √(-4) produces an error

**Logarithm Operations:**
- Requires positive input values (x > 0)
- Zero and negative inputs will result in domain error messaging
- Example: ln(e) ≈ 1, but ln(0) or ln(-1) produces an error

**Trigonometric Operations:**
- Sine and cosine functions accept angle inputs in radians
- No domain constraints - all real number inputs are valid
- For degree-to-radian conversion: radians = degrees × π/180

## 🔢 Scientific Function Usage Examples

### Power Operations
```
Enter base: 2
Enter exponent: 3
Result: 8.0
```

### Square Root Operations
```
Enter number: 25
Result: 5.0
```

### Trigonometric Operations (Radian Input)
```
Sine calculation:
Enter angle in radians: 1.5708  # π/2 radians = 90 degrees
Result: 1.0

Cosine calculation:
Enter angle in radians: 0       # 0 radians = 0 degrees
Result: 1.0
```

### Logarithm Operations
```
Enter number: 2.718281828       # Approximately e
Result: 1.0
```

## 🎯 Educational Purpose

This calculator serves as a practical demonstration of:
- Pure function implementation principles
- Mathematical domain constraint validation
- Comprehensive error handling practices
- Menu-driven console application development
- Integration of Python's standard library modules
- Scientific computing fundamentals for programming education

The project maintains educational simplicity while showcasing enterprise-grade error handling and mathematical accuracy suitable for both learning and practical calculation needs.