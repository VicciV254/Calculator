"""
Calculator Engine
Handles all mathematical operations for the Casio FX-991EX calculator
"""
import math
import re
from typing import Union, List
import cmath


class CalculatorEngine:
    """Core calculator engine implementing FX-991EX functionality"""
    
    def __init__(self):
        self.angle_mode = 'DEG'  # Default angle mode
        self.last_answer = 0
        self.memory = 0
        
    def _convert_angle(self, angle: float, from_mode: str, to_mode: str) -> float:
        """Convert angle between different modes"""
        if from_mode == to_mode:
            return angle
        
        # First convert to radians
        if from_mode == 'DEG':
            radians = math.radians(angle)
        elif from_mode == 'GRAD':
            radians = angle * math.pi / 200
        else:  # RAD
            radians = angle
        
        # Then convert from radians to target mode
        if to_mode == 'DEG':
            return math.degrees(radians)
        elif to_mode == 'GRAD':
            return radians * 200 / math.pi
        else:  # RAD
            return radians
    
    def _create_safe_namespace(self, angle_mode: str = 'DEG') -> dict:
        """Create a safe namespace for eval with calculator functions"""
        namespace = {
            'abs': abs,
            'round': round,
            'int': int,
            'float': float,
            'e': math.e,
            'pi': math.pi,
            '__builtins__': {},
        }
        
        # Trigonometric functions
        def sin(x):
            x_rad = self._convert_angle(x, angle_mode, 'RAD')
            return math.sin(x_rad)
        
        def cos(x):
            x_rad = self._convert_angle(x, angle_mode, 'RAD')
            return math.cos(x_rad)
        
        def tan(x):
            x_rad = self._convert_angle(x, angle_mode, 'RAD')
            return math.tan(x_rad)
        
        def asin(x):
            result_rad = math.asin(x)
            return self._convert_angle(result_rad, 'RAD', angle_mode)
        
        def acos(x):
            result_rad = math.acos(x)
            return self._convert_angle(result_rad, 'RAD', angle_mode)
        
        def atan(x):
            result_rad = math.atan(x)
            return self._convert_angle(result_rad, 'RAD', angle_mode)
        
        def sinh(x):
            return math.sinh(x)
        
        def cosh(x):
            return math.cosh(x)
        
        def tanh(x):
            return math.tanh(x)
        
        # Logarithmic functions
        def log(x):
            return math.log10(x)
        
        def ln(x):
            return math.log(x)
        
        def log_base(base, x):
            return math.log(x, base)
        
        # Exponential functions
        def exp(x):
            return math.exp(x)
        
        # Factorial and combinatorics
        def factorial(n):
            if n < 0:
                raise ValueError("Factorial not defined for negative numbers")
            return math.factorial(int(n))
        
        def permutation(n, r):
            n, r = int(n), int(r)
            if n < 0 or r < 0 or r > n:
                raise ValueError("Invalid permutation parameters")
            return math.factorial(n) // math.factorial(n - r)
        
        def combination(n, r):
            n, r = int(n), int(r)
            if n < 0 or r < 0 or r > n:
                raise ValueError("Invalid combination parameters")
            return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        
        # Statistical functions
        def mean(data):
            return sum(data) / len(data)
        
        def stdev(data):
            if len(data) < 2:
                raise ValueError("Need at least 2 values for standard deviation")
            m = mean(data)
            variance = sum((x - m) ** 2 for x in data) / (len(data) - 1)
            return math.sqrt(variance)
        
        # Other functions
        def sqrt(x):
            return math.sqrt(x)
        
        def cbrt(x):
            if x >= 0:
                return x ** (1/3)
            else:
                return -((-x) ** (1/3))
        
        def reciprocal(x):
            if x == 0:
                raise ValueError("Division by zero")
            return 1 / x
        
        def mod(a, b):
            return a % b
        
        def gcd(a, b):
            a, b = int(a), int(b)
            while b:
                a, b = b, a % b
            return a
        
        def lcm(a, b):
            a, b = int(a), int(b)
            return abs(a * b) // gcd(a, b)
        
        # Add functions to namespace
        namespace.update({
            'sin': sin,
            'cos': cos,
            'tan': tan,
            'asin': asin,
            'arcsin': asin,
            'acos': acos,
            'arccos': acos,
            'atan': atan,
            'arctan': atan,
            'sinh': sinh,
            'cosh': cosh,
            'tanh': tanh,
            'log': log,
            'ln': ln,
            'exp': exp,
            'sqrt': sqrt,
            'cbrt': cbrt,
            '!': factorial,
            'P': permutation,
            'C': combination,
            'mod': mod,
            'gcd': gcd,
            'lcm': lcm,
            'mean': mean,
            'stdev': stdev,
        })
        
        return namespace
    
    def _preprocess_expression(self, expr: str) -> str:
        """Preprocess expression to make it compatible with Python eval"""
        # Replace implicit multiplication
        expr = re.sub(r'(\d)\s*\(', r'\1*(', expr)  # 2(3) -> 2*(3)
        expr = re.sub(r'\)\s*\(', r')*(', expr)      # )(  -> )*(
        expr = re.sub(r'(\d)\s*([a-zA-Z])', r'\1*\2', expr)  # 2x -> 2*x
        
        # Replace ^ with **
        expr = expr.replace('^', '**')
        
        # Replace Ans with last answer
        expr = expr.replace('Ans', str(self.last_answer))
        
        # Replace M with memory value
        expr = expr.replace('M', str(self.memory))
        
        return expr
    
    def validate_expression(self, expr: str) -> bool:
        """Check if expression is valid"""
        try:
            # Basic validation
            if not expr or not isinstance(expr, str):
                return False
            
            # Check for balanced parentheses
            if expr.count('(') != expr.count(')'):
                return False
            
            # Try to compile
            expr = self._preprocess_expression(expr)
            compile(expr, '<string>', 'eval')
            return True
        except:
            return False
    
    def evaluate(self, expr: str, angle_mode: str = 'DEG') -> Union[float, str]:
        """
        Evaluate a mathematical expression
        
        Args:
            expr: Mathematical expression to evaluate
            angle_mode: 'DEG', 'RAD', or 'GRAD'
        
        Returns:
            Calculated result
        """
        try:
            if not isinstance(expr, str) or not expr.strip():
                raise ValueError("Invalid expression")
            
            # Validate angle mode
            if angle_mode not in ['DEG', 'RAD', 'GRAD']:
                angle_mode = 'DEG'
            
            self.angle_mode = angle_mode
            
            # Preprocess expression
            processed_expr = self._preprocess_expression(expr)
            
            # Create safe namespace
            namespace = self._create_safe_namespace(angle_mode)
            
            # Evaluate expression
            result = eval(processed_expr, namespace)
            
            # Store result
            self.last_answer = result
            
            # Format result
            if isinstance(result, complex):
                # For complex numbers, format nicely
                return f"{result.real:.10g}+{result.imag:.10g}i" if result.imag >= 0 else f"{result.real:.10g}{result.imag:.10g}i"
            elif isinstance(result, float):
                # Avoid scientific notation for reasonable numbers
                if abs(result) < 1e10 and abs(result) > 1e-10 or result == 0:
                    # Round to avoid floating point errors
                    return round(result, 10)
                else:
                    return result
            else:
                return result
                
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")
        except ValueError as e:
            raise ValueError(f"Math error: {str(e)}")
        except NameError as e:
            raise ValueError(f"Unknown function or variable: {str(e)}")
        except SyntaxError:
            raise ValueError("Invalid expression syntax")
        except Exception as e:
            raise ValueError(f"Calculation error: {str(e)}")
    
    def get_available_functions(self) -> List[dict]:
        """Get list of all available functions"""
        return [
            {'name': 'sin', 'description': 'Sine function'},
            {'name': 'cos', 'description': 'Cosine function'},
            {'name': 'tan', 'description': 'Tangent function'},
            {'name': 'asin', 'description': 'Arcsine function'},
            {'name': 'acos', 'description': 'Arccosine function'},
            {'name': 'atan', 'description': 'Arctangent function'},
            {'name': 'sinh', 'description': 'Hyperbolic sine'},
            {'name': 'cosh', 'description': 'Hyperbolic cosine'},
            {'name': 'tanh', 'description': 'Hyperbolic tangent'},
            {'name': 'log', 'description': 'Logarithm base 10'},
            {'name': 'ln', 'description': 'Natural logarithm'},
            {'name': 'exp', 'description': 'Exponential (e^x)'},
            {'name': 'sqrt', 'description': 'Square root'},
            {'name': 'cbrt', 'description': 'Cube root'},
            {'name': 'factorial', 'description': 'Factorial'},
            {'name': 'P', 'description': 'Permutation - P(n,r)'},
            {'name': 'C', 'description': 'Combination - C(n,r)'},
            {'name': 'mod', 'description': 'Modulo - mod(a,b)'},
            {'name': 'gcd', 'description': 'Greatest common divisor'},
            {'name': 'lcm', 'description': 'Least common multiple'},
            {'name': 'mean', 'description': 'Mean of values'},
            {'name': 'stdev', 'description': 'Standard deviation'},
            {'name': 'pi', 'description': 'Pi constant'},
            {'name': 'e', 'description': 'Euler\'s number'},
        ]
    
    def set_memory(self, value: float):
        """Set memory value"""
        self.memory = value
    
    def add_to_memory(self, value: float):
        """Add to memory"""
        self.memory += value
    
    def get_memory(self) -> float:
        """Get memory value"""
        return self.memory
    
    def clear_memory(self):
        """Clear memory"""
        self.memory = 0
