'''
Created on 3/4/21
@author:   Avery Cunningham
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 4
'''


def knapsack(capacity, itemList):
    """Given a list of item weights and values, return the most valuable combination of items that weigh less than capacity"""

    if itemList == [] or capacity == 0:
        return [0, []]
    elif itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    else:
        useIt = knapsack(capacity - itemList[0][0], itemList[1:])
        useIt = [useIt[0] + itemList[0][1], [itemList[0]] + useIt[1]]

        loseIt = knapsack(capacity, itemList[1:])
        return max(useIt, loseIt)
