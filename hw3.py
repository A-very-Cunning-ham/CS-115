'''
Created on 3/3/21
@author: Avery Cunningham
Pledge: I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 3
'''
from cs115 import map
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def giveChange(amount, coins):
    """Returns the minimum number of coins needed to make a given change value with the given list of coins, and returns the coins used"""
    if amount == 0:
        return [0, []]
    elif coins == [] or coins[0] > amount:
        return [float("inf"), []]
    else:
        useIt = giveChange(amount - coins[0], coins)
        # useIt[0] += 1
        # useIt[1].append(coins[0])
        useIt = [useIt[0]+1, useIt[1] + [coins[0]]]
        loseIt = giveChange(amount, coins[1:])
        return min(useIt, loseIt)


print(giveChange(48, [1, 5, 10, 25, 50]))
print(giveChange(48, [1, 7, 24, 42]))
print(giveChange(35, [1, 3, 16, 30, 50]))

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
    [['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10]]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    def letterScore(letter, scorelist):
        """Returns a letter's coresponding score as found in scoreList"""
        if scorelist[0][0] == letter:
            return scorelist[0][1]
        else:
            return letterScore(letter, scorelist[1:])

    def wordScore(S, scorelist):
        """Returns the total score of a word based on individual letter scores as listed in scoreList"""
        if S == "":
            return 0
        else:
            return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

    def wordAndScore(word):
        """Returns a list with the given word and its score as determined by wordScore()"""
        return [word, wordScore(word, scrabbleScores)]

    return map(wordAndScore, dct)


print(wordsWithScore(Dictionary, scrabbleScores))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if L == [] or n == 0:
        return []
    else:
        return [L[0]] + take(n-1, L[1:])

lst = [1, 2, 3, 4]

print(take(0,[]))
assert(lst[0:0] == take(0, lst))
assert(lst[0:1] == take(1, lst))
assert(lst[0:2] == take(2, lst))
assert(lst[0:3] == take(3, lst))
assert(lst[0:4] == take(4, lst))
assert(lst[0:5] == take(5, lst))
assert(lst[0:6] == take(6, lst))
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if L == []:
        return []
    elif n > 0:
        return drop(n-1, L[1:])
    else:
        return [L[0]] + drop(n-1, L[1:])


print(drop(0, lst))
print(drop(1, lst))
assert(lst[0:] == drop(0, lst))
assert(lst[1:] == drop(1, lst))
assert(lst[2:] == drop(2, lst))
assert(lst[3:] == drop(3, lst))
assert(lst[4:] == drop(4, lst))
assert(lst[5:] == drop(5, lst))
assert(lst[6:] == drop(6, lst))