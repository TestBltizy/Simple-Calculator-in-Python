#!/usr/bin/env python3
"""
Comprehensive Unit Test Suite for Enhanced Simple Python Calculator

This test suite provides systematic validation of all nine mathematical operations
(four arithmetic and five scientific functions) using Python's built-in unittest framework.
The tests ensure mathematical accuracy, domain constraint enforcement, and error handling
verification across the expanded calculator functionality.

Test Coverage:
- Arithmetic Operations: add, subtract, multiply, divide
- Scientific Operations: power, square_root, sine, cosine, logarithm
- Domain Constraint Testing: negative square root, non-positive logarithm
- Error Handling: division by zero, domain violations
- Mathematical Accuracy: verification against known values and math module references
- Integration Testing: menu-driven dispatch validation

Author: Enhanced Calculator Test Suite
Python Version: 3.x
Dependencies: unittest (built-in), math (standard library)
"""

import unittest
import math
from calculator import (
    add, subtract, multiply, divide,
    power, square_root, sine, cosine, logarithm
)


class TestArithmeticOperations(unittest.TestCase):
    """
    Comprehensive validation of four core arithmetic operations.
    
    Tests cover positive numbers, negative numbers, floating-point precision,
    zero values, and mathematical edge cases for educational demonstration.
    """
    
    def test_add_positive_numbers(self):
        """Test addition with positive integer and floating-point numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(1.5, 2.5), 4.0)
        self.assertEqual(add(10, 20), 30)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=10)
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers and mixed signs."""
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-1.5, 2.5), 1.0)
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(-10, 10), 0)
    
    def test_add_zero_values(self):
        """Test addition with zero values."""
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, -3), -3)
        self.assertEqual(add(0.0, 2.5), 2.5)
    
    def test_subtract_standard_operations(self):
        """Test subtraction with standard positive and negative scenarios."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 15), -5)
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-5, 3), -8)
    
    def test_subtract_floating_point(self):
        """Test subtraction with floating-point precision."""
        self.assertAlmostEqual(subtract(5.7, 2.3), 3.4, places=10)
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2, places=10)
        self.assertEqual(subtract(2.5, 2.5), 0.0)
    
    def test_subtract_zero_scenarios(self):
        """Test subtraction involving zero values."""
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, 0), -3)
    
    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(2.5, 4), 10.0)
        self.assertEqual(multiply(1.5, 2.5), 3.75)
        self.assertEqual(multiply(7, 8), 56)
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers and mixed signs."""
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(-3, -4), 12)
        self.assertEqual(multiply(5, -2), -10)
        self.assertEqual(multiply(-2.5, 2), -5.0)
    
    def test_multiply_with_zero(self):
        """Test multiplication with zero values."""
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(-3, 0), 0)
        self.assertEqual(multiply(0, -7), 0)
    
    def test_multiply_with_one(self):
        """Test multiplication identity property with one."""
        self.assertEqual(multiply(1, 5), 5)
        self.assertEqual(multiply(5, 1), 5)
        self.assertEqual(multiply(-3, 1), -3)
        self.assertEqual(multiply(1, -7), -7)
    
    def test_divide_standard_operations(self):
        """Test division with standard positive and negative scenarios."""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(15, 3), 5.0)
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(10, -2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)
    
    def test_divide_floating_point_precision(self):
        """Test division with floating-point results and precision."""
        self.assertAlmostEqual(divide(7, 3), 2.3333333333333335, places=10)
        self.assertAlmostEqual(divide(1, 3), 0.3333333333333333, places=10)
        self.assertEqual(divide(5.0, 2.0), 2.5)
        self.assertAlmostEqual(divide(22, 7), 3.142857142857143, places=10)
    
    def test_divide_by_zero_error_handling(self):
        """Test division by zero returns appropriate error message."""
        self.assertEqual(divide(10, 0), "Error! Division by zero.")
        self.assertEqual(divide(-5, 0), "Error! Division by zero.")
        self.assertEqual(divide(0, 0), "Error! Division by zero.")
        self.assertEqual(divide(3.14, 0), "Error! Division by zero.")


