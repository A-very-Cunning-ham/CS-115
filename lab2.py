'''
Avery Cunningham
Lab 2
2/18/2021

I pledge my honor that I have abided by the Stevens Honor System
'''


def dot(L, K):
    """Returns the dot product of the elements in lists L and K"""
    if L == [] and K == []:
        return 0.0
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])


def explode(S):
    """Explodes a string into a respective list of single character strings"""
    if S == "":
        return []
    else:
        return [S[0]] + explode(S[1:])


def ind(e, L):
    """Returns the index of the first occurrence of e in L"""
    if L == "" or L == []:  # is there a way to check for a blank string or list with the same syntax? can we use 'not'?
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])


def removeAll(e, L):
    """Removes all top-level occurrences of element e in list L"""
    if L == []:
        return []
    elif L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])


def myFilter(f, L):
    """Returns a list of elements in L where the function f returns True"""
    if L == []:
        return []
    elif f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    else:
        return myFilter(f, L[1:])


def deepReverse(L):
    """Reverses the order of a list and all lists contained within"""
    if L == []:
        return []
    elif isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]
