'''
Created on 2/25/21
@author:   Avery Cunningham
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 2
'''


def change(amount, coins):
    if amount == 0:
        return 0
    elif coins == [] or coins[0] > amount:
        return float("inf")
    else:
        useIt = 1 + change(amount - coins[0], coins)
        loseIt = change(amount, coins[1:])
        return min(useIt, loseIt)


print(change(48, [1, 5, 10, 25, 50]))
