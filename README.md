# 🧮 Scientific Python Calculator

This is a comprehensive scientific calculator program written in Python that performs both basic arithmetic operations and advanced mathematical computations including trigonometric functions, logarithmic calculations, and power operations. The calculator transforms from a basic arithmetic utility into a complete mathematical tool while maintaining zero external dependencies beyond Python's standard library.

## 🚀 Features

### Basic Arithmetic Operations
- Add two numbers
- Subtract two numbers
- Multiply two numbers
- Divide two numbers (with division by zero handling)

### Scientific Mathematical Functions
- **Power Operations**: Calculate x raised to the power of y (x**y)
- **Square Root**: Extract square root with domain validation (non-negative inputs only)
- **Trigonometric Functions**: 
  - Sine calculations (input in radians)
  - Cosine calculations (input in radians)
- **Logarithmic Computations**: Natural logarithm with positive value validation

### System Features
- Interactive menu-driven interface with 9 mathematical operations
- Comprehensive error handling including mathematical domain validation
- Intelligent input collection (two operands for arithmetic/power, single operand for scientific functions)
- Domain constraint protection (square root ≥ 0, logarithm > 0)

## 📦 Requirements

- Python 3.x
- Python's built-in `math` module (part of standard library - no external dependencies required)

## 🛠️ How to Run

1. Clone the repository or download the `calculator.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the calculator using:

```bash
python calculator.py
