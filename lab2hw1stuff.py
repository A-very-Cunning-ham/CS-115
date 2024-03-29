# some exercises & some solutions for lab2 and hw1

from cs115 import *

# NEW EXERCISES Use recursion to solve these.


def addOne(lon):
    '''Assuming lon is a list of numbers, make a list by adding one to each.
    This is the same as map(add1, lon) where add1 is a function that adds one.
    Your task is to implement it using recursion, not map.'''
    if lon == []:
        return []
    else:
        return [lon[0] + 1] + addOne(lon[1:])


def test_addOne():
    print(addOne([2, 2]) == [3, 3])
    print(addOne([]) == [])


def sumPos(lon):
    '''Assuming lon is a list of number, return the sum of the positive elements,
    ignoring negative ones.  For example, sumPos([1,-3,0,6]) is 7.
    This is the same as sum(filter(isPos,lon)) where isPos checks for positive.'''
    if lon == []:
        return 0
    elif lon[0] < 0:
        return sumPos(lon[1:])
    else:
        return lon[0] + sumPos(lon[1:])



print(sumPos([1, 2, 3, -5, 5]))
# SOLUTIONS for lab


def dot(L, K):
    '''dot product of equal-length lists L,K of numbers'''
    if L == []:
        return 0
    else:
        return (L[0]*K[0]) + dot(L[1:], K[1:])


def test_dot():
    print(dot([5, 3, 1], [6, 4, 2]) == 44)  # since 5*6 + 3*4 + 1*2 = 44


def explode(s):
    '''list of characters in string s'''
    if s == "":
        return []
    else:
        return [s[0]] + explode(s[1:])


def test_explode():
    print(explode("abc") == ['a', 'b', 'c'])


def myFilter(f, L):
    '''assume f is a unary function to booleans and L a list;
    return the list of elements of L for which f is true'''
    if L == []:
        return []
    elif f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    else:
        return myFilter(f, L[1:])


def even(n): return n % 2 == 0


def test_myFilter():
    print(myFilter(even, [1, 2, 5, 6, 7]) == [2, 6])

# from homework 1


def divides(n):
    '''returns a function that tests whether a number
       is divisible by n'''

    def div(k):
        '''whether k is divisible by n'''
        return n % k == 0

    return div


def prime(n):
    '''whether or not n is prime, assuming n is a non-negative integer'''
    possibleDivs = range(1, n)
    divs = filter(divides(n), possibleDivs)
    return sum(divs) == 1


def testPrime():
    '''print True for each successful test'''
    print(not prime(0))
    print(not prime(1))
    print(prime(2))
    print(prime(3))
    print(not prime(4))
    print(prime(37))
    print(not prime(39))


def primeSuccinct(n):
    return sum(filter(divides(n), range(1, n))) == 1
