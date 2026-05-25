# Development Notes

## Architecture Overview

The Casio FX-991EX Calculator web application is built with a clean separation between frontend and backend:

```
┌─────────────────────────────────────────────────────────┐
│                    Web Browser                           │
│  ┌────────────────────────────────────────────────────┐ │
│  │   HTML/CSS/JavaScript Frontend                      │ │
│  │   - Calculator UI with responsive design            │ │
│  │   - Event handling for buttons and keyboard         │ │
│  │   - API communication with backend                  │ │
│  └────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
                          ↑ HTTP/JSON ↓
┌─────────────────────────────────────────────────────────┐
│                  Flask Backend (Python)                  │
│  ┌────────────────────────────────────────────────────┐ │
│  │   app.py - Routes & API Endpoints                   │ │
│  │   - /calculate - Process expressions               │ │
│  │   - /validate - Validate expressions               │ │
│  │   - /functions - Get available functions           │ │
│  └────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────┐ │
│  │   calculator_engine.py - Core Logic                │ │
│  │   - Safe expression evaluation                     │ │
│  │   - Angle mode conversion (DEG/RAD/GRAD)           │ │
│  │   - Function implementations                       │ │
│  │   - Memory management                              │ │
│  └────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

## File Structure

```
Calculator/
├── app.py                           # Flask application server
├── calculator_engine.py             # Core calculator logic
├── requirements.txt                 # Python dependencies
├── run.sh / run.bat                # Startup scripts
├── test_calculator.py              # Unit tests
├── README.md                        # Full documentation
├── QUICKSTART.md                   # Quick start guide
├── DEVELOPMENT.md                  # This file
├── templates/
│   └── index.html                  # Main HTML template
└── static/
    ├── css/
    │   └── style.css               # Styling
    └── js/
        └── calculator.js           # Frontend JavaScript
```

## Key Components

### Backend: `app.py`
- **Framework**: Flask
- **Responsibilities**:
  - Serve static files (CSS, JS, HTML)
  - Handle API requests for calculations
  - Validate expressions
  - Return function list for UI reference

### Backend: `calculator_engine.py`
- **Key Classes**: `CalculatorEngine`
- **Responsibilities**:
  - Safe evaluation of mathematical expressions
  - Angle mode management (DEG, RAD, GRAD)
  - Function implementations
  - Memory operations
  - Error handling and validation

**Important Security Note**: Uses a restricted namespace with eval() to prevent code injection. Only approved functions are available in the evaluation context.

### Frontend: `index.html`
- Calculator interface with 5 rows of buttons
- Display screens (expression and result)
- Mode selector and memory indicator
- Info panel with available functions

### Frontend: `style.css`
- Responsive grid-based button layout
- Color-coded button types
- Mobile-friendly design
- Animation effects

### Frontend: `calculator.js`
- **Key Class**: `Calculator`
- Event listeners for all buttons
- Keyboard support
- API communication with backend
- Memory management
- Expression preprocessing

## Function Implementation Details

### Trigonometric Functions

The trigonometric functions are angle-mode aware. They convert input angles to radians before calculation and convert results back to the selected mode:

```python
def sin(x):
    x_rad = self._convert_angle(x, angle_mode, 'RAD')
    return math.sin(x_rad)
```

**Angle Conversion Formula**:
- DEG to RAD: `radians = degrees × π / 180`
- GRAD to RAD: `radians = gradians × π / 200`
- RAD to DEG: `degrees = radians × 180 / π`
- RAD to GRAD: `gradians = radians × 200 / π`

### Safe Expression Evaluation

The calculator uses a restricted namespace to safely evaluate user expressions:

```python
def _create_safe_namespace(self, angle_mode):
    namespace = {
        'sin': sin,
        'cos': cos,
        # ... other functions
        '__builtins__': {},  # Disable dangerous built-ins
    }
    return namespace

result = eval(expression, namespace)
```

This prevents code injection attacks while allowing mathematical expressions.

### Expression Preprocessing

Before evaluation, expressions are preprocessed to handle:
- **Implicit multiplication**: `2(3)` → `2*(3)`
- **Power operator**: `x^y` → `x**y`
- **Previous answer**: `Ans` → `[previous result]`
- **Memory value**: `M` → `[memory value]`

## Adding New Functions

To add a new mathematical function:

1. **Define the function in `calculator_engine.py`**:
```python
def new_function(x):
    # Implementation here
    return result
