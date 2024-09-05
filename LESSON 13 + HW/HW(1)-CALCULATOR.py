# HOMEWORK 1 CALCULATOR

# CALCULATOR
# a. Add the power function to the calculator
# b. Add the sqrt function to the calculator
# c. Add the is_prime function to the calculator
# d. Add the factorial function to the calculator
# e. Write the tests

# START

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

# a. Add the power function to the calculator:
def power(base, exponent):
    return base ** exponent

# b. Add the sqrt function to the calculator:
import math

def sqrt(number):
    return math.sqrt(number)

# c. Add the is_prime function to the calculator:
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# d. Add the factorial function to the calculator:
def factorial(n):
    if n < 0:
        raise ValueError("factorial not defined for negative values")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# e. Write the tests:
import pytest
import math
from calculator import power, sqrt, is_prime, factorial

def test_power_2_4():
    assert power(2, 4) == 16

def test_power_3_2():
    assert power(3, 2) == 9

def test_power_9_0():
    assert power(9, 0) == 1

def test_sqrt_25():
    assert sqrt(25) == 5

def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-5)

def test_is_prime_1():
    assert not is_prime(1)

def test_is_prime_2():
    assert is_prime(2)

def test_is_prime_16():
    assert not is_prime(16)

def test_is_prime_negative_3():
    assert not is_prime(-3)

def test_is_prime_0():
    assert not is_prime(0)

def test_factorial_4():
    assert factorial(4) == 24

def test_factorial_0():
    assert factorial(0) == 1

def test_factorial_1():
    assert factorial(1) == 1

def test_factorial_5():
    assert factorial(5) == 120

def test_factorial_negative_3():
    with pytest.raises(ValueError):
        factorial(-3)

# END