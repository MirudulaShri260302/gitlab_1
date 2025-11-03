import sys
sys.path.append('src')
from calculator import fun1, fun2, fun3, fun4

def test_fun1():
    assert fun1(2, 3) == 5
    assert fun1(-1, 1) == 0

def test_fun2():
    assert fun2(5, 3) == 2
    assert fun2(10, 15) == -5

def test_fun3():
    assert fun3(4, 5) == 20
    assert fun3(0, 10) == 0

def test_fun4():
    assert fun4(2, 3) == 10 
