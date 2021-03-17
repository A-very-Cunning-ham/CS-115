# map/reduce/filter exercise

# You can use 'in', len, map, filter, and reduce, but try to solve it without
# using fancy Python library functions.

from cs115 import *

Vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

S = '''On this first Monday of October, students and adults alike
are encouraged to BlueUp by wearing our blue shirt or their own
to make that the day that bullying prevention is heard around the world
We chose blue because in many diverse cultures blue brings peace
'''

listOfWords = S.split()

def deVowel(w):
    """Assuming w is a word, remove its vowels.
    For example, deVowel('friday') is 'frdy'."""
    return None # TO-DO

'''Now, change the expression in this assignment so it sets longest to
be one of the longest words in listOfWords, ignoring vowels.  One correct
answer is 'students'. '''


longest = None # TO-DO
                                                             
print(longest)

