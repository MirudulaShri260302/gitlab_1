# gitlab_1
# MLOps Lab 1 - Calculator with Testing and CI/CD

This repository contains Lab 1 for MLOps (IE-7374) course at Northeastern University, demonstrating best practices for Python development including virtual environments, testing frameworks, and GitHub Actions automation.

## 📁 Project Structure

```
gitlab_1/
├── .github/
│   └── workflows/
│       ├── pytest_action.yml      # GitHub Actions workflow for Pytest
│       └── unittest_action.yml    # GitHub Actions workflow for Unittest
├── src/
│   └── calculator.py              # Calculator functions
├── test/
│   ├── test_pytest.py            # Pytest test cases
│   └── test_unittest.py          # Unittest test cases
├── .gitignore                     # Git ignore file
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🚀 Features

- **Calculator Functions**: Basic arithmetic operations (add, subtract, multiply, combine)
- **Dual Testing Framework**: Both Pytest and Unittest implementations
- **CI/CD Pipeline**: Automated testing with GitHub Actions
- **Virtual Environment**: Isolated Python environment for dependencies

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/MirudulaShri260302/gitlab_1.git
cd gitlab_1
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv lab_01

# Activate virtual environment
# Windows:
lab_01\Scripts\activate
# Mac/Linux:
source lab_01/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🧪 Running Tests

### Run Pytest Tests

```bash
pytest test/test_pytest.py
```

### Run Unittest Tests

```bash
python -m unittest test.test_unittest
```

### Run All Tests

```bash
# Pytest
pytest test/

# Unittest
python -m unittest discover -s test -p "test_*.py"
```

## 📊 Calculator Functions

The calculator module (`src/calculator.py`) includes:

- **fun1(x, y)**: Addition - Returns x + y
- **fun2(x, y)**: Subtraction - Returns x - y  
- **fun3(x, y)**: Multiplication - Returns x * y
- **fun4(x, y)**: Combined operations - Returns fun1 + fun2 + fun3

### Example Usage

```python
from src.calculator import fun1, fun2, fun3, fun4

result1 = fun1(5, 3)    # Returns 8
result2 = fun2(10, 4)   # Returns 6
result3 = fun3(7, 6)    # Returns 42
result4 = fun4(2, 3)    # Returns 10 (5 + (-1) + 6)
```

## 🔄 GitHub Actions Workflows

### Pytest Workflow
- **Trigger**: Push or Pull Request to main branch
- **Actions**: Checkout code → Setup Python → Install dependencies → Run tests → Upload results

### Unittest Workflow
- **Trigger**: Push to main branch
- **Actions**: Checkout code → Setup Python → Install dependencies → Run tests

Both workflows automatically run when code is pushed to the repository.

## ✅ Test Coverage

| Function | Test Cases | Status |
|----------|-----------|--------|
| fun1     | 2 tests   | ✅ Pass |
| fun2     | 2 tests   | ✅ Pass |
| fun3     | 2 tests   | ✅ Pass |
| fun4     | 1 test    | ✅ Pass |

## 📝 Requirements

- Python 3.8+
- pytest 7.4.0
- Git



---

**Last Updated**: November 2025
