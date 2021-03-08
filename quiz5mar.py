# pop quiz March 5, 2021

###########################################################################
# RULES: You can use the following:
# Canvas to download+upload the exam
# IDLE to edit this file and check your solutions
# Zoom for the class meeting - and you must stay in the meeting (muted) 
#   until you submit your test.  Use private chat to Dave or TAs if needed.
# One sheet of paper with handwritten notes on both sides (don't submit it).
# Blank paper if you find that helpful work working on your solutions  
# No other resources other than your mind.  
# You have until 10:55am.
#
# Hint: If some of your code doesn't work, comment it out and write a note
# so your file still runs.
# 
# Name and pledge:
#
# @author:   Avery Cunningham
# Pledge:    I pledge my honor that I have abided by the Stevens Honor System
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
# Question 1 
# Change the numbers in the list slices below, and nothing else, so that
# it prints   ['yes', 'we', 'survive', 'the', 'pandemic']
###########################################################################

def q1():
    L = ['yes', 'we', 'are', 'trying', 'to', 'survive', 'the', 'pandemic']
    print(L[0:2]+L[5:8])
q1()
###########################################################################
# Question 2
# Using the definition of fib below, show the trace of function calls
# for the expression fib(4). 
###########################################################################

def fib(n):
    if n==0 or n==1: 
        return n
    else: 
        return fib(n-1) + fib(n-2)

'''
TO-DO your trace here 

fib(4)
    fib(3)
        fib(2)
            fib(1)
            fib(0)
        fib(1)
    fib(2)
        fib(1)
        fib(0)
'''


###########################################################################
# Question 3 
# Implement the following, using map and lambda (not recursion).
# Hint: all it needs is a return statement.
# Hint: if you can't figure out lambda, just define a helper function.
###########################################################################

def addQ(strs):
    ''' Assume strs is a list of strings.
        Return a list of the same strings but with ? added at the end.'''
    return map(lambda x: x + "?", strs)

print(addQ(['yes', 'we', 'are', 'trying', 'to', 'survive', 'the', 'pandemic']))

