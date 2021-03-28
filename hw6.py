"""
Created on 3/25/21
@author:   Avery Cunningham
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 6
"""
from cs115 import map, reduce

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def isOdd(n):
    """Returns whether or not the integer argument is odd."""
    return n % 2 != 0


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


def pad(n):
    """Adds an appropriate number of zeros to a binary string to make it COMPRESSED_BLOCK_SIZE long"""
    return (COMPRESSED_BLOCK_SIZE - len(n)) * "0" + n


def str_flip(s):
    """Flips a bit that is stored as a string"""
    if s == "0":
        return "1"
    else:
        return "0"


def compress(S):
    """Takes a binary string S and returns the run length encoded compressed version of it"""
    S = list(S)
    def run(a, b):
        """Helper function to return a list of bits and their occurrences in S"""
        if a[-1][0] == b:
            a[-1][1] += 1
            if a[-1][1] == MAX_RUN_LENGTH:
                a = a + [[str_flip(b), 0]]
            return a
        else:
            return a + [[b, 1]]

    return reduce(
        lambda x, y: x + y,
        map(lambda x: pad(numToBinary(x[1])), reduce(run, S, [["0", 0]])))


def uncompress(s):
    """Decompresses a run length encoded binary string into the original string"""
    def helper(s, c):
        """Helper that expands binary numbers to a number of respective bits according to the encoding pattern"""
        if s == "":
            return ""
        return binaryToNum(s[:COMPRESSED_BLOCK_SIZE]) * c + helper(
            s[COMPRESSED_BLOCK_SIZE:], str_flip(c))
    return helper(s, "0")

def compression(S):
    """Returns the compression ratio of the string S when encoded with the compress function"""
    return len(compress(S)) / len(S)

# Laicompress can not exist because data with no repetitions or patterns can not be compressed
# if it were possible to always compress an input with Laicompress, then you could successively
# use this algorithm to infinitely compress any input. this is clearly impossible