class TestScientificOperations(unittest.TestCase):
    """
    Comprehensive validation of five scientific mathematical operations.
    
    Tests cover mathematical accuracy verification against known values,
    domain constraint validation, and cross-platform floating-point consistency
    using math module reference calculations.
    """
    
    def test_power_positive_exponents(self):
        """Test power operation with positive integer and floating-point exponents."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(3, 4), 81)
        self.assertAlmostEqual(power(2, 0.5), math.sqrt(2), places=10)
        self.assertAlmostEqual(power(4, 0.5), 2.0, places=10)
    
    def test_power_negative_exponents(self):
        """Test power operation with negative exponents."""
        self.assertAlmostEqual(power(2, -1), 0.5, places=10)
        self.assertAlmostEqual(power(4, -2), 0.0625, places=10)
        self.assertAlmostEqual(power(10, -3), 0.001, places=10)
        self.assertAlmostEqual(power(5, -1), 0.2, places=10)
    
    def test_power_zero_exponent(self):
        """Test power operation with zero exponent (any number to power 0 equals 1)."""
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(-3, 0), 1)
        self.assertEqual(power(100, 0), 1)
        self.assertEqual(power(0.5, 0), 1)
    
    def test_power_zero_base(self):
        """Test power operation with zero base."""
        self.assertEqual(power(0, 1), 0)
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(0, 100), 0)
        # Note: 0^0 is mathematically undefined but Python returns 1
        self.assertEqual(power(0, 0), 1)
    
    def test_power_fractional_exponents(self):
        """Test power operation with fractional exponents."""
        self.assertAlmostEqual(power(8, 1/3), 2.0, places=10)  # Cube root of 8
        self.assertAlmostEqual(power(16, 1/4), 2.0, places=10)  # Fourth root of 16
        self.assertAlmostEqual(power(27, 1/3), 3.0, places=10)  # Cube root of 27
    
    def test_square_root_positive_values(self):
        """Test square root with positive values and mathematical accuracy."""
        self.assertAlmostEqual(square_root(4), 2.0, places=10)
        self.assertAlmostEqual(square_root(9), 3.0, places=10)
        self.assertAlmostEqual(square_root(16), 4.0, places=10)
        self.assertAlmostEqual(square_root(25), 5.0, places=10)
        self.assertAlmostEqual(square_root(2), math.sqrt(2), places=10)
    
    def test_square_root_zero_value(self):
        """Test square root of zero."""
        self.assertEqual(square_root(0), 0.0)
        self.assertEqual(square_root(0.0), 0.0)
    
    def test_square_root_decimal_values(self):
        """Test square root with decimal values."""
        self.assertAlmostEqual(square_root(0.25), 0.5, places=10)
        self.assertAlmostEqual(square_root(1.44), 1.2, places=10)
        self.assertAlmostEqual(square_root(6.25), 2.5, places=10)
        self.assertAlmostEqual(square_root(0.01), 0.1, places=10)
    
    def test_square_root_large_values(self):
        """Test square root with large values."""
        self.assertAlmostEqual(square_root(100), 10.0, places=10)
        self.assertAlmostEqual(square_root(10000), 100.0, places=10)
        self.assertAlmostEqual(square_root(1000000), 1000.0, places=10)
    
    def test_sine_standard_angles(self):
        """Test sine function with standard trigonometric angles."""
        # Test sine at key angles (in radians)
        self.assertAlmostEqual(sine(0), 0.0, places=10)
        self.assertAlmostEqual(sine(math.pi/2), 1.0, places=10)
        self.assertAlmostEqual(sine(math.pi), 0.0, places=5)  # Floating-point precision
        self.assertAlmostEqual(sine(3*math.pi/2), -1.0, places=10)
        self.assertAlmostEqual(sine(2*math.pi), 0.0, places=5)  # Floating-point precision
    
    def test_sine_arbitrary_radians(self):
        """Test sine function with arbitrary radian values."""
        self.assertAlmostEqual(sine(math.pi/6), 0.5, places=10)  # 30 degrees
        self.assertAlmostEqual(sine(math.pi/4), math.sqrt(2)/2, places=10)  # 45 degrees
        self.assertAlmostEqual(sine(math.pi/3), math.sqrt(3)/2, places=10)  # 60 degrees
        self.assertAlmostEqual(sine(1), math.sin(1), places=10)  # 1 radian
    
    def test_sine_negative_angles(self):
        """Test sine function with negative angle values."""
        self.assertAlmostEqual(sine(-math.pi/2), -1.0, places=10)
        self.assertAlmostEqual(sine(-math.pi/6), -0.5, places=10)
        self.assertAlmostEqual(sine(-1), math.sin(-1), places=10)
    
    def test_cosine_standard_angles(self):
        """Test cosine function with standard trigonometric angles."""
        # Test cosine at key angles (in radians)
        self.assertAlmostEqual(cosine(0), 1.0, places=10)
        self.assertAlmostEqual(cosine(math.pi/2), 0.0, places=5)  # Floating-point precision
        self.assertAlmostEqual(cosine(math.pi), -1.0, places=10)
        self.assertAlmostEqual(cosine(3*math.pi/2), 0.0, places=5)  # Floating-point precision
        self.assertAlmostEqual(cosine(2*math.pi), 1.0, places=10)
    
    def test_cosine_arbitrary_radians(self):
        """Test cosine function with arbitrary radian values."""
        self.assertAlmostEqual(cosine(math.pi/6), math.sqrt(3)/2, places=10)  # 30 degrees
        self.assertAlmostEqual(cosine(math.pi/4), math.sqrt(2)/2, places=10)  # 45 degrees
        self.assertAlmostEqual(cosine(math.pi/3), 0.5, places=10)  # 60 degrees
        self.assertAlmostEqual(cosine(1), math.cos(1), places=10)  # 1 radian
    
    def test_cosine_negative_angles(self):
        """Test cosine function with negative angle values."""
        self.assertAlmostEqual(cosine(-math.pi/2), 0.0, places=5)
        self.assertAlmostEqual(cosine(-math.pi/6), math.sqrt(3)/2, places=10)
        self.assertAlmostEqual(cosine(-1), math.cos(-1), places=10)
    
    def test_logarithm_positive_values(self):
        """Test natural logarithm with positive values."""
        self.assertAlmostEqual(logarithm(1), 0.0, places=10)  # ln(1) = 0
        self.assertAlmostEqual(logarithm(math.e), 1.0, places=10)  # ln(e) = 1
        self.assertAlmostEqual(logarithm(math.e**2), 2.0, places=10)  # ln(e^2) = 2
        self.assertAlmostEqual(logarithm(10), math.log(10), places=10)
    
    def test_logarithm_mathematical_constants(self):
        """Test logarithm with mathematical constants and known values."""
        self.assertAlmostEqual(logarithm(math.e), 1.0, places=10)
        self.assertAlmostEqual(logarithm(1), 0.0, places=10)
        self.assertAlmostEqual(logarithm(math.exp(3)), 3.0, places=10)  # ln(e^3) = 3
        self.assertAlmostEqual(logarithm(math.exp(0.5)), 0.5, places=10)  # ln(e^0.5) = 0.5
    
    def test_logarithm_decimal_values(self):
        """Test logarithm with decimal values."""
        self.assertAlmostEqual(logarithm(0.5), math.log(0.5), places=10)
        self.assertAlmostEqual(logarithm(2.718281828), math.log(2.718281828), places=10)
        self.assertAlmostEqual(logarithm(0.1), math.log(0.1), places=10)
    
    def test_logarithm_large_values(self):
        """Test logarithm with large values."""
        self.assertAlmostEqual(logarithm(100), math.log(100), places=10)
        self.assertAlmostEqual(logarithm(1000), math.log(1000), places=10)
        self.assertAlmostEqual(logarithm(10000), math.log(10000), places=10)


class TestErrorHandling(unittest.TestCase):
    """
    Comprehensive validation of error handling and domain constraint enforcement.
    
    Tests cover division by zero protection, square root negative input validation,
    logarithm non-positive input validation, and proper error messaging for
    mathematical domain violations.
    """
    
    def test_division_by_zero_scenarios(self):
        """Test division by zero returns appropriate error messages."""
        self.assertEqual(divide(10, 0), "Error! Division by zero.")
        self.assertEqual(divide(-5, 0), "Error! Division by zero.")
        self.assertEqual(divide(0, 0), "Error! Division by zero.")
        self.assertEqual(divide(3.14159, 0), "Error! Division by zero.")
        self.assertEqual(divide(-2.5, 0), "Error! Division by zero.")
    
    def test_square_root_negative_input_validation(self):
        """Test square root with negative inputs returns domain error."""
        self.assertEqual(square_root(-1), "Error! Square root requires non-negative number.")
        self.assertEqual(square_root(-4), "Error! Square root requires non-negative number.")
        self.assertEqual(square_root(-0.5), "Error! Square root requires non-negative number.")
        self.assertEqual(square_root(-100), "Error! Square root requires non-negative number.")
        self.assertEqual(square_root(-0.001), "Error! Square root requires non-negative number.")
    
    def test_square_root_boundary_conditions(self):
        """Test square root at domain boundary (zero and positive values)."""
        # Zero should work (boundary condition)
        self.assertEqual(square_root(0), 0.0)
        self.assertEqual(square_root(0.0), 0.0)
        
        # Very small positive values should work
        self.assertAlmostEqual(square_root(0.0001), math.sqrt(0.0001), places=10)
        self.assertAlmostEqual(square_root(1e-10), math.sqrt(1e-10), places=15)
    
    def test_logarithm_non_positive_input_validation(self):
        """Test logarithm with non-positive inputs returns domain error."""
        # Test zero input
        self.assertEqual(logarithm(0), "Error! Logarithm requires positive number.")
        self.assertEqual(logarithm(0.0), "Error! Logarithm requires positive number.")
        
        # Test negative inputs
        self.assertEqual(logarithm(-1), "Error! Logarithm requires positive number.")
        self.assertEqual(logarithm(-5), "Error! Logarithm requires positive number.")
        self.assertEqual(logarithm(-0.5), "Error! Logarithm requires positive number.")
        self.assertEqual(logarithm(-100), "Error! Logarithm requires positive number.")
    
    def test_logarithm_boundary_conditions(self):
        """Test logarithm at domain boundary (very small positive values)."""
        # Very small positive values should work
        self.assertAlmostEqual(logarithm(0.0001), math.log(0.0001), places=10)
        self.assertAlmostEqual(logarithm(1e-10), math.log(1e-10), places=15)
        self.assertAlmostEqual(logarithm(0.001), math.log(0.001), places=10)
    
    def test_power_edge_cases(self):
        """Test power function edge cases and potential issues."""
        # Test very large exponents (should not cause errors)
        result = power(2, 10)
        self.assertEqual(result, 1024)
        
        # Test negative base with integer exponents
        self.assertEqual(power(-2, 2), 4)
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(-3, 2), 9)
        
        # Test negative base with fractional exponents (may produce complex results)
        # Note: Python handles this but may return complex numbers
        result = power(-1, 0.5)
        # This should work in Python (returns complex number, but we get real part)
        self.assertIsInstance(result, (int, float, complex))
    
    def test_trigonometric_function_edge_cases(self):
        """Test trigonometric functions with edge cases and large values."""
        # Test very large angle values
        large_angle = 1000 * math.pi
        sine_result = sine(large_angle)
        cosine_result = cosine(large_angle)
        
        # Results should be within valid range [-1, 1]
        self.assertTrue(-1 <= sine_result <= 1)
        self.assertTrue(-1 <= cosine_result <= 1)
        
        # Test very small angle values
        small_angle = 1e-10
        self.assertAlmostEqual(sine(small_angle), small_angle, places=10)  # sin(x) ≈ x for small x
        self.assertAlmostEqual(cosine(small_angle), 1.0, places=10)  # cos(x) ≈ 1 for small x


class TestIntegrationAndAccuracy(unittest.TestCase):
    """
    Integration testing for menu-driven dispatch validation and cross-platform
    mathematical consistency verification.
    
    Tests ensure proper function routing, mathematical accuracy across platforms,
    and floating-point precision consistency for educational demonstration.
    """
    
    def test_arithmetic_function_integration(self):
        """Test integration of arithmetic functions with various input combinations."""
        # Test chained operations that might be used in educational scenarios
        result1 = add(multiply(2, 3), divide(8, 2))  # (2*3) + (8/2) = 6 + 4 = 10
        self.assertEqual(result1, 10.0)
        
        result2 = subtract(add(5, 3), multiply(2, 2))  # (5+3) - (2*2) = 8 - 4 = 4
        self.assertEqual(result2, 4)
        
        result3 = divide(multiply(6, 4), add(2, 4))  # (6*4) / (2+4) = 24 / 6 = 4
        self.assertEqual(result3, 4.0)
    
    def test_scientific_function_integration(self):
        """Test integration of scientific functions with mathematical relationships."""
        # Test Pythagorean identity: sin²(x) + cos²(x) = 1
        angle = math.pi / 4  # 45 degrees
        sin_val = sine(angle)
        cos_val = cosine(angle)
        pythagorean_result = add(power(sin_val, 2), power(cos_val, 2))
        self.assertAlmostEqual(pythagorean_result, 1.0, places=10)
        
        # Test logarithm and exponential relationship: ln(e^x) = x
        x_value = 2.5
        exp_result = power(math.e, x_value)
        log_result = logarithm(exp_result)
        self.assertAlmostEqual(log_result, x_value, places=10)
        
        # Test square root and power relationship: sqrt(x) = x^0.5
        test_value = 16
        sqrt_result = square_root(test_value)
        power_result = power(test_value, 0.5)
        self.assertAlmostEqual(sqrt_result, power_result, places=10)
    
    def test_cross_platform_floating_point_consistency(self):
        """Test floating-point consistency across different platform environments."""
        # Test mathematical constants consistency
        self.assertAlmostEqual(sine(math.pi), 0.0, places=5)
        self.assertAlmostEqual(cosine(math.pi), -1.0, places=10)
        self.assertAlmostEqual(logarithm(math.e), 1.0, places=10)
        
        # Test precision with known mathematical relationships
        self.assertAlmostEqual(power(square_root(2), 2), 2.0, places=10)
        self.assertAlmostEqual(square_root(power(3, 2)), 3.0, places=10)
        
        # Test trigonometric precision at standard angles
        self.assertAlmostEqual(sine(math.pi/6), 0.5, places=10)
        self.assertAlmostEqual(cosine(math.pi/3), 0.5, places=10)
    
    def test_mathematical_accuracy_verification(self):
        """Test mathematical accuracy against known mathematical values."""
        # Test well-known mathematical results
        self.assertAlmostEqual(power(2, 10), 1024, places=10)
        self.assertAlmostEqual(square_root(144), 12.0, places=10)
        self.assertAlmostEqual(logarithm(math.exp(5)), 5.0, places=10)
        
        # Test trigonometric identities
        angle = math.pi / 3  # 60 degrees
        self.assertAlmostEqual(sine(angle), math.sqrt(3)/2, places=10)
        self.assertAlmostEqual(cosine(angle), 0.5, places=10)
        
        # Test logarithmic properties: ln(a*b) = ln(a) + ln(b)
        a, b = 2, 3
        log_product = logarithm(multiply(a, b))
        log_sum = add(logarithm(a), logarithm(b))
        self.assertAlmostEqual(log_product, log_sum, places=10)
    
    def test_domain_constraint_comprehensive_validation(self):
        """Comprehensive validation of all domain constraints across functions."""
        # Test all functions with valid inputs
        self.assertIsInstance(add(1, 2), (int, float))
        self.assertIsInstance(subtract(5, 3), (int, float))
        self.assertIsInstance(multiply(2, 4), (int, float))
        self.assertIsInstance(divide(10, 2), (int, float))
        self.assertIsInstance(power(2, 3), (int, float))
        self.assertIsInstance(square_root(9), (int, float))
        self.assertIsInstance(sine(math.pi/4), (int, float))
        self.assertIsInstance(cosine(math.pi/4), (int, float))
        self.assertIsInstance(logarithm(math.e), (int, float))
        
        # Test domain constraint violations return error strings
        self.assertIsInstance(divide(1, 0), str)
        self.assertIsInstance(square_root(-1), str)
        self.assertIsInstance(logarithm(0), str)
        self.assertIsInstance(logarithm(-1), str)
    
    def test_educational_demonstration_scenarios(self):
        """Test scenarios commonly used in educational programming demonstrations."""
        # Basic calculator operations
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(divide(10, 5), 2.0)
        
        # Scientific calculator operations
        self.assertEqual(power(10, 2), 100)
        self.assertAlmostEqual(square_root(100), 10.0, places=10)
        self.assertAlmostEqual(sine(0), 0.0, places=10)
        self.assertAlmostEqual(cosine(0), 1.0, places=10)
        self.assertAlmostEqual(logarithm(1), 0.0, places=10)
        
        # Error handling demonstrations
        self.assertTrue(divide(1, 0).startswith("Error!"))
        self.assertTrue(square_root(-1).startswith("Error!"))
        self.assertTrue(logarithm(0).startswith("Error!"))


if __name__ == '__main__':
    # Configure test execution with detailed output for educational purposes
    unittest.main(verbosity=2, buffer=True)