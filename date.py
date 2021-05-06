'''
"""
Created on 5/5/21
@author:   Avery Cunningham
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
        self.day == d2.day

    def tomorrow(self):
        """Updates the date object to represent the next day, 
        changing the month and year as necessary"""
        if self.isLeapYear():
            dates = list(DAYS_IN_MONTH)
            dates[2] += 1
        else:
            dates = list(DAYS_IN_MONTH)

        if self.day == dates[self.month]:
            self.day = 1
            if self.month == 12:
                self.year += 1
                self.month = 1
            else:
                self.month += 1
        else:
            self.day += 1

    def yesterday(self):
        """Updates the date object to represent the previous, 
        changing the month and year as necessary"""
        if self.day == 1:
            if self.month == 1:
                self.year -= 1
                self.month = 12
            else:
                self.month -= 1

            if self.isLeapYear():
                dates = list(DAYS_IN_MONTH)
                dates[2] += 1
            else:
                dates = list(DAYS_IN_MONTH)
            self.day = dates[self.month]

        else:
            self.day -= 1

    def addNDays(self, N):
        """Increments the current date by the number of days N"""
        for _ in range(N):
            print(self)
            self.tomorrow()
        print(self)

    def subNDays(self, N):
        """Decrements the current date by the number of days N"""
        for _ in range(N):
            print(self)
            self.yesterday()
        print(self)

    def isBefore(self, d2):
        """Returns True if the calling object comes before d2 
        chronologically, and False otherwise"""
        if self.year != d2.year:
            return self.year < d2.year
        elif self.month != d2.month:
            return self.month < d2.month
        elif self.day != d2.day:
            return self.day < d2.day
        else:
            return False

    def isAfter(self, d2):
        """Returns True if the calling object comes after d2 
        chronologically, and False otherwise"""
        if self.equals(d2):
            return False
        else:
            return not self.isBefore(d2)

    def diff(self, d2):
        """Return the number of days between the calling object and d2
        represents self-d2, so negative results mean self is before d2"""
        if self.equals(d2):
            return

        temp = self.copy()

        if self.isBefore(d2):
            step = temp.tomorrow
            sign = -1
        else:
            step = temp.yesterday
            sign = 1

        counter = 0
        while not temp.equals(d2):
            step()
            counter += 1
        return counter * sign

    def dow(self):
        """Returns the day of the week for the calling object"""
        reference = Date(11, 6, 2011)  # a wednesday
        diff = self.diff(reference)

        mod = diff % 7

        if mod == 0:
            return "Sunday"
        if mod == 1:
            return "Monday"
        if mod == 2:
            return "Tuesday"
        if mod == 3:
            return "Wednesday"
        if mod == 4:
            return "Thursday"
        if mod == 5:
            return "Friday"
        if mod == 6:
            return "Saturday"