/**
 * Casio FX-991EX Calculator - Frontend
 * Handles UI interactions and API communication
 */

class Calculator {
    constructor() {
        this.expression = '';
        this.result = '0';
        this.angleMode = 'DEG';
        this.memory = 0;
        this.lastAnswer = 0;
        
        // Initialize UI
        this.initializeElements();
        this.attachEventListeners();
        this.loadFunctions();
    }
    
    initializeElements() {
        this.expressionDisplay = document.getElementById('expressionDisplay');
        this.resultDisplay = document.getElementById('resultDisplay');
        this.memoryIndicator = document.getElementById('memoryValue');
        this.functionsList = document.getElementById('functionsList');
        
        this.btnClear = document.getElementById('btnDelete');
        this.btnDelete = document.getElementById('btnDelete');
        this.btnEquals = document.getElementById('btnEquals');
        this.btnMAdd = document.getElementById('btnMAdd');
        this.btnMSub = document.getElementById('btnMSub');
        this.btnMStore = document.getElementById('btnMStore');
        this.btnMClear = document.getElementById('btnMClear');
        this.btnMRecall = document.getElementById('btnMRecall');
    }
    
    attachEventListeners() {
        // Digit buttons
        document.querySelectorAll('.btn-digit').forEach(btn => {
            btn.addEventListener('click', () => {
                const value = btn.dataset.value || btn.dataset.digit;
                this.appendToExpression(value);
            });
        });
        
        // Operator buttons
        document.querySelectorAll('.btn-operator').forEach(btn => {
            btn.addEventListener('click', () => {
                this.appendOperator(btn.dataset.operator);
            });
        });
        
        // Function buttons
        document.querySelectorAll('.btn-function').forEach(btn => {
            btn.addEventListener('click', () => {
                this.appendFunction(btn.dataset.func);
            });
        });
        
        // Delete and Clear buttons
        document.getElementById('btnDelete').addEventListener('click', () => {
            this.deleteLastCharacter();
        });
        
        document.getElementById('btnClear').addEventListener('click', () => {
            this.clear();
        });
        
        // Equals button
        document.getElementById('btnEquals').addEventListener('click', () => {
            this.calculate();
        });
        
        // Memory buttons
        document.getElementById('btnMAdd').addEventListener('click', () => {
            this.addToMemory();
        });
        
        document.getElementById('btnMSub').addEventListener('click', () => {
            this.subtractFromMemory();
        });
        
        document.getElementById('btnMStore').addEventListener('click', () => {
            this.storeMemory();
        });
        
        document.getElementById('btnMClear').addEventListener('click', () => {
            this.clearMemory();
        });
        
        document.getElementById('btnMRecall').addEventListener('click', () => {
            this.recallMemory();
        });
        
        // Mode buttons
        document.querySelectorAll('.mode-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                this.switchMode(btn.dataset.mode);
            });
        });
        
        // Keyboard support
        document.addEventListener('keydown', (e) => {
            this.handleKeyPress(e);
        });
    }
    
    appendToExpression(value) {
        // Prevent multiple decimal points in a number
        if (value === '.') {
            const lastNumber = this.expression.split(/[+\-*/^]/).pop();
            if (lastNumber.includes('.')) {
                return;
            }
        }
        
        this.expression += value;
        this.updateDisplay();
    }
    
    appendOperator(operator) {
        if (this.expression === '') return;
        
        // Replace last operator if expression ends with an operator
        if (/[+\-*/^]$/.test(this.expression)) {
            this.expression = this.expression.slice(0, -1) + operator;
        } else {
            this.expression += operator;
        }
        
        this.updateDisplay();
    }
    
    appendFunction(func) {
        this.expression += func;
        this.updateDisplay();
    }
    
    deleteLastCharacter() {
        this.expression = this.expression.slice(0, -1);
        this.updateDisplay();
    }
    
    clear() {
        this.expression = '';
        this.result = '0';
        this.updateDisplay();
    }
    
    async calculate() {
        if (!this.expression) return;
        
        try {
            this.resultDisplay.classList.add('calculating');
            
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    expression: this.expression,
                    angle_mode: this.angleMode
                })
            });
            
            const data = await response.json();
            
            if (data.success) {
                this.lastAnswer = data.result;
                this.expression = '';
                this.result = this.formatResult(data.result);
                this.resultDisplay.classList.remove('error');
            } else {
                this.result = 'Error: ' + data.error;
                this.resultDisplay.classList.add('error');
            }
        } catch (error) {
            this.result = 'Error: ' + error.message;
            this.resultDisplay.classList.add('error');
        } finally {
            this.resultDisplay.classList.remove('calculating');
            this.updateDisplay();
        }
    }
    
    formatResult(value) {
        if (typeof value === 'string' && value.includes('i')) {
            // Complex number
            return value;
        }
        
        if (typeof value !== 'number') {
            return String(value);
        }
        
        // Very large or very small numbers in scientific notation
        if (Math.abs(value) > 1e10 || (Math.abs(value) < 1e-5 && value !== 0)) {
            return value.toExponential(10).replace(/\.?0+e/, 'e');
        }
        
        // Regular numbers
        if (Number.isInteger(value)) {
            return String(value);
        }
        
        // Round to reasonable decimal places
        return parseFloat(value.toPrecision(12));
    }
    
    updateDisplay() {
        this.expressionDisplay.textContent = this.expression;
        this.resultDisplay.textContent = this.result;
    }
    
    switchMode(mode) {
        this.angleMode = mode;
        
        // Update active button
        document.querySelectorAll('.mode-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        event.target.classList.add('active');
    }
    
    addToMemory() {
        if (this.result !== '0' && this.result !== 'Error') {
            const value = parseFloat(this.result);
            if (!isNaN(value)) {
                this.memory += value;
                this.updateMemoryDisplay();
            }
        }
    }
    
    subtractFromMemory() {
        if (this.result !== '0' && this.result !== 'Error') {
            const value = parseFloat(this.result);
            if (!isNaN(value)) {
                this.memory -= value;
                this.updateMemoryDisplay();
            }
        }
    }
    
    storeMemory() {
        if (this.result !== '0' && this.result !== 'Error') {
            const value = parseFloat(this.result);
            if (!isNaN(value)) {
                this.memory = value;
                this.updateMemoryDisplay();
            }
        }
    }
    
    clearMemory() {
        this.memory = 0;
        this.updateMemoryDisplay();
    }
    
    recallMemory() {
        this.expression += this.memory.toString();
        this.updateDisplay();
    }
    
    updateMemoryDisplay() {
        this.memoryIndicator.textContent = 
            this.memory === 0 ? '0' : this.formatResult(this.memory);
    }
    
    async loadFunctions() {
        try {
            const response = await fetch('/functions');
            const data = await response.json();
            
            if (data.success) {
                const html = data.functions.map(func => `
                    <div class="function-item">
                        <span class="function-name">${func.name}</span>
                        <span class="function-desc">${func.description}</span>
                    </div>
                `).join('');
                
                this.functionsList.innerHTML = html;
            }
        } catch (error) {
            console.error('Failed to load functions:', error);
        }
    }
    
    handleKeyPress(event) {
        const key = event.key;
        
        // Numbers
        if (/[0-9]/.test(key)) {
            this.appendToExpression(key);
        }
        
        // Basic operators
        if (key === '+' || key === '-' || key === '*' || key === '/') {
            event.preventDefault();
            this.appendOperator(key === '*' ? '*' : key === '/' ? '/' : key);
        }
        
        // Decimal point
        if (key === '.') {
            event.preventDefault();
            this.appendToExpression('.');
        }
        
        // Enter or equals
        if (key === 'Enter' || key === '=') {
            event.preventDefault();
            this.calculate();
        }
        
        // Backspace
        if (key === 'Backspace') {
            event.preventDefault();
            this.deleteLastCharacter();
        }
        
        // Escape
        if (key === 'Escape') {
            this.clear();
        }
        
        // Power
        if (key === '^') {
            event.preventDefault();
            this.appendOperator('^');
        }
    }
}

// Initialize calculator when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new Calculator();
});
