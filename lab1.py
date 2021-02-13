'''
Avery Cunningham
2/11/2021

I pledge my honor that I have abided by the Stevens Honor System
'''
from cs115 import map, reduce
from math import factorial
import math

def inverse(n):
    """Return the inverse of a number as a float"""
    return float(1/n)

def e(n):
    """Approximates the mathematical value of e using taylor expansion. n controls the number of expanded terms and the accuracy of the calculation"""
    return sum(map(inverse, map(factorial, range(0, n+1))))

def error(n):
    """Returns the difference between the e(n) function and the actual value of e as given by Python's math module"""
    return abs(e(n)-math.e)
