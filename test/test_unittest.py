import unittest
import sys
sys.path.append('src')
from calculator import fun1, fun2, fun3, fun4

class TestCalculator(unittest.TestCase):
    def test_fun1(self):
        self.assertEqual(fun1(2, 3), 5)
        self.assertEqual(fun1(-1, 1), 0)
    
    def test_fun2(self):
        self.assertEqual(fun2(5, 3), 2)
        self.assertEqual(fun2(10, 15), -5)
    
    def test_fun3(self):
        self.assertEqual(fun3(4, 5), 20)
        self.assertEqual(fun3(0, 10), 0)
    
    def test_fun4(self):
        self.assertEqual(fun4(2, 3), 11)

if __name__ == '__main__':
    unittest.main()
```


### 6. **Create .gitignore**
```
lab_01/
__pycache__/
*.pyc
.pytest_cache/