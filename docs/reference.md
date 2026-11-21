# Calculator reference

The calculator page and the JSON API share one engine, `CalculatorEngine` in `calculator_engine.py`, so the syntax below applies to both. Start the server as described in the [README](../README.md#getting-started) first.

## Expression syntax

| Write | Meaning |
|---|---|
| `+`, `-`, `*`, `/` | Add, subtract, multiply, divide |
| `^` | Power: `2^10` is 1024 |
| `(` and `)` | Grouping: `(2+3)*4` is 20 |
| `pi`, `e` | The constants π and e |
| `Ans` | The last result the server calculated |

A digit directly before `(` or a letter multiplies, so `2(3+4)` is 14 and `2pi` means `2*pi`. The page's ×, ÷ and − keys enter `*`, `/` and `-`.

## Functions

| Function | Result | Page key |
|---|---|---|
| `sin(x)`, `cos(x)`, `tan(x)` | Sine, cosine and tangent of an angle in the selected [angle mode](#angle-modes) | sin, cos, tan |
| `asin(x)`, `acos(x)`, `atan(x)` | Inverse functions, returning an angle in the selected mode; `arcsin`, `arccos` and `arctan` are aliases | sin⁻¹, cos⁻¹, tan⁻¹ |
| `sinh(x)`, `cosh(x)`, `tanh(x)` | Hyperbolic sine, cosine and tangent | None |
| `log(x)` | Base-10 logarithm | log |
| `ln(x)` | Natural logarithm | ln |
| `exp(x)` | e to the power x | e^x |
| `sqrt(x)` | Square root | √ |
| `cbrt(x)` | Cube root, including of negative numbers | ³√ |
| `mod(a, b)` | Remainder of a divided by b | mod |
| `gcd(a, b)`, `lcm(a, b)` | Greatest common divisor and least common multiple | None |
| `P(n, r)`, `C(n, r)` | Permutations and combinations, for 0 ≤ r ≤ n | None |
| `mean([x1, x2, ...])` | Arithmetic mean: `mean([1, 2, 3, 4, 5])` is 3 | None |
| `stdev([x1, x2, ...])` | Sample standard deviation (divides by n − 1) of two or more values | None |

`gcd`, `lcm`, `P` and `C` truncate their arguments to integers. `abs`, `round`, `int` and `float` behave as in Python.

## Angle modes

DEG (the default), RAD and GRAD set how `sin`, `cos` and `tan` read their argument and how `asin`, `acos` and `atan` express their result; the hyperbolic functions ignore the mode. Choose a mode with the DEG, RAD and GRAD buttons on the page, or with the `angle_mode` field of [`POST /calculate`](#post-calculate), which treats any other value as DEG. For example, `sin(90)` is 1 in DEG and `sin(100)` is 1 in GRAD.

## Page keys and keyboard

- `=` evaluates the expression. On success the expression clears and the result shows; on an error the display shows `Error:` and the message, and the expression stays so you can correct it.
- DEL deletes the last character, and AC clears the expression and the result.
- Function keys such as sin enter the function name and an opening parenthesis, `sin(`; close it with the `)` key.
- An operator key replaces an operator already at the end of the expression and does nothing while the expression is empty. To enter a negative number, open a parenthesis first, as in `2*(-3)`.

| Key | Action |
|---|---|
| `0` to `9` | Enter a digit |
| `+`, `-`, `*`, `/`, `^` | Enter an operator |
| `.` | Enter a decimal point, unless the current number already has one |
| Enter or `=` | Evaluate |
| Backspace | Delete the last character |
| Escape | Clear the expression and the result |

The keyboard cannot type letters, parentheses or commas; use the on-screen keys for functions and parentheses.

## Memory

The memory value lives in the page, shows as `M:` next to the angle-mode buttons, and resets to 0 when you reload the page.

| Key | Action |
|---|---|
| M+ | Add the displayed result to memory |
| M− | Subtract the displayed result from memory |
| M= | Replace memory with the displayed result |
| MC | Clear memory to 0 |
| MR | Enter the memory value into the expression |

Because `=` clears the expression, reuse a result by storing it with M= and entering it with MR.

## HTTP API

The API endpoints use JSON; send POST bodies with `Content-Type: application/json`. A failed POST request returns HTTP 400 with an `error` message.

### POST /calculate

| Field | Required | Value |
|---|---|---|
| `expression` | Yes | The expression, as a string |
| `angle_mode` | No | `DEG` (default), `RAD` or `GRAD` |

```bash
curl -X POST http://localhost:5000/calculate -H "Content-Type: application/json" -d '{"expression": "2^10", "angle_mode": "DEG"}'
```

```json
{
  "result": 1024,
  "success": true
}
```

`result` is a number, or a string in `a+bi` form for a complex result. A failed calculation returns `{"error": "<message>", "success": false}` with one of the [error messages](#error-messages); a missing or empty `expression` returns `{"error": "No expression provided"}`.

### POST /validate

Send `{"expression": "2 + 3 * 4"}`; the response is `{"valid": true, "success": true}`, or `"valid": false`. An expression is valid when it is non-empty, has as many `(` as `)` and parses. Function names and values are not checked, so `log(0)` is valid but fails in `POST /calculate`.

### GET /functions

Returns `"success": true` and `functions`, a list of objects such as `{"name": "sin", "description": "Sine function"}`. The page shows this list in its Available Functions panel. The list includes `factorial`; see [Known gaps](#known-gaps).

## Error messages

`POST /calculate` returns these in `error`, and the page shows them after `Error:`.

| Message begins with | Cause | Example |
|---|---|---|
| `Cannot divide by zero` | Division by zero | `1/0` |
| `Math error:` | A value outside a function's domain, or invalid `P`, `C` or `stdev` input | `sqrt(-1)` |
| `Unknown function or variable:` | A name the engine does not define | `sec(30)` |
| `Invalid expression syntax` | The expression does not parse | `(2+3` |
| `Calculation error:` | Any other failure, such as the wrong number of arguments | `log(2, 8)` |

## Troubleshooting

- **The server cannot start because port 5000 is in use.** Change `port=5000` in the `app.run(...)` call at the end of `app.py`, start the server again and open the new port.
- **`ModuleNotFoundError: No module named 'flask'`.** Activate the virtual environment, then run `pip install -r requirements.txt`.
- **`bash run.sh` stops at `✗ Failed to install dependencies`.** Read pip's error above that line. If it says `externally-managed-environment`, your system Python does not accept pip installs: activate a virtual environment as in the [README](../README.md#getting-started), then run the script again.

## Known gaps

- `factorial` does not work: the `n!` key enters `factorial(`, a name the engine does not define, and `5!` is not valid syntax.
- `log(x)` is base 10 only. For another base, divide natural logarithms, as in `ln(8)/ln(2)`.
- On the page you can use only the functions that have a key, and not `mod`, which needs a comma the page cannot enter. Use the API for the other functions and for `Ans`.
- Scientific notation such as `2.5e5` is read as `2.5*e5` and fails; write `2.5*10^5`.
- Complex numbers cannot be entered, although a calculation such as `(-8)^(1/3)` can return one.
- Matrix calculations, equation solving, numerical integration and differentiation, and the FX-991EX's statistics (STAT) mode are not implemented.
