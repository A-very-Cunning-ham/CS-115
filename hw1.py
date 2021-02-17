'''
Avery Cunningham
Homework 1
2/11/2021

I pledge my honor that I have abided by the Stevens Honor System
'''

from cs115 import *


def mult(x, y):
    """Returns the product of x and y"""
    return x * y


def add(x, y):
    """Returns the sum of x and y"""
    return x + y


def factorial(n):
    """Takes a positive integer n and returns its factorial (n!)"""
    return reduce(mult, range(1, n+1))


def mean(L):
    """Returns the numerical average of the values in the list L"""
    return float(reduce(add, L)/len(L))


def divides(n):
    """Returns the div function which takes n mod k"""
    def div(k):
        return n % k == 0
    return div

def primes(n):
    """Returns true if integer n is prime, and false if it is coprime"""
    return sum(map(divides(n), range(2, n))) == 0 and n > 1
