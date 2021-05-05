"""
Created on 4/30/21
@author:   Avery Cunningham
Pledge:    I pledge my honor that I have abided by the Stevens Honor System
"""

class Person:
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last

    def asleep(self, time):
        return 0 <= time <= 7
    
    def __str__(self):
        return self.firstName + " " + self.lastName

    def __eq__(self,other):
        return self.firstName == other.firstName \
               and self.lastName == other.lastName

class Student(Person):
    def __init__(self, first, last, age):
        Person.__init__(self, first, last)
        self.age = age
        
    def asleep(self, time):
        return 3 <= time <= 11

    def __str__(self):
        return Person.__str__(self) + ", " + str(self.asleep(4))


class Mudder(Student):
    def __init__(self, first, last, age, dorm):
        Student.__init__(self, first, last, age)
        self.dorm = dorm

    def asleep(self, time):
        return False

class Stevens(Student):
    def __init__(self, first, last, age):
        Student.__init__(self, first, last, age)

    def asleep(self, time):
        return 12 <= time <= 9