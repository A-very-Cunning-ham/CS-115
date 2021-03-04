# CS 115A Fall 2020 - more practice exercise for test

###########################################################################
# RULES: You can use the following:
# Canvas to download+upload the 
# IDLE to edit this file and check your solutions
# Zoom for the class meeting; use private chat to Dave or TAs if needed.
# One sheet of paper with handwritten notes on both sides (don't submit it).
# Blank paper if you find that helpful work working on your solutions  
# No other resources other than your mind.  
#
# Hint: If some of your code doesn't work, comment it out and write a note.
# 
# Name and pledge:
#
###########################################################################

###########################################################################
# STEP ZERO:
# Please run this file right now to be sure you downloaded it ok, and have 
# cs115.py in the same folder.  There should be no error.
###########################################################################

from cs115 import *

###########################################################################
# STEP ONE:
# Using the definition of LCS below, show the trace of function calls
# for the expression LCS("hi", "bi").  Use indentation to show which 
# calls result from previous calls.
###########################################################################

def LCS(S1, S2):
    """Length of longest common subsequence of two lists."""
    if S1 == "" or S2 == "": return 0
    elif S1[0] == S2[0]:  
        return 1 + LCS(S1[1:], S2[1:])
    else:
        return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

"""
ANSWER DONE IN CLASS:

LCS("hi", "bi")
    LCS("hi", "i")
       LCS("hi", "")
       LCS("i", "i")
           LCS("", "")
    LCS("i", "bi")
       LCS("i", "i")
           LCS("", "")
       LCS("", "bi")
"""

###########################################################################
# Here's another tracing problem:  show the function call trace
# for the call quiz(2,7).  Here's the code.
###########################################################################

def quiz(n,k):
    if k == 0: return 1
    elif k % 2 == 0:
        t = quiz(n, k//2)
        return t*t
    else: return n * quiz(n,k-1)

'''
quiz(2, 7)
    quiz(2, 6)
        quiz(2, 3)
            quiz(2, 2)
                quiz(2, 1)
                    quiz(2, 0)
                        
'''


###########################################################################
# Here's a typical question from pencil-and-paper tests.
# You should be able to read this code and figure out what it prints
# without running it in IDLE.
###########################################################################

M = ['what', 'does', 'map', 'really']
L = 2*['do'] + M 
N = [ 'map', L[3], M[2] ]  
print(N)

###########################################################################
# Here's another one like that.
###########################################################################

P = ['climate', 'youth', 'action']
Q = ['united', 'nations', 'leaders']
R = P[:2] + Q[:1] + P[2:] 
print(R)


###########################################################################
# Implement the following function.  
# It should return a list of the values of the polynomial 3x**2+3 (in words:
# three x squared plus three), applied to the first N non-negative integers.
# You may use range, map, lambda, and the exponent operator **.
# Do NOT use recursion.
###########################################################################

def poly(N):
    pass # TO-DO your code here


def testPoly():
    assert ( poly(5) == [3, 6, 15, 30, 51] )


###########################################################################
# Fill in the missing parts in the following code. 
# It should compute the same result as map(lambda x: n*x, L).
###########################################################################

def multAll(n, L):
    '''Assuming n is a number and L is a list of numbers,
       make a list by multiplying each element of L by n.
       For example, multAll(3,[3,5,7,9]) is [9,15,21,27].'''
    if L==[]:

        return None # TO-DO replace None 


    else:

        return None # TO-DO replace None 

###########################################################################
# Complete this function so it uses assert to test multAll on at 
# least the example in the docstring of multAll.
###########################################################################

def testMultAll():
    pass # TO-DO 

