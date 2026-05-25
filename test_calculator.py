#!/usr/bin/env python3
"""
Simple test script to verify calculator engine functionality
"""

import sys
sys.path.insert(0, '/workspaces/Calculator')

from calculator_engine import CalculatorEngine

def test_calculator():
    """Test basic calculator functionality"""
    calc = CalculatorEngine()
    
    test_cases = [
        ("2+3", None, 5, "Basic addition"),
        ("10/2", None, 5, "Basic division"),
        ("2^3", None, 8, "Power operation"),
        ("sqrt(16)", None, 4, "Square root"),
        ("sin(90)", "DEG", 1, "Sine in degrees"),
        ("cos(0)", "DEG", 1, "Cosine"),
        ("log(100)", None, 2, "Log base 10"),
        ("5!", None, 120, "Factorial"),
        ("C(5,2)", None, 10, "Combination"),
        ("P(5,2)", None, 20, "Permutation"),
    ]
    
    print("Testing Calculator Engine")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for expression, angle_mode, expected, description in test_cases:
        try:
            if angle_mode:
                result = calc.evaluate(expression, angle_mode)
            else:
                result = calc.evaluate(expression)
            
            # Round for comparison due to floating point precision
            if isinstance(result, float):
                result = round(result, 5)
            if isinstance(expected, float):
                expected = round(expected, 5)
            
            if result == expected:
                print(f"✓ {description:30} | {expression:20} = {result}")
                passed += 1
            else:
                print(f"✗ {description:30} | {expression:20} = {result} (expected {expected})")
                failed += 1
        except Exception as e:
            print(f"✗ {description:30} | {expression:20} | Error: {e}")
            failed += 1
    
    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    
    return failed == 0

if __name__ == "__main__":
    success = test_calculator()
    sys.exit(0 if success else 1)
