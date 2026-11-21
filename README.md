# Casio FX-991EX Calculator

A browser version of the Casio FX-991EX scientific calculator, backed by a Python (Flask) server that evaluates each expression. Run it on your own machine and use it in a browser; it implements a subset of the FX-991EX's functions.

## Overview

Build an expression with the on-screen keys or your keyboard, then press `=` to see the result. Trigonometric functions follow the selected angle mode: DEG, RAD or GRAD. The memory keys (M+, M−, M=, MC, MR) hold a value in the page. The same calculations are available as a JSON API.

## Getting started

You need Python 3.8 or later, with pip. From the repository root on Linux or macOS, run:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

On Windows, replace the first two commands with `python -m venv venv` and `venv\Scripts\activate`.

Open `http://localhost:5000` in your browser.

## Verification

```bash
python test_calculator.py
curl -X POST http://localhost:5000/calculate -H "Content-Type: application/json" -d '{"expression": "2+3"}'
```

The first checks the calculation engine and exits with status 1 if a check fails; expect the factorial check to fail ([Known gaps](docs/reference.md#known-gaps)). The second needs the running server and returns JSON with `"result": 5`.

## Tech stack

- Python, with Flask 3.0.0 and Werkzeug 3.0.0 pinned in `requirements.txt`
- HTML, CSS and JavaScript, with no framework or build step

## Project structure

```text
.
├── app.py                   # Flask routes: the page and the JSON API
├── calculator_engine.py     # Expression evaluation and calculator functions
├── test_calculator.py       # Engine checks
├── requirements.txt         # Pinned Python dependencies
├── run.sh                   # Installs requirements and starts the server: bash run.sh
├── run.bat                  # The same, for Windows
├── templates/index.html     # Calculator page
├── static/css/style.css     # Page styles
├── static/js/calculator.js  # Keys, keyboard input, memory and API calls
└── docs/reference.md        # Syntax, functions, keys, API and errors
```

## Docs

- [Calculator reference](docs/reference.md): expression syntax, functions, angle modes, page keys and memory, the HTTP API, error messages, troubleshooting and known gaps.

## License

This project is created for educational purposes. The repository has no license file.
