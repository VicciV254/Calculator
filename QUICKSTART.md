# Quick Start Guide - Casio FX-991EX Calculator

Welcome to the Casio FX-991EX Calculator web application! This guide will help you get started quickly.

## 🚀 Quick Start (5 minutes)

### Option 1: Using the startup script (Recommended)

**On Linux/macOS:**
```bash
chmod +x run.sh
./run.sh
```

**On Windows:**
```bash
run.bat
```

### Option 2: Manual startup

1. **Install Python 3.8 or higher** (if not already installed)
   - Download from https://www.python.org/

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   - Go to `http://localhost:5000`

## 📱 Using the Calculator

### Mouse/Touch Usage
1. **Click buttons** in the order you want to use them
2. **Select angle mode** (DEG, RAD, GRAD) at the top
3. **Press the equals button (=)** to calculate

### Keyboard Usage
- **Numbers**: Press `0-9`
- **Operators**: Press `+`, `-`, `*`, `/`
- **Equals**: Press `Enter` or `=`
- **Delete last digit**: Press `Backspace`
- **Clear all**: Press `Escape`
- **Power**: Press `^` (e.g., `2^3`)

## 📚 Common Examples

### Basic Math
```
Calculate:    Button Sequence:     Result:
2 + 3 =       2 + 3 =              5
10 / 2 =      10 / 2 =             5
2^10 =        2 ^ 10 =             1024
√16 =         √ 16 =               4
```

### Trigonometry (Make sure DEG mode is selected)
```
Calculate:    Button Sequence:     Result:
sin(90°) =    sin 90 =             1
cos(0°) =     cos 0 =              1
tan(45°) =    tan 45 =             1
```

### Logarithms
```
Calculate:      Button Sequence:    Result:
log(100) =      log 100 =           2
ln(e) =         ln e =              1
```

### Factorials & Combinations
```
Calculate:    Button Sequence:     Result:
5! =          5 n! =               120
P(5,2) =      P 5 , 2 =            20
C(5,2) =      C 5 , 2 =            10
```

## 💾 Memory Functions

The calculator has built-in memory (M) functions:

- **M+**: Add current result to memory
- **M−**: Subtract current result from memory
- **M=**: Store current result in memory
- **MC**: Clear memory
- **MR**: Recall memory value

### Example: Store a value
1. Calculate something: `100 / 4 =` (Result: 25)
2. Click `M=` to store 25 in memory
3. The memory indicator shows `M: 25`
4. Click `MR` to insert 25 into next calculation

## 🎨 Angle Modes

Select one of three angle modes at the top:

- **DEG**: Degrees (0-360°) - Default for most users
- **RAD**: Radians (0-2π) - Used in advanced math
- **GRAD**: Gradians (0-400) - Used in surveying

**Tip**: For trigonometry homework, usually use DEG mode.

## ⌨️ Full Keyboard Shortcut List

| Key | Function |
|-----|----------|
| `0-9` | Enter digit |
| `.` | Decimal point |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `^` | Power/Exponent |
| `Enter` or `=` | Calculate |
| `Backspace` | Delete last digit |
| `Escape` | Clear everything |

## 🔧 Troubleshooting

### "Cannot find Python"
- Python is not installed or not in PATH
- Download from https://www.python.org/
- During installation, check "Add Python to PATH"

### "Port 5000 already in use"
- Another program is using port 5000
- Edit `app.py` and change the port number:
  ```python
  app.run(debug=True, host='0.0.0.0', port=5001)  # Change 5000 to 5001
  ```

### "Expression Error"
- Check for balanced parentheses: `(`, `)`
- Make sure function names are spelled correctly
- Verify angle mode matches your calculation

### Calculator won't load in browser
- Wait a few seconds and refresh (F5)
- Make sure Flask server shows "Running on http://localhost:5000"
- Try opening http://127.0.0.1:5000 instead

## 📖 Available Functions Reference

### Trigonometric Functions
- `sin(x)` - Sine
- `cos(x)` - Cosine  
- `tan(x)` - Tangent
- `asin(x)` or `arcsin(x)` - Arc sine
- `acos(x)` or `arccos(x)` - Arc cosine
- `atan(x)` or `arctan(x)` - Arc tangent
- `sinh(x)` - Hyperbolic sine
- `cosh(x)` - Hyperbolic cosine
- `tanh(x)` - Hyperbolic tangent

### Logarithmic & Exponential
- `log(x)` - Logarithm base 10
- `ln(x)` - Natural logarithm
- `exp(x)` - e^x (exponential)

### Roots & Powers
- `sqrt(x)` - Square root
- `cbrt(x)` - Cube root
- `x^y` - Power (x to the power of y)

### Factorials & Combinatorics
- `n!` - Factorial (e.g., 5!)
- `P(n,r)` - Permutations
- `C(n,r)` - Combinations

### Number Operations
- `mod(a,b)` - Modulo (remainder)
- `gcd(a,b)` - Greatest common divisor
- `lcm(a,b)` - Least common multiple

### Statistical Functions
- `mean(data)` - Average
- `stdev(data)` - Standard deviation

### Constants
- `pi` - Pi (π ≈ 3.14159...)
- `e` - Euler's number (≈ 2.71828...)

## 💡 Pro Tips

1. **Use Parentheses**: `(2+3)*4` is different from `2+3*4`
   - The first gives 20, the second gives 14

2. **The "Ans" feature**: Previous result is automatically saved
   - Use `Ans` in next calculation to reference it

3. **Chain calculations**: Each result can be used in the next one
   - Calculate something, then use M= to save it

4. **Check angle mode**: Most common mistake with trig functions
   - sin(90) in DEG mode = 1
   - sin(90) in RAD mode ≠ 1

5. **Use keyboard for speed**: Much faster than clicking buttons
   - Type: `sin(30)+cos(60)`

## 📞 Need Help?

- Check the full README.md for technical details
- Verify your expression syntax
- Make sure parentheses are balanced
- Try simpler expressions first

---

**Enjoy calculating!** 🧮 Happy number crunching!
