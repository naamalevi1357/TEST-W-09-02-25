import math
import sqlite3
from logging import raiseExceptions


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def make_error():
    raise IndexError()

def create_table(query):
    # check if table exists
    raise sqlite3.IntegrityError

def say_hello():
    name = input("enter name? ")
    return f"hello {name}"

# a
def power(a,b):
    return a**b

# b
def sqrt(a):
    result= math.sqrt(a)
    return result


# c
def factorial(s):

    if s<0:
        raise ValueError

    else:
        result = math.factorial(s)
        return result

print(factorial(5))
