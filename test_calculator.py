"""
Comprehensive Unit Test Suite for Educational Scientific Calculator

This test suite validates all 9 mathematical operations of the Educational Scientific Calculator,
ensuring mathematical accuracy, proper error handling, and domain constraint validation.
The tests demonstrate educational testing concepts using Python's built-in unittest framework
while maintaining zero external dependencies.

Test Coverage:
- Basic Arithmetic Operations (4 functions): add, subtract, multiply, divide
- Scientific Operations (5 functions): power, square_root, sine, cosine, logarithm
- Domain-specific error condition validation
- Floating-point precision testing for mathematical accuracy

Usage:
    python -m unittest test_calculator.py
    python -m unittest discover
"""

import unittest
import math
from calculator import (
    add, subtract, multiply, divide,
    power, square_root, sine, cosine, logarithm
)


class TestArithmeticOperations(unittest.TestCase):
    """
    Test class for basic arithmetic operations covering addition, subtraction,
    multiplication, and division operations with comprehensive edge case validation.
    """

    def test_add_positive_numbers(self):
        """Test addition with positive integers and floating-point numbers"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=10)
        self.assertEqual(add(100, 200), 300)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers and mixed positive/negative inputs"""
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-1.5, 2.5), 1.0)
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(-10, 15), 5)

    def test_add_zero(self):
        """Test addition with zero as additive identity"""
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, -3), -3)
        self.assertEqual(add(0.0, 7.5), 7.5)

    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10.5, 3.2), 7.3)
        self.assertAlmostEqual(subtract(1.0, 0.1), 0.9, places=10)
        self.assertEqual(subtract(100, 25), 75)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers and mixed inputs"""
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-2, 3), -5)
        self.assertEqual(subtract(3, -2), 5)
        self.assertEqual(subtract(-10, -15), 5)

    def test_subtract_equal_numbers(self):
        """Test subtraction resulting in zero"""
        self.assertEqual(subtract(5, 5), 0)
        self.assertEqual(subtract(-3, -3), 0)
        self.assertEqual(subtract(0, 0), 0)
        self.assertAlmostEqual(subtract(2.5, 2.5), 0.0, places=10)

    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers"""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(multiply(0.3, 0.7), 0.21, places=10)
        self.assertEqual(multiply(1.5, 2.5), 3.75)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers"""
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(3, -4), -12)
        self.assertEqual(multiply(-3, -4), 12)
        self.assertEqual(multiply(-2.5, 2), -5.0)

    def test_multiply_zero(self):
        """Test multiplication with zero as multiplicative identity"""
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(7, 0), 0)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(-3, 0), 0)

    def test_divide_positive_numbers(self):
        """Test division with positive numbers"""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(15, 3), 5.0)
        self.assertAlmostEqual(divide(7, 3), 2.333333333333333, places=10)
        self.assertEqual(divide(1, 4), 0.25)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers"""
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(10, -2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)
        self.assertEqual(divide(-15, 3), -5.0)

    def test_divide_by_zero(self):
        """Test division by zero error handling"""
        # Note: divide() returns a string message instead of raising an exception
        self.assertEqual(divide(10, 0), "Error! Division by zero.")
        self.assertEqual(divide(-5, 0), "Error! Division by zero.")
        self.assertEqual(divide(0, 0), "Error! Division by zero.")
        self.assertEqual(divide(3.14, 0), "Error! Division by zero.")


class TestScientificOperations(unittest.TestCase):
    """
    Test class for scientific mathematical operations covering power, square root,
    sine, cosine, and logarithm functions with domain constraint validation.
    """

    def test_power_positive_integers(self):
        """Test power operation with positive integer exponents"""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(10, 0), 1)
        self.assertEqual(power(3, 1), 3)
        self.assertEqual(power(1, 100), 1)

    def test_power_negative_exponent(self):
        """Test power operation with negative exponents"""
        self.assertEqual(power(2, -1), 0.5)
        self.assertEqual(power(4, -2), 0.0625)
        self.assertAlmostEqual(power(10, -3), 0.001, places=10)
        self.assertEqual(power(5, -1), 0.2)

    def test_power_fractional_exponent(self):
        """Test power operation with fractional exponents"""
        self.assertAlmostEqual(power(4, 0.5), 2.0, places=10)
        self.assertAlmostEqual(power(8, 1/3), 2.0, places=10)
        self.assertAlmostEqual(power(9, 0.5), 3.0, places=10)
        self.assertAlmostEqual(power(27, 1/3), 3.0, places=10)

    def test_power_zero_base(self):
        """Test power operation with zero base"""
        self.assertEqual(power(0, 1), 0)
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(0, 100), 0)
        # Note: 0^0 is implementation-defined, typically returns 1 in Python
        self.assertEqual(power(0, 0), 1)

    def test_square_root_positive_input(self):
        """Test square root with valid positive inputs"""
        self.assertAlmostEqual(square_root(4), 2.0, places=10)
        self.assertAlmostEqual(square_root(9), 3.0, places=10)
        self.assertAlmostEqual(square_root(16), 4.0, places=10)
        self.assertAlmostEqual(square_root(25), 5.0, places=10)
        self.assertAlmostEqual(square_root(2), 1.4142135623730951, places=10)

    def test_square_root_zero(self):
        """Test square root of zero"""
        self.assertEqual(square_root(0), 0.0)
        self.assertAlmostEqual(square_root(0.0), 0.0, places=10)

    def test_square_root_negative_raises_value_error(self):
        """Test square root domain constraint: negative input raises ValueError"""
        with self.assertRaises(ValueError) as context:
            square_root(-1)
        self.assertEqual(str(context.exception), "Square root requires non-negative input")
        
        with self.assertRaises(ValueError) as context:
            square_root(-4)
        self.assertEqual(str(context.exception), "Square root requires non-negative input")
        
        with self.assertRaises(ValueError) as context:
            square_root(-0.1)
        self.assertEqual(str(context.exception), "Square root requires non-negative input")

    def test_sine_known_values(self):
        """Test sine function with known mathematical values"""
        # sin(0) = 0
        self.assertAlmostEqual(sine(0), 0.0, places=10)
        
        # sin(π/2) = 1
        self.assertAlmostEqual(sine(math.pi / 2), 1.0, places=10)
        
        # sin(π) = 0
        self.assertAlmostEqual(sine(math.pi), 0.0, places=5)  # Reduced precision due to floating-point
        
        # sin(3π/2) = -1
        self.assertAlmostEqual(sine(3 * math.pi / 2), -1.0, places=10)
        
        # sin(2π) = 0
        self.assertAlmostEqual(sine(2 * math.pi), 0.0, places=5)

    def test_sine_negative_input(self):
        """Test sine function with negative radian inputs"""
        # sin(-π/2) = -1
        self.assertAlmostEqual(sine(-math.pi / 2), -1.0, places=10)
        
        # sin(-π) = 0
        self.assertAlmostEqual(sine(-math.pi), 0.0, places=5)
        
        # Test arbitrary negative values
        self.assertAlmostEqual(sine(-1), -math.sin(1), places=10)

    def test_cosine_known_values(self):
        """Test cosine function with known mathematical values"""
        # cos(0) = 1
        self.assertAlmostEqual(cosine(0), 1.0, places=10)
        
        # cos(π/2) = 0
        self.assertAlmostEqual(cosine(math.pi / 2), 0.0, places=5)
        
        # cos(π) = -1
        self.assertAlmostEqual(cosine(math.pi), -1.0, places=10)
        
        # cos(3π/2) = 0
        self.assertAlmostEqual(cosine(3 * math.pi / 2), 0.0, places=5)
        
        # cos(2π) = 1
        self.assertAlmostEqual(cosine(2 * math.pi), 1.0, places=10)

    def test_cosine_negative_input(self):
        """Test cosine function with negative radian inputs"""
        # cos(-π/2) = 0
        self.assertAlmostEqual(cosine(-math.pi / 2), 0.0, places=5)
        
        # cos(-π) = -1
        self.assertAlmostEqual(cosine(-math.pi), -1.0, places=10)
        
        # Test arbitrary negative values - cosine is even function: cos(-x) = cos(x)
        self.assertAlmostEqual(cosine(-1), math.cos(1), places=10)

    def test_logarithm_positive_input(self):
        """Test natural logarithm with valid positive inputs"""
        # ln(1) = 0
        self.assertAlmostEqual(logarithm(1), 0.0, places=10)
        
        # ln(e) = 1
        self.assertAlmostEqual(logarithm(math.e), 1.0, places=10)
        
        # ln(e²) = 2
        self.assertAlmostEqual(logarithm(math.e ** 2), 2.0, places=10)
        
        # Test other positive values
        self.assertAlmostEqual(logarithm(10), math.log(10), places=10)
        self.assertAlmostEqual(logarithm(2.718281828459045), 1.0, places=10)

    def test_logarithm_zero_raises_value_error(self):
        """Test logarithm domain constraint: zero input raises ValueError"""
        with self.assertRaises(ValueError) as context:
            logarithm(0)
        self.assertEqual(str(context.exception), "Logarithm requires positive input")
        
        with self.assertRaises(ValueError) as context:
            logarithm(0.0)
        self.assertEqual(str(context.exception), "Logarithm requires positive input")

    def test_logarithm_negative_raises_value_error(self):
        """Test logarithm domain constraint: negative input raises ValueError"""
        with self.assertRaises(ValueError) as context:
            logarithm(-1)
        self.assertEqual(str(context.exception), "Logarithm requires positive input")
        
        with self.assertRaises(ValueError) as context:
            logarithm(-10)
        self.assertEqual(str(context.exception), "Logarithm requires positive input")
        
        with self.assertRaises(ValueError) as context:
            logarithm(-0.1)
        self.assertEqual(str(context.exception), "Logarithm requires positive input")


