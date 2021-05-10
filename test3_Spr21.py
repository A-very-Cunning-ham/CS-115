# CS 115 Spring 2021 Test 3 SOLUTION

###########################################################################
# RULES: You can use the following:
# Canvas to download+upload the exam
# IDLE to edit this file and check your solutions
# Zoom for the class meeting: you _must_ stay in the meeting (muted) until 
#   you submit your test.  Use private chat to Dave or a TA if needed.
#   Please refrain from posting everyone in the chat.
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
#
#
###########################################################################

###########################################################################
# STEP ZERO:
# Please run this file right now to be sure you downloaded it ok.
# You don't need cs115.py but you may import it if you like.
###########################################################################


###########################################################################
# Question 1 (20 points) 
# Using a loop, implement the following.
# You may use the list() function.  
###########################################################################

def copyTicTac(board):
    '''Assume board is a list of lists of 0s and 1s.
    Return a deep copy.'''
    pass # TO-DO




def testCopy():
    '''Should print [[0,0,0],[0,0,0],[0,0,0]] '''
    B1 = [[0,0,0],[0,0,0],[0,0,0]]
    B2 = copyTicTac(B1)
    B1[1][1] = 1
    print(B2)

    
###########################################################################
# Question 2 (15 points) 
# Show a trace of the loop in this code, for the given test,
# in the comment below.
###########################################################################    

def binsearch(L, i, x):
    '''Assuming L[0:i] is sorted and 0 <= i <= len(L),
       return j such that 0 <= j <= i and L[0:j] <= x < L[j:i].'''    
    j = 0  
    hi = i
    n = 0
    # invariant: L[0:j] <= x < L[hi:i] and j <= hi
    while j != hi:
        n += 1
        mid = (hi + j) // 2 
        if L[mid] <= x:
            j = mid + 1
        else:
            hi = mid
    return j

def testBinsearch():
    L = [1,3,4,7,10,13,14,20,26]
    binsearch(L, len(L), 15)

''' TO-DO Fill in this table to show the values of the variables
before each iteration, and also a row to show after the last iteration.

j hi n 
----------







'''

###########################################################################
# Question 3 (10 points) 
# The copy() method is not correct.  Fix it so it makes a new object.
###########################################################################

class Duck(object):

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self): 
        return self.name + " " + str(self.age)

    def getAge(self):
        return self.age

    def birthday(self):
        self.age += 1

    def copy(self):
        '''Return a copy of self.'''
        return self  # TO-DO: replace this line with correct code
  
def testDuck():
    '''test whether copy() makes a separate object'''
    c = Duck("Attila", 149)
    d = c.copy()
    c.birthday()
    assert c.getAge() == 150
    assert d.getAge() == 149


###########################################################################
# Question 4 (20 points) 
# In the code below, class Commissioned inherits __str__ and overrides 
# compensation(). Finish the implementation of compensation() in class
# Commissioned, where it says TO-DO. Do not add or change any other code.
#
# Hint: your code should call Employee.compensation().
###########################################################################

class Employee(object):
    def __init__(self, name, hours_per_week, hourly_rate):
        self.__name = name
        self.__hours_per_week = hours_per_week
        self.__hourly_rate = hourly_rate

    def compensation(self):
        '''Annual compensation, assuming 50 weeks worked per year.'''
        return 50 * self.__hours_per_week * self.__hourly_rate

    def __str__(self):
        return 'Employee: ' + self.__name + ' Yearly compensation: ' + str(self.compensation())

class Commissioned(Employee):
    '''Represents an employee who earns a 10 percent commission on sales.'''
    
    def __init__(self, name, hours_per_week, hourly_rate, annual_sales):
        Employee.__init__(self, name,hours_per_week, hourly_rate)
        # Alternatively: super().__init__(....)
        self.__annual_sales = annual_sales

    def compensation(self):
        '''Return the annual compensation: hourly earnings plus 0.10 times annual sales.'''
        pass # TO-DO 


def testComm():
    m = Commissioned("Ursula Burns", 50, 50.0, 270000.0)
    print(m)
    m = Commissioned("Dave", 50, 20.0, 100.0)
    print(m)
    '''This should print two lines:
           Employee: Ursula Burns Yearly compensation: 152000.0
           Employee: Dave Yearly compensation: 50010.0
    '''

###########################################################################
# Question 5 (10 points) 
# Implement triangle() so that it does what the docstring says.
# Hint: you may use * for strings, and implement it with a loop, or
# recursion, or whatever.  
###########################################################################

def triangle(letter, n):
    '''Assume n > 0 and letter is a string of length one.
    Print N rows with 1, 2, 3, ... n copies of the letter.'''
    pass # TO-DO


def testTri():
    '''This should print the following:
a
aa
aaa
aaaa
aaaaa
    '''
    triangle('a', 5)


###########################################################################
# Question 6 (25 points) 
# Finish the code so it works correctly.  Do not change anything except
# to delete the 'pass' statement and replace it with your code.
# You may use the append method for Lists.
###########################################################################

def unionSorted(L,M):
    '''Assume L and M are sorted and neither list has any repeated elements.
    Return a sorted list of all their elements but no repeated ones.'''
    res = [] # accumulates the result
    i = 0    # index for L
    j = 0    # index for M
    # Get elements from the lists, similarly to intersection of sorted lists
    # Invariant: res is the union of L[:i] and M[:j].
    while i < len(L) and j < len(M):
        # Add code to compare L[i] and M[j] and update i, j, and/or res accordingly.
        # Hint: i or j or both should be incremented, based on the comparison
        # and an element should be appended to res.


        pass # TO-DO




       
    # Get any remaining elements - keep this code
    if i < len(L):
        res += L[i:]
    elif j < len(M):
        res += M[j:] 
    return res

def testUnionSorted():
    L1 = ["Chance", "Meshell"]
    L2 = ["Esperanza", "Thundercat"]
    assert unionSorted(L1,L2) == ['Chance', 'Esperanza', 'Meshell', 'Thundercat']
   
    M1 = ["Chance", "Esperanza Spalding",  "Meshell Ndegeocello", "St Vincent", "Travi$"]
    M2 = ["Chance", "Meshell Ndegeocello", "Thundercat"]
    assert unionSorted(M1,M2) == ['Chance', 'Esperanza Spalding', 'Meshell Ndegeocello', \
                                  'St Vincent', 'Thundercat', 'Travi$']


###########################################################################
# Question 7: (10 points BONUS) 
# Below is a solution for the limiter() function from Test 2. 
# Add code where it says TO-DO so it works correctly.
# Don't change the provided code.
###########################################################################

def limiter(L,M):
    '''Assume L and M are lists of numbers, and len(L)==len(M). 
    Return a list like L except that at any position i, if L[i] > M[i] then
    the result has M[i] instead of L[i].'''
    if L == []:
        return []
    elif L[0] <= M[0]:
        return [ L[0] ] + limiter(L[1:], M[1:])
    else:
        return [ M[0] ] + limiter(L[1:], M[1:])

def limiterLoop(L,M):
    '''same as limiter()'''
    result = list(L)        # copy of L

    
    pass # TO-DO use a loop to compute result





    return result

            
def testLim():
    assert limiterLoop([85,101,100,105], [100,100,100,100]) == [85,100,100,100]
    assert limiterLoop([9,5,7,8], [10,6,7,7]) == [9,5,7,7]


