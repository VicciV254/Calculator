@echo off
REM Startup script for Casio FX-991EX Calculator Web App on Windows

echo ================================
echo Casio FX-991EX Calculator
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo Checking dependencies...
python -m pip install -q -r requirements.txt

if errorlevel 1 (
    echo Failed to install dependencies
    pause
    exit /b 1
)

echo Dependencies installed successfully
echo.
echo Starting Flask development server...
echo Open your browser and go to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py
pause
