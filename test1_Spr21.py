# CS 115 Spring 2021 Test 1

###########################################################################
# RULES: You can use the following:
# Canvas to download+upload the exam
# IDLE to edit this file and check your solutions
# Zoom for the class meeting - and you must stay in the meeting (muted)
#   until you submit your test.  Use private chat to Dave or TAs if needed.
# One sheet of paper with handwritten notes on both sides (don't submit it).
# Blank paper if you find that helpful for working on your solutions
# No other resources other than your mind.
# You have until 10:55am.
#
# Hint: If some of your code doesn't work, comment it out and write a note
# so your file still runs.
#
# Name and pledge:
#
# name: Avery Cunningham
# I pledge my honor that I have abided by the Stevens Honor System
#
#
#
###########################################################################


###########################################################################
# STEP ZERO:
# Please run this file right now to be sure you downloaded it ok,
# and have cs115.py in the same folder.
###########################################################################

from cs115 import *

print("So far so good...")

###########################################################################
# Question 1 (15 points)
# Using the knapsack code below, show the trace of function calls
# from the one given.  Use indentation to show which calls cause which.
# Show all calls and nothing else.
###########################################################################


def knapsack(capacity, items):
    """Max value possible within capacity, assuming capacity >= 0,
    given list of items of the form [weight,value]"""
    if items == []:
        return 0
    elif items[0][0] > capacity:         # check if first item is too heavy
        return knapsack(capacity, items[1:])
    else:
        use = items[0][1] + knapsack(capacity-items[0][0], items[1:])
        lose = knapsack(capacity, items[1:])
        return max(use, lose)


'''
TO-DO your trace here, starting from this call:

 knapsack( 7 ,  [[2, 100], [8, 112], [4, 125]] )
    knapsack(5, [[8, 112], [4, 125]] )
        knapsack(5, [[4, 125]])
            knapsack(1, [])
            knapsack(5, [])
    knapsack(7, [[8, 112], [4, 125]] )
        knapsack(7, [[4, 125]] )
            knapsack(3, [] )
            knapsack(7, [] )


'''

###########################################################################
# Question 2 (5 points)
# Implement this function.  Just use a list slice.  You do not need
# to use recursion or map/reduce.
###########################################################################


def firstHalf(L):
    '''Assuming L is a list with at least two elements, return the first 
    half of the list.  That is, the first len(L)//2 elements.'''
    return L[:len(L)//2]


def testFirstHalf():
    L = ['yes', 'we', 'are', 'trying', 'to', 'survive', 'the', 'pandemic']
    assert firstHalf(L) == ['yes', 'we', 'are', 'trying']
    assert firstHalf(['a', 'b', 'c', 'd', 'e']) == ['a', 'b']


testFirstHalf()
print(firstHalf(['yes', 'we', 'are', 'trying',
                 'to', 'survive', 'the', 'pandemic']))
###########################################################################
# Question 3 (10 points)
# This code does not work quite right: the string it returns is missing
# spaces and commas.  Make a small change in one line of the code so it
# works right.
###########################################################################


def coinNames(coinInfo):
    """Assume coinInfo is a non-empty list of pairs [value,name].
    Return the names, as a string, with the names separated by comma and space."""

    nameList = map(lambda pair: pair[1], coinInfo)
    return reduce(lambda st1, st2: st1 + ', ' + st2, nameList)


def testCoinNames():
    coins1 = [[1, 'penny'], [3, 'nickel'], [7, 'dime']]
    coins2 = [[4, 'penny'], [3, 'nickel']]
    assert coinNames(coins1) == 'penny, nickel, dime'
    assert coinNames(coins2) == 'penny, nickel'


testCoinNames()

###########################################################################
# Question 4 (10 points)
# Implement the palindromes function, using map and lambda and the reverse
# function provided here. Don't use recursion.
# Hint: if you can't figure out lambda, just define a helper function.
###########################################################################


def palindromes(strs):
    ''' Assume strs is a list of strings.
        Return a list of palindromes made by catenating each
        string with its reverse.'''
    return map(lambda x: x + reverse(x), strs)


def reverse(s):
    '''reverse of a string'''
    if s == "":
        return ""
    else:
        return reverse(s[1:]) + s[0]


def testPalindromes():
    assert palindromes(["aha", "stay", "relaxed"]) == [
        'ahaaha', 'stayyats', 'relaxeddexaler']


testPalindromes()
###########################################################################
# Question 5 (15 points)
# Implement the following.  You may use lambda, map, reduce, and/or filter,
# but not recursion.
###########################################################################


def okSquares(nums):
    '''Assume nums is a list of integers.  Return the list of the squares
    of the non-negative ones.'''
    return map(lambda x: x**2, filter(lambda x: x > 0, nums))


def testOkSquares():
    assert okSquares([2, -2, 5, 4, -7]) == [4, 25, 16]
    assert okSquares([-5, -1]) == []


testOkSquares()

###########################################################################
# Question 6 (15 points)
# Implement the following, using recursion.
# Do not use map or filter or okSquares.
###########################################################################


def okSquaresRec(nums):
    '''same as okSquares, but implemented using recursion'''
    if nums == []:
        return []
    elif nums[0] > 0:
        return [nums[0]**2] + okSquaresRec(nums[1:])
    else:
        return okSquaresRec(nums[1:])


def testOkSquaresRec():
    assert okSquaresRec([2, -2, 5, 4, -7]) == [4, 25, 16]
    assert okSquaresRec([-5, -1]) == []


testOkSquaresRec()

###########################################################################
# Question 7 (15 points)
# Implement the exponent function, using recursion.
# Your code should take advantage of this fact about exponent:
#       If k is even then  n ** k  ==  n**(k//2) * n**(k//2)
# For even numbers, make a single recursive call to get k**(k//2),
# and square that number.  For odd k, just use the usual
# form:  n ** k == n * (n ** (k-1)).
# For example, the call trace for exp(2, 7) will be
#
#  exp(2, 7)
#     exp(2, 6)
#        exp(2,3)
#           exp(2,2)
#              exp(2,1)
#                 exp(2,0)
###########################################################################


def exp(n, k):
    """exponent n**k, assuming n is a number and k is an integer, k>=0"""
    if k == 0:
        return 1
    elif k % 2 == 0:
        return exp(n, k//2) ** 2
    else:
        return n * exp(n, k-1)

def testExp():
    assert exp(5,6) == 5**6
    assert exp(2,2) == 2**2
    assert exp(3,3) == 3**3
testExp()

###########################################################################
# Question 8 (15 points)
# Replace each 'None' in dotTR, so it works correctly.
###########################################################################


def dot(L, K):
    '''Assume L and K are lists of numbers, and len(L)==len(K).  Return 
    their dot product.'''
    if L == []:
        return 0
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])


def dotTR(L, K):
    '''same as dot(L,K), but implemented using tail recursion.'''
    def help(M, N, acc):
        if M == []:
            return acc 
        else:
            return help(M[1:], N[1:], acc + (M[0] * N[0]) ) 
    return help(L, K, 0)  


def testDotTR():
    assert dot([2, 7], [3, 1]) == dotTR([2, 7], [3, 1])
    L = [2, 7, 4, 7, 3]
    M = [1, 1, 2, 2, 1]
    assert dot(L, M) == dotTR(L, M)

testDotTR()