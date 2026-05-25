#!/bin/bash
# Startup script for Casio FX-991EX Calculator Web App

echo "================================"
echo "Casio FX-991EX Calculator"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

# Check if requirements are installed
echo "Checking dependencies..."
python3 -m pip install -q -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "✗ Failed to install dependencies"
    exit 1
fi

echo ""
echo "Starting Flask development server..."
echo "Open your browser and go to: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the application
python3 app.py
