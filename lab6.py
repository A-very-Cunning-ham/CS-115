"""
Created on 3/18/21
@author:   Avery Cunningham
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
"""


def isOdd(n):
    """Returns whether or not the integer argument is odd."""
    return n % 2 != 0


# the binary representation of 42 (base 10) is 101010

# odd base 10 numbers have a lsb of 1 in binary where even numbers have a lsb of 0

# removing the lsb from a binary number is the same as integer dividing by 2 in base 10
def numToBinary(n):
    """Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned."""
    if n == 0:
        return ""
    else:
        return numToBinary(n >> 1) + str(int(isOdd(n)))


def binaryToNum(s):
    """Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0."""
    if s == "":
        return 0
    elif len(s) == 1:
        return int(s)
    else:
        return 2 * binaryToNum(s[:-1]) + int(s[-1])


def increment(s):
    """Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1."""
    if s == "11111111":
        return "00000000"  # is there a better way to do this?

    num = numToBinary(binaryToNum(s) + 1)
    return (8 - len(num)) * "0" + num


def count(s, n):
    """Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors."""
    print(s)
    if n > 0:
        count(increment(s), n - 1)


# the ternary value for the decimal number 59 is 2012
# since 2*1 + 1*3 + 0*9 + 2*27 = 59


def numToTernary(n):
    """Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned."""
    if n == 0:
        return ""
    elif n % 3 == 0:
        return numToTernary(n // 3) + "0"
    elif n % 3 == 1:
        return numToTernary(n // 3) + "1"
    else:
        return numToTernary(n // 3) + "2"


def ternaryToNum(s):
    """Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0."""
    if s == "":
        return 0
    elif len(s) == "1":
        return int(s)
    else:
        return 3 * ternaryToNum(s[:-1]) + int(s[-1])