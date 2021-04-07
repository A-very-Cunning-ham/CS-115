# CS 115 Spring 2021 Test 2 

###########################################################################
# RULES REMINDER  You can use the following:
# Canvas to download+upload the exam.
# IDLE to edit this file and check your solutions.
# Zoom for the class meeting: you _must_ stay in the meeting (muted) until 
#   you submit your test.  Use private chat to Dave or a TA if needed.
#   Please refrain from posting everyone in the chat.
# One sheet of paper with handwritten notes on both sides (don't submit it).
# Blank paper if you find that helpful work working on your solutions. 
# No other resources other than your mind.  
# You have until 10:55am
# 
# Name and pledge:
#
#
#
###########################################################################

###########################################################################
# STEP ZERO:
# Please run this file right now to be sure you downloaded it ok,
# and have cs115.py in the same folder.  There should be no error.
###########################################################################

from cs115 import *

print("So far so good...")

###########################################################################
# Question 1 (20 points) 
# This table defines a boolean function, f, of three arguments.
#
#    x | y | z | f(x,y,z)
#    --------------------
#    0 | 0 | 0 | 0
#    0 | 0 | 1 | 1
#    0 | 1 | 0 | 0
#    0 | 1 | 1 | 0
#    1 | 0 | 0 | 0
#    1 | 0 | 1 | 1
#    1 | 1 | 0 | 1
#    1 | 1 | 1 | 1        
# 
# Complete the following Python implementation of f, using a single return.
# Use the built-in Python functions "and", "or", "not".
# Hint: use the minterm expansion principle.
###########################################################################

def f(x, y, z):
    return None # TODO
    
###########################################################################
# Question 2: (20 points) 
# Part A: What is the two's complement representation of 29 in seven bits?
# 
#    A: 1100010
#    B: 0011101
#    C: 1100011
#    D: 1011101
#
# ANSWER = 
###########################################################################
# Part B: What is the two's complement representation of -25 in seven bits?
#
#    A: 0011001
#    B: 1011001
#    C: 1100111
#    D: 1100110
#
# ANSWER =  
###########################################################################
# Part C: Using two's complement with seven bits, what is the largest
# positive number that can be represented?
#    
#    A: 128 (which is 2**7)
#    B: 64 
#    C: 127 
#    D: 63
#
# ANSWER = 
###########################################################################
# Part D: Using two's complement with seven bits, what is the smallest
# number that can be represented (most negative)?
#
#    A: -128 
#    B: -64 
#    C: -127 
#    D: -63
#
# ANSWER = 
############################################################################ 


###########################################################################
# Question 3: (20 points) 
# Complete the following function, using recursion on the lists.  That means 
# you can only access L using the expressions L[0], L==[], and L[1:].  And
# the same for M.   
###########################################################################

def limiter(L,M):
    '''Assume L and M are lists of numbers, and len(L)==len(M). 
    Return a list like L except that at any position i, if L[i] > M[i] then
    the result has M[i] instead of L[i].  For examples see the test function.'''
    pass # TODO


def testLim():
    assert limiter([85,101,100,105], [100,100,100,100]) == [85,100,100,100]
    assert limiter([9,5,7,8], [10,6,7,7]) == [9,5,7,7]

###########################################################################
# Question 4: (5 points)
# Implement this function using filter, lambda, and range.
###########################################################################

def fives(n):
    '''List of all multiples of 5 less than n, assuming n>=0.'''
    pass # TODO


def testFives():
    assert fives(25) == [0, 5, 10, 15, 20]
    assert fives(26) == [0, 5, 10, 15, 20, 25]

###########################################################################
# Question 5: (20 points) 
# Below is an implementation of the edit distance function.
# Improve it by memoization: add code at the places indicated by 'TODO'.
###########################################################################

def ED(first, second):
    '''Returns the edit distance between the strings first and second.'''

    # TODO make a dictionary to use as memo table

  
    def ED_mem(first, second):

        # TODO use answer in memo table, if available
        

        if first == '':
            result = len(second)
        elif second == '':
            result = len(first)
        elif first[0] == second[0]:
            result = ED_mem(first[1:], second[1:])
        else:
            substitution = 1 + ED_mem(first[1:], second[1:])
            deletion = 1 + ED_mem(first[1:], second)
            insertion = 1 + ED_mem(first, second[1:])
            result = min(substitution, deletion, insertion)

        # TODO update memo table 


        return result    

    return ED_mem(first, second)


def testED():
    assert ED("edit", "distance") == 6


###########################################################################
# Question 6: (15 points) 
# Write out the trace of function calls starting from g(4,1) for the
# function g defined below.
# Use indentation to indicate which calls are the result of preceding calls.
#
# Hint: You are welcome to modify the function and make it trace itself.
# But to answer the question you need to write your trace in the comment below.
###########################################################################

def g(n,k):
    '''mystery function'''
    if n <= k:
        return n
    else:
        return g(n-2,k) + g(n-1,k)

'''
TODO - your trace goes here


'''