class TestMathematicalAccuracy(unittest.TestCase):
    """
    Test class for mathematical accuracy and floating-point precision validation
    across all scientific operations to ensure educational reliability.
    """

    def test_trigonometric_identity_validation(self):
        """Test fundamental trigonometric identities for mathematical correctness"""
        # Test sin²(x) + cos²(x) = 1 for various angles
        test_angles = [0, math.pi/6, math.pi/4, math.pi/3, math.pi/2, math.pi]
        
        for angle in test_angles:
            sin_val = sine(angle)
            cos_val = cosine(angle)
            identity_result = sin_val**2 + cos_val**2
            self.assertAlmostEqual(identity_result, 1.0, places=10,
                                 msg=f"sin²({angle}) + cos²({angle}) should equal 1")

    def test_power_logarithm_inverse_relationship(self):
        """Test that power and logarithm operations are mathematical inverses"""
        # Test e^(ln(x)) = x for positive values
        test_values = [1, 2, 5, 10, 100]
        
        for x in test_values:
            ln_x = logarithm(x)
            e_to_ln_x = power(math.e, ln_x)
            self.assertAlmostEqual(e_to_ln_x, x, places=10,
                                 msg=f"e^(ln({x})) should equal {x}")

    def test_square_root_power_relationship(self):
        """Test that square root and power operations are mathematical inverses"""
        # Test (√x)² = x for positive values
        test_values = [1, 4, 9, 16, 25, 100]
        
        for x in test_values:
            sqrt_x = square_root(x)
            sqrt_x_squared = power(sqrt_x, 2)
            self.assertAlmostEqual(sqrt_x_squared, x, places=10,
                                 msg=f"(√{x})² should equal {x}")

    def test_floating_point_precision_boundaries(self):
        """Test mathematical operations at floating-point precision boundaries"""
        # Test very small positive numbers
        very_small = 1e-10
        self.assertAlmostEqual(logarithm(very_small), math.log(very_small), places=15)
        self.assertAlmostEqual(square_root(very_small), math.sqrt(very_small), places=15)
        
        # Test very large numbers
        very_large = 1e10
        self.assertAlmostEqual(logarithm(very_large), math.log(very_large), places=10)
        self.assertAlmostEqual(square_root(very_large), math.sqrt(very_large), places=10)


if __name__ == '__main__':
    # Configure unittest to run with verbose output for educational purposes
    unittest.main(verbosity=2)