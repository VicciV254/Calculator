"""
Casio FX-991EX Calculator Web Application
Main Flask application
"""
from flask import Flask, render_template, request, jsonify
import json
from calculator_engine import CalculatorEngine

app = Flask(__name__)

# Initialize calculator engine
calc_engine = CalculatorEngine()


@app.route('/')
def index():
    """Render the main calculator page"""
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    """Request and response: docs/reference.md#post-calculate."""
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        angle_mode = data.get('angle_mode', 'DEG')
        
        if not expression:
            return jsonify({'error': 'No expression provided'}), 400
        
        # Calculate result
        result = calc_engine.evaluate(expression, angle_mode)
        
        return jsonify({
            'result': result,
            'success': True
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 400


@app.route('/validate', methods=['POST'])
def validate():
    """Validate mathematical expression"""
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        
        is_valid = calc_engine.validate_expression(expression)
        
        return jsonify({
            'valid': is_valid,
            'success': True
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 400


@app.route('/functions', methods=['GET'])
def get_functions():
    """Get list of available functions"""
    return jsonify({
        'functions': calc_engine.get_available_functions(),
        'success': True
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
