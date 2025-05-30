# 🧮 Educational Scientific Calculator

This is an enhanced educational calculator program written in Python that performs comprehensive mathematical operations including basic arithmetic and advanced scientific functions. The application serves as a practical demonstration tool for programming education while providing access to essential mathematical computing capabilities through Python's built-in math module.

## 🚀 Features

### Basic Arithmetic Operations (4 operations)
- **Addition**: Add two numbers with floating-point precision
- **Subtraction**: Subtract two numbers with full decimal support
- **Multiplication**: Multiply two numbers with accurate results
- **Division**: Divide two numbers with division by zero protection

### Advanced Scientific Operations (5 operations)
- **Power**: Calculate x raised to the power of y using exponentiation (x**y)
- **Square Root**: Compute square root using math.sqrt() with negative input validation
- **Sine**: Calculate sine of angle in radians using math.sin()
- **Cosine**: Calculate cosine of angle in radians using math.cos()
- **Logarithm**: Compute natural logarithm using math.log() with domain validation

### Additional Features
- **Enhanced Error Handling**: Domain-specific validation for scientific functions
- **Interactive Menu System**: User-friendly 9-option menu navigation
- **Educational Error Messages**: Descriptive guidance for mathematical constraints
- **Session Management**: Continuous operation with graceful exit option

## 📦 Requirements

- **Python 3.x**: Any version supporting the standard library
- **Math Module**: Integrated from Python standard library (no external dependencies)

## 🛠️ How to Run

1. Clone the repository or download the `calculator.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the calculator using:

```bash
python calculator.py
```

## 🎯 Usage

When you run the calculator, you'll see a menu with 9 mathematical operations plus an exit option:

```
Scientific Calculator Menu:
1. Addition
2. Subtraction  
3. Multiplication
4. Division
5. Power (x^y)
6. Square Root
7. Sine (radians)
8. Cosine (radians)
9. Logarithm (natural log)
10. Exit

Select an operation (1-10):
```

### Example Usage

**Basic Arithmetic Example:**
```
Select operation: 1
Enter first number: 15.5
Enter second number: 4.5
Result: 15.5 + 4.5 = 20.0
```

**Scientific Function Example:**
```
Select operation: 7
Enter angle in radians: 1.5708
Result: sin(1.5708) = 1.0
```

## 🔬 Scientific Functions

### Important Notes for Scientific Operations

**Trigonometric Functions (Sine & Cosine):**
- Input values must be in **radians**, not degrees
- To convert degrees to radians: radians = degrees × π/180
- Common radian values: π/2 ≈ 1.5708, π ≈ 3.1416, 2π ≈ 6.2832

**Domain Constraints:**
- **Square Root**: Only accepts non-negative numbers (x ≥ 0)
- **Logarithm**: Only accepts positive numbers (x > 0)
- **Power**: Accepts any real numbers for base and exponent

**Error Handling:**
- Invalid domain inputs display educational error messages
- Application continues running after errors for learning reinforcement
- All scientific functions maintain floating-point precision

## 🧪 Testing

The calculator includes comprehensive unit tests to ensure mathematical accuracy and error handling reliability:

### Running Tests

Execute the test suite using Python's built-in unittest framework:

```bash
python -m unittest test_calculator.py
```

Or run with verbose output:

```bash
python -m unittest test_calculator.py -v
```

### Test Coverage

The test suite covers:
- **All 9 mathematical functions**: Addition, subtraction, multiplication, division, power, square root, sine, cosine, logarithm
- **Domain constraint validation**: Negative square root inputs, zero/negative logarithm inputs
- **Error handling scenarios**: Division by zero, invalid input types
- **Mathematical accuracy**: Verification against known mathematical values
- **Edge cases**: Boundary conditions and floating-point precision limits

### Test Organization

```
TestArithmeticOperations: Tests for basic arithmetic functions (1-4)
TestScientificOperations: Tests for scientific functions (5-9) 
TestErrorHandling: Input validation and domain constraint testing
```

## 📚 Educational Purpose

This calculator is designed as an educational tool that demonstrates:

- **Programming Concepts**: Function design, error handling, user input validation
- **Mathematical Computing**: Integration with Python's math module for scientific operations
- **Software Architecture**: Clean code organization with pure functions and separation of concerns
- **Testing Practices**: Comprehensive unit testing with domain-specific validation
- **STEM Learning**: Practical application of mathematical concepts in programming

The application maintains zero external dependencies while providing access to advanced mathematical functions, making it ideal for programming education and computational learning scenarios.

## 🎓 Learning Outcomes

Students working with this calculator will gain experience with:

- Python standard library integration (math module)
- Mathematical domain validation and constraint handling
- Scientific computing concepts (trigonometry, logarithms, exponentiation)
- Error handling patterns for mathematical operations
- Unit testing strategies for mathematical software
- Command-line interface design and user experience considerations