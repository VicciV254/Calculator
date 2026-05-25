# Casio FX-991EX Calculator Web Application

A complete web-based implementation of the Casio FX-991EX scientific calculator built with Python (Flask) and JavaScript. This calculator provides all the essential features of the famous FX-991EX calculator including trigonometric functions, logarithms, statistical calculations, and much more.

## Features

### Mathematical Functions
- **Trigonometric**: sin, cos, tan, arcsin, arccos, arctan
- **Hyperbolic**: sinh, cosh, tanh
- **Logarithmic**: log (base 10), ln (natural log), log(base, x)
- **Exponential**: e^x
- **Root Functions**: √ (square root), ³√ (cube root)
- **Factorial**: n!
- **Combinatorics**: Permutation P(n,r), Combination C(n,r)
- **Number Theory**: GCD, LCM, modulo
- **Statistical**: Mean, standard deviation

### Calculator Features
- **Multiple Angle Modes**: DEG (Degrees), RAD (Radians), GRAD (Gradians)
- **Memory Operations**: M+, M−, M=, MC (clear), MR (recall)
- **Answer History**: Ans variable for previous result
- **Expression Display**: Shows current expression being entered
- **Large Result Display**: Shows calculated results clearly
- **Keyboard Support**: Full keyboard support for faster input
- **Responsive Design**: Works on desktop, tablet, and mobile devices

### UI/UX
- **Professional Design**: Modern interface mimicking the FX-991EX
- **Real-time Calculation**: Quick feedback on inputs
- **Error Handling**: Clear error messages for invalid expressions
- **Memory Indicator**: Visual display of memory value
- **Functions Reference**: Built-in list of available functions

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or navigate to the project directory:**
   ```bash
   cd /workspaces/Calculator
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask development server:**
   ```bash
   python app.py
   ```

2. **Open your web browser:**
   - Navigate to `http://localhost:5000`
   - The calculator will load immediately

3. **Use the calculator:**
   - Click buttons or use your keyboard
   - Select angle mode (DEG, RAD, GRAD) using the mode buttons
   - Use memory functions for temporary value storage

## Usage Examples

### Basic Arithmetic
```
2 + 3 × 4 = 14
10 ÷ 2 - 1 = 4
```

### Trigonometric Functions (DEG mode)
```
sin(30) = 0.5
cos(60) = 0.5
tan(45) = 1
```

### Logarithmic Functions
```
log(100) = 2
ln(e) = 1
```

### Statistical Functions
```
mean([1, 2, 3, 4, 5]) = 3
stdev([1, 2, 3, 4, 5]) ≈ 1.58
```

### Combinatorics
```
5! = 120
P(5, 2) = 20
C(5, 2) = 10
```

### Powers and Roots
```
2^10 = 1024
√16 = 4
³√27 = 3
```

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0-9` | Enter digits |
| `+`, `-`, `*`, `/` | Operators |
| `.` | Decimal point |
| `^` | Power |
| `Enter` or `=` | Calculate |
| `Backspace` | Delete last character |
| `Escape` | Clear all |

## API Endpoints

### POST /calculate
Calculates a mathematical expression.

**Request:**
```json
{
  "expression": "sin(90) + cos(0)",
  "angle_mode": "DEG"
}
```

**Response:**
```json
{
  "result": 2,
  "success": true
}
```

### POST /validate
Validates if an expression is syntactically correct.

**Request:**
```json
{
  "expression": "2 + 3 * 4"
}
```

**Response:**
```json
{
  "valid": true,
  "success": true
}
```

### GET /functions
Retrieves list of available functions.

**Response:**
```json
{
  "functions": [
    {
      "name": "sin",
      "description": "Sine function"
    },
    ...
  ],
  "success": true
}
```

## Project Structure

```
Calculator/
├── app.py                 # Flask application and API routes
├── calculator_engine.py   # Core calculator logic
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main calculator HTML
└── static/
    ├── css/
    │   └── style.css     # Calculator styling
    └── js/
        └── calculator.js  # Frontend logic
```

## Technical Details

### Backend (Python/Flask)
- **Framework**: Flask for web server and API
- **Calculator Engine**: Custom implementation supporting safe expression evaluation
- **Angle Conversion**: Built-in conversion between DEG, RAD, GRAD
- **Error Handling**: Comprehensive error messages for invalid operations

### Frontend (HTML/CSS/JavaScript)
- **Responsive Design**: CSS Grid for button layout, flexbox for responsive design
- **Keyboard Support**: Full keyboard event handling
- **Real-time Display**: Live expression and result display
- **Memory Management**: Client-side memory operations

### Security
- **Safe Evaluation**: Uses restricted namespace for eval() to prevent code injection
- **Input Validation**: Expression validation before evaluation
- **Error Handling**: Graceful handling of all error conditions

## Limitations

- Complex number support is limited (for display purposes)
- Matrix operations are not implemented
- Numerical differential/integral approximations are not included
- Some advanced FX-991EX features (like STAT mode) are simplified

## Future Enhancements

- [ ] Matrix calculations
- [ ] Statistical analysis mode
- [ ] Equation solving
- [ ] Numerical integration and differentiation
- [ ] Complex number full support
- [ ] Save/load calculation history
- [ ] Dark mode theme
- [ ] Multi-language support

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, you can change it in app.py:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Module Import Error
Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Expression Not Calculating
- Check that parentheses are balanced
- Verify function names are spelled correctly
- Ensure angle mode is appropriate for your calculation

## License

This project is created for educational purposes.

## Support

For issues or questions, please check the code comments or verify your expression syntax with the validation endpoint.

---

**Enjoy using your web-based Casio FX-991EX Calculator!** 🧮