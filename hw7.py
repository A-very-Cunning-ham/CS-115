"""
Created on 3/31/21
@author:   Avery Cunningham
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - HW 7
"""


def numToBaseB(N, B):
    """Converts non-negative base 10 integer N to a string in base B"""

    def helper(N, B):
        """Helps account for base case"""
        if N == 0:
            return ""
        else:
            return helper(N // B, B) + str(N % B)

    if N == 0:
        return "0"
    else:
        return helper(N, B)


assert numToBaseB(4, 2) == "100"
assert numToBaseB(4, 3) == "11"
assert numToBaseB(4, 4) == "10"
assert numToBaseB(0, 4) == "0"
assert numToBaseB(0, 2) == "0"


def baseBToNum(S, B):
    """Converts number string S stored in base B to a base 10 integer"""
    if S == "":
        return 0
    else:
        return int(S[-1]) + B * baseBToNum(S[:-1], B)


assert baseBToNum("11", 2) == 3
assert baseBToNum("11", 3) == 4
assert baseBToNum("11", 10) == 11
assert baseBToNum("", 10) == 0
assert baseBToNum("12345", 10) == 12345


def baseToBase(B1, B2, SinB1):
    """Converts the numeric string SinB1, stored in base B1, to a string in base B2"""
    return numToBaseB(baseBToNum(SinB1, B1), B2)


assert baseToBase(2, 10, "11") == "3"  # 11 in base 2 is 3 in base 10...
assert baseToBase(10, 2, "3") == "11"  # 3 in base 10 is 11 in base 2...
assert baseToBase(3, 5, "11") == "4"  # 11 in base 3 is 4 in base 5...


def add(S, T):
    """Returns the binary string sum of two binary strings"""
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)


assert add("11", "01") == "100"
assert add("011", "100") == "111"
assert add("110", "011") == "1001"

FullAdder = {
    ("0", "0", "0"): ("0", "0"),
    ("0", "0", "1"): ("1", "0"),
    ("0", "1", "0"): ("1", "0"),
    ("0", "1", "1"): ("0", "1"),
    ("1", "0", "0"): ("1", "0"),
    ("1", "0", "1"): ("0", "1"),
    ("1", "1", "0"): ("0", "1"),
    ("1", "1", "1"): ("1", "1"),
}


def addB(a, b):
    """Returns the sum of two binary strings, with all calculations done using binary strings"""

    def helper(a, b, carry):
        """Allows for full adder operation with a carry bit"""
        if a == "" and b == "":
            if carry == "0":
                return ""
            else:
                return "1"
        elif a == "":
            f = FullAdder[("0", b[-1], carry)]
        elif b == "":
            f = FullAdder[(a[-1], "0", carry)]
        else:
            f = FullAdder[(a[-1], b[-1], carry)]
        return helper(a[:-1], b[:-1], f[1]) + f[0]

    return helper(a, b, "0")


assert addB("11", "1") == "100"
assert addB("011", "100") == "111"