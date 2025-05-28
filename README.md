# 🧮 Educational Scientific Calculator

This is an educational calculator program written in Python that performs comprehensive mathematical operations including basic arithmetic and advanced scientific functions. The calculator demonstrates programming concepts while providing practical mathematical computing capabilities using Python's built-in math module.

## 🚀 Features

### Basic Arithmetic Operations (Operations 1-4)
- Add two numbers
- Subtract two numbers  
- Multiply two numbers
- Divide two numbers (with division by zero handling)

### Advanced Scientific Operations (Operations 5-9)
- **Power calculations**: Compute x raised to the power of y (x**y)
- **Square root**: Calculate square root of a number (with negative input validation)
- **Sine function**: Calculate sine of an angle in radians
- **Cosine function**: Calculate cosine of an angle in radians  
- **Natural logarithm**: Calculate natural logarithm of a number (with domain validation)

## 📦 Requirements

- Python 3.x
- Python `math` module (included in Python standard library)

## 🛠️ How to Run

1. Clone the repository or download the `calculator.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the calculator using:

```bash
python calculator.py
```

## 💡 Usage Instructions

The calculator presents an interactive menu with 9 mathematical operations:

```
Select operation:
1. Add
2. Subtract  
3. Multiply
4. Divide
5. Power (x**y)
6. Square Root
7. Sine (radians)
8. Cosine (radians)
9. Natural Logarithm
```

### Operation Types

**Two-operand operations** (1-5): You'll be prompted to enter two numbers
- Examples: Addition, Subtraction, Multiplication, Division, Power

**Single-operand operations** (6-9): You'll be prompted to enter one number
- Examples: Square Root, Sine, Cosine, Natural Logarithm

### Important Notes

⚠️ **Trigonometric Functions**: Sine and cosine functions expect input in **radians**, not degrees
- To convert degrees to radians: radians = degrees × π/180
- Common radian values: π/2 ≈ 1.5708, π ≈ 3.1416, 2π ≈ 6.2832

⚠️ **Domain Constraints**: 
- Square root operations require non-negative input (x ≥ 0)
- Natural logarithm operations require positive input (x > 0)

## 🧪 Testing

The project includes comprehensive unit tests using Python's built-in `unittest` framework:

### Running Tests

Execute the test suite using:

```bash
python -m unittest test_calculator.py
```

Or for verbose output:

```bash  
python -m unittest test_calculator.py -v
```

### Test Coverage

The test suite covers:
- **Arithmetic Functions**: All basic operations with edge cases
- **Scientific Functions**: Advanced mathematical operations with domain validation
- **Error Handling**: Input validation and mathematical constraint violations
- **Domain-Specific Tests**: Negative square root and invalid logarithm inputs

### Test Organization

- `TestArithmeticOperations`: Tests for basic arithmetic functions
- `TestScientificOperations`: Tests for advanced mathematical functions  
- `TestErrorHandling`: Tests for input validation and error conditions

## 🎯 Educational Value

This calculator demonstrates key programming concepts:

- **Function Purity**: Mathematical operations without side effects
- **Exception Handling**: Robust error management with ValueError handling
- **Standard Library Usage**: Integration with Python's math module
- **Domain-Specific Validation**: Mathematical constraint handling
- **Control Flow**: Menu navigation and program structure
- **Type Conversion**: String-to-float input processing

## 🔧 Technical Implementation

- **Architecture**: Single-file procedural programming design
- **Dependencies**: Zero external dependencies (Python standard library only)
- **Error Handling**: Comprehensive validation for mathematical domain constraints
- **Cross-Platform**: Compatible with Windows, macOS, and Linux
- **Performance**: Sub-millisecond operation execution

## 📚 Mathematical Functions Reference

| Operation | Function | Input Requirements | Example |
|-----------|----------|-------------------|---------|
| Addition | `add(x, y)` | Two numbers | `add(5, 3) = 8` |
| Subtraction | `subtract(x, y)` | Two numbers | `subtract(10, 4) = 6` |
| Multiplication | `multiply(x, y)` | Two numbers | `multiply(6, 7) = 42` |
| Division | `divide(x, y)` | Two numbers, y ≠ 0 | `divide(15, 3) = 5` |
| Power | `power(x, y)` | Two numbers | `power(2, 3) = 8` |
| Square Root | `square_root(x)` | x ≥ 0 | `square_root(9) = 3` |
| Sine | `sine(x)` | Angle in radians | `sine(π/2) ≈ 1` |
| Cosine | `cosine(x)` | Angle in radians | `cosine(0) = 1` |
| Natural Log | `logarithm(x)` | x > 0 | `logarithm(e) ≈ 1` |

## 🚨 Error Handling

The calculator gracefully handles various error conditions:

- **Invalid Input**: Non-numeric input values
- **Division by Zero**: Prevents mathematical errors
- **Negative Square Roots**: Domain validation with descriptive error messages  
- **Invalid Logarithms**: Zero or negative input validation
- **Menu Selection**: Invalid operation choice handling

## 🤝 Contributing

This project serves as an educational tool. When contributing:

1. Maintain the single-file architecture
2. Preserve zero external dependency requirement
3. Include comprehensive error handling
4. Add corresponding unit tests for new functions
5. Update documentation for any new features