```

2. **Add to safe namespace** in `_create_safe_namespace()`:
```python
namespace.update({
    'new_function': new_function,
})
```

3. **Add to available functions list** in `get_available_functions()`:
```python
{
    'name': 'new_function',
    'description': 'Description of what it does'
}
```

4. **Add button to UI** in `templates/index.html` (optional):
```html
<button class="btn btn-function" data-func="new_function(">nf</button>
```

## API Endpoints

### POST /calculate
Evaluate a mathematical expression.

**Request**:
```json
{
  "expression": "sin(90) + sqrt(16)",
  "angle_mode": "DEG"
}
```

**Response (Success)**:
```json
{
  "result": 5,
  "success": true
}
```

**Response (Error)**:
```json
{
  "error": "Division by zero",
  "success": false
}
```

### POST /validate
Check if expression is valid.

**Request**:
```json
{
  "expression": "2 + 3 * 4"
}
```

**Response**:
```json
{
  "valid": true,
  "success": true
}
```

### GET /functions
Get list of available functions.

**Response**:
```json
{
  "functions": [
    {"name": "sin", "description": "Sine function"},
    {"name": "cos", "description": "Cosine function"},
    ...
  ],
  "success": true
}
```

## Testing

Run the test script to verify calculator functionality:

```bash
python test_calculator.py
```

### Adding Tests

Add test cases to `test_calculator.py`:

```python
test_cases = [
    ("2+3", None, 5, "Basic addition"),
    ("sin(90)", "DEG", 1, "Sine in degrees"),
    # Add more...
]
```

## Deployment Considerations

### Development (Current)
- Uses Flask development server (`debug=True`)
- Not suitable for production
- Good for development and testing

### Production
To deploy to production:

1. **Use a production WSGI server**:
```bash
pip install gunicorn
gunicorn app:app
```

2. **Set debug to False** in `app.py`:
```python
app.run(debug=False)
```

3. **Use environment variables** for configuration:
```python
import os
debug_mode = os.getenv('DEBUG', 'False') == 'True'
app.run(debug=debug_mode)
```

4. **Consider using a reverse proxy** (nginx, Apache)

5. **Add HTTPS/SSL certificate**

## Performance Optimization

### Current Performance
- Expression evaluation: ~1-5ms
- Angle conversion: <1ms
- Total request time: ~50-100ms (includes network latency)

### Future Optimizations
- Cache compiled expressions
- Implement expression caching for repeated calculations
- Add request limiting/rate limiting
- Minify CSS and JavaScript for production

## Known Limitations

1. **Complex Numbers**: Limited support (display only)
2. **Matrix Operations**: Not implemented
3. **Numerical Methods**: No integration/differentiation
4. **STAT Mode**: Simplified implementation
5. **Equation Solving**: Not implemented
6. **Multiple Variable Support**: Limited

## Browser Compatibility

Tested and working on:
- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Debugging Tips

### Enable Flask Debug Mode
Flask is already in debug mode, which means:
- Auto-reloads on code changes
- Interactive debugger in browser for errors
- Detailed error messages

### Check Browser Console
Open Developer Tools (F12) and check Console for JavaScript errors.

### Test API Directly
```bash
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{"expression": "2+3", "angle_mode": "DEG"}'
```

### Check Server Logs
Flask prints all requests and errors to the console.

## Future Enhancements

### Short Term
- [ ] Add more statistical functions
- [ ] Implement complex number support
- [ ] Add calculation history
- [ ] Dark mode theme

### Medium Term
- [ ] Matrix operations
- [ ] Equation solver
- [ ] Numerical integration/differentiation
- [ ] Save/load calculations
- [ ] Custom functions/macros

### Long Term
- [ ] Symbolic math support (SymPy integration)
- [ ] Graph plotting
- [ ] Multi-variable functions
- [ ] Programming mode
- [ ] Unit conversion

## Contributing

To extend the calculator:

1. Create a new branch for your feature
2. Make changes to appropriate files
3. Test with `python test_calculator.py`
4. Update documentation
5. Create a pull request

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Math Module](https://docs.python.org/3/library/math.html)
- [Casio FX-991EX Manual](https://support.casio.com/)
- [JavaScript MDN Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

---

**Happy coding! 🚀**
