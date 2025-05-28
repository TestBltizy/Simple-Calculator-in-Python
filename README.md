# 🧮 Simple Python Calculator

This is a comprehensive scientific calculator program written in Python that performs both basic arithmetic operations and advanced scientific computations. The calculator has been enhanced from a basic arithmetic tool to support a wide range of mathematical operations including trigonometric functions, logarithmic calculations, power operations, and access to fundamental mathematical constants.

## 🚀 Features

### Basic Arithmetic Operations
- Add two numbers
- Subtract two numbers
- Multiply two numbers
- Divide two numbers (with division by zero handling)

### Scientific Operations
- **Power Operations**: Calculate x raised to the power of y (x**y)
- **Square Root**: Calculate square root of a number (requires non-negative input)
- **Trigonometric Functions**: 
  - Sine function (sin) - input in radians
  - Cosine function (cos) - input in radians
- **Logarithmic Functions**: Natural logarithm (ln) - requires positive input
- **Mathematical Constants**: Access to π (pi) and e through Python's math module

### Error Handling & Validation
- Comprehensive input validation for all operations
- Domain-specific validation for scientific operations:
  - Square root operations require non-negative inputs (x ≥ 0)
  - Logarithm operations require positive inputs (x > 0)
- Division by zero protection with clear error messaging
- Graceful error recovery with session continuation capability

## 📦 Requirements

- **Python 3.x interpreter** (required)
- **Python standard library** including the math module (included with Python)
- **No external dependencies** - uses only Python's built-in capabilities

## 🛠️ How to Run

1. Clone the repository or download the `calculator.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the calculator using:

```bash
python calculator.py
```

## 📋 Usage Instructions

The calculator presents an interactive menu with 9 operation options:

```
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power (x**y)
6. Square Root
7. Sine
8. Cosine
9. Natural Logarithm
```

### Basic Operations (1-4)
For basic arithmetic operations, you'll be prompted to enter two numbers:
```
Enter first number: 10
Enter second number: 5
Result: 15.0
```

### Scientific Operations (5-9)

#### Power Operation (Option 5)
```
Enter base number: 2
Enter exponent: 3
Result: 8.0
```

#### Single-Operand Operations (Options 6-9)
For square root, trigonometric, and logarithmic functions:
```
Enter number: 16
Result: 4.0
```

## 🔬 Scientific Calculation Examples

### Square Root Calculation
```
Select operation: 6
Enter number: 25
Result: 5.0
```

### Trigonometric Calculations
```
Select operation: 7 (Sine)
Enter angle in radians: 1.5708  # π/2 radians = 90 degrees
Result: 1.0
```

### Logarithmic Calculations
```
Select operation: 9
Enter number: 2.718281828  # approximately e
Result: 1.0
```

## ⚠️ Error Handling Examples

### Domain Validation Errors

**Square Root with Negative Input:**
```
Select operation: 6
Enter number: -4
Error: Square root requires non-negative input (x ≥ 0)
```

**Logarithm with Non-Positive Input:**
```
Select operation: 9
Enter number: -1
Error: Logarithm requires positive input (x > 0)
```

**Division by Zero:**
```
Select operation: 4
Enter first number: 10
Enter second number: 0
Error: Cannot divide by zero
```

## 🏗️ Architecture

The calculator maintains a **stateless computational model** where each calculation represents an independent transaction. Key architectural features include:

- **Single-file implementation** (`calculator.py`) for maximum portability
- **Procedural programming approach** for educational clarity
- **Zero external dependencies** beyond Python standard library
- **Comprehensive error handling** with graceful recovery
- **Interactive command-line interface** using stdin/stdout
- **Math module integration** for scientific operations while maintaining simplicity

## 🔧 Technical Implementation

### Mathematical Constants
The calculator provides access to fundamental mathematical constants through Python's math module:
- **π (pi)**: `math.pi` - approximately 3.14159
- **e**: `math.e` - approximately 2.71828

### Domain Validation
Scientific operations include built-in domain validation:
- **Square root**: Validates input ≥ 0 before calculation
- **Natural logarithm**: Validates input > 0 before calculation
- **All operations**: Include comprehensive error handling for invalid inputs

### Session Management
- Each calculation operates independently without persistent state
- Error conditions allow session continuation for recoverable errors
- Invalid numeric inputs result in graceful application termination with clear error messages

## 🎯 Educational Value

This calculator serves as an excellent educational tool demonstrating:
- **Python programming fundamentals** including functions, conditionals, and loops
- **Error handling best practices** with try-catch mechanisms
- **Mathematical computation** using Python's standard library
- **User interface design** through command-line interaction patterns
- **Input validation techniques** for robust application development

## 🚀 Getting Started

No installation or configuration required! Simply ensure you have Python 3.x installed on your system and run the calculator directly. The program is designed for immediate deployment in any Python-enabled environment while maintaining universal compatibility across different operating systems.