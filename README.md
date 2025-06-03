# 🧮 Scientific Python Calculator

This is an enhanced scientific calculator program written in Python that performs both basic arithmetic operations and advanced scientific mathematical functions including exponential calculations, trigonometric operations, and logarithmic computations.

## 🚀 Features

### Basic Arithmetic Operations
- Add two numbers
- Subtract two numbers
- Multiply two numbers
- Divide two numbers (with division by zero handling)

### Scientific Operations
- **Power (Exponential)**: Calculate x raised to the power of y using high-precision math computation
- **Square Root**: Compute square root with domain validation (non-negative values only)
- **Sine**: Calculate trigonometric sine values for angles in radians
- **Cosine**: Calculate trigonometric cosine values for angles in radians
- **Natural Logarithm**: Compute natural logarithm with domain validation (positive values only)

## 📦 Requirements

- Python 3.x
- Python's built-in `math` module (included in standard Python installations)

## 🛠️ How to Run

1. Clone the repository or download the `calculator.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the calculator using:

```bash
python calculator.py
```

## 📋 Usage Instructions

The calculator presents an interactive menu with **9 operation options**:

### Basic Arithmetic (Options 1-4)
1. **Add** - Addition of two numbers
2. **Subtract** - Subtraction of two numbers  
3. **Multiply** - Multiplication of two numbers
4. **Divide** - Division of two numbers (with zero-division protection)

### Scientific Computing (Options 5-9)
5. **Power** - Calculate x^y (exponential calculations)
6. **Square Root** - Calculate √x (requires non-negative input)
7. **Sine** - Calculate sin(x) where x is in radians
8. **Cosine** - Calculate cos(x) where x is in radians
9. **Logarithm** - Calculate ln(x) natural logarithm (requires positive input)

### Operation Examples:
```
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square Root
7. Sine
8. Cosine
9. Logarithm

Enter choice (1/2/3/4/5/6/7/8/9): 5
Enter first number: 2
Enter second number: 3
Result: 8.0

Enter choice (1/2/3/4/5/6/7/8/9): 7
Enter number: 1.5708
Result: 1.0
```

## 📚 Educational Notes

### Mathematical Concepts
- **Radian Trigonometry**: The sine and cosine functions use radian measurement. To convert degrees to radians: `radians = degrees × π ÷ 180`
- **Domain Restrictions**: 
  - Square root function requires non-negative inputs (x ≥ 0)
  - Natural logarithm function requires positive inputs (x > 0)
- **Scientific Notation**: Results for very large or very small numbers are automatically displayed in scientific notation format

### Learning Objectives
This calculator demonstrates:
- Function implementation patterns in Python
- Integration of Python's standard library (math module)
- Input validation and error handling techniques
- Domain-specific validation for mathematical operations
- User interface design with menu-driven interaction
- Scientific computing fundamentals and mathematical precision

### Error Handling
The calculator provides educational examples of robust error handling:
- Division by zero protection with descriptive error messages
- Domain validation for mathematical functions (e.g., "Error: Cannot calculate square root of negative number")
- Input validation for numeric data with graceful error recovery
- Mathematical domain errors handled without program crashes

## 🔧 Technical Implementation

- **Single-file architecture** maintaining educational simplicity
- **Zero external dependencies** using only Python standard library
- **Comprehensive error handling** for educational demonstration
- **Clear code organization** with separated arithmetic and scientific function groups
- **Consistent interface design** across all nine mathematical operations