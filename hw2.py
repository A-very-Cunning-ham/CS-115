'''
Created on 2/22/21
@author:   Avery Cunningham
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
    [['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10]]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']


# Implement your functions here.


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


def removeFirst(e, L):
    """Removes the first first occurrence of element e in list L"""
    if L == []:
        return []
    elif L[0] == e:
        return L[1:]
    else:
        return [L[0]] + removeFirst(e, L[1:])


def wordInRack(rack, word):
    """Returns True if the given word can be made with the letters in the given rack, and False if it can not"""
    if word == "":  # if all letters in the word have been removed then the word can be made with the rack
        return True
    elif rack == []:  # if the rack runs out of letters before the word is made then the word is not in the rack
        return False
    elif word[0] in rack:  # if 1st letter in word is in the rack then remove that letter from the rack and check again with [1:] slice of word in dict
        return wordInRack(removeFirst(word[0], rack), word[1:])
    else:  # if a letter in the word is not in the rack then the word can not be made
        return False


def scoreList(Rack):
    """Takes a rack of lowercase letters and returns all words in the global dictionary that can be spelled from the rack"""
    return map(wordAndScore, filter(lambda x: wordInRack(Rack, x), Dictionary))


def bestWord(Rack):
    """Takes a rack of lowercase letters and returns the highest scoring word in the global dictionary that can be spelled from the rack"""
    return reduce(lambda a, b: a if a[1] > b[1] else b, scoreList(Rack), ["", 0])

