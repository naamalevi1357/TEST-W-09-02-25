import pytest
import calculatorpy
from pyexpat import ExpatError

# D
def test_power_16():
    a: int = 2
    b: int = 4
    expected: int = 16

    actual: int = calculatorpy.power(a, b)

    assert actual == expected, " numbers power"


# E
def test_power_9():
    a: int = 2
    b: int = 3
    expected: int = 9

    actual: int = calculatorpy.power(a, b)

    assert actual == expected, " numbers power"

# F
def test_sqrt_25():
    a: int = 25
    expected: int = 5

    actual: int = calculatorpy.sqrt(a)

    assert actual == expected, " numbers sqrt"

# G
def test_sqrt_number_negative():
    a: int = -5

    with pytest.raises(ValueError) as ex:
        calculatorpy.sqrt(a)


# H
def test_factorial_4():
    s: int = 4
    expected: int = 24

    actual: int = calculatorpy.factorial(s)

    assert actual == expected, " numbers factorial"


# I

def test_factorial_5():
    s: int = 5
    expected: int = 120

    actual: int = calculatorpy.factorial(s)

    assert actual == expected, " numbers factorial"


# J
def test_factorial_number_negative():
    s: int = -3


    with pytest.raises(ValueError) as ex:
        calculatorpy.factorial(s)