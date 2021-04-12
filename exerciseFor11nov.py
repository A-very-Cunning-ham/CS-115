# class exercise using for-loop

from cs115 import *


def mapSqr(L):
    '''Assume L is a list of numbers; return map(sqr,L).
    Use a for-loop.'''
    result = []
    for i in L:
        # result += [i*i]
        result.append(i * i)
    return result


def mapSqr2(L):
    '''Assume L is a list of numbers; return map(sqr,L).
    Use a for-loop.'''
    return [i * i for i in L]


def testMapSqr():
    assert mapSqr([1, 2, 3]) == map(lambda x: x * x, [1, 2, 3])
    assert mapSqr2([1, 2, 3]) == map(lambda x: x * x, [1, 2, 3])


testMapSqr()