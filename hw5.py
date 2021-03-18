"""
Created on 3/17/21
@author:   Avery Cunningham
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 5 (Rev. Oct 2020 by D.N.)
"""
from turtle import Turtle, Screen # Needed for graphics


def sv_tree(trunk_length, levels):
    """Recursively draw a tree with segments of trunk_length and with the supplied number of levels"""
    if levels > 0:
        if levels > 3:  # a little extra logic to put green leaves on brown branches when levels > 3
            turtle.color("brown")
        else:
            turtle.color("green")

        turtle.pendown()
        turtle.forward(trunk_length)
        turtle.left(30)
        sv_tree(trunk_length / 2, levels - 1)
        turtle.right(60)
        sv_tree(trunk_length / 2, levels - 1)
        turtle.left(30)
        turtle.penup()  # avoid drawing over branch with the wrong color when returning home
        turtle.backward(trunk_length)


def fast_lucas(n):
    """Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]"""
    def lucas_helper(n, memo):
        """A helper function to use memoization with the fast_lucas function"""
        if n in memo:
            return memo[n]
        if n == 0:
            ans = 2
        elif n == 1:
            ans = 1
        else:
            ans = lucas_helper(n-1, memo) + lucas_helper(n-2, memo)
        memo[n] = ans
        return ans
    return lucas_helper(n, {})


def fast_change(amount, coins):
    """Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance."""

    def fast_change_helper(amount, coins, memo):
        """Does the job of fast_change, assuming coins is a tuple."""
        if (amount, coins) in memo:
            return memo[(amount, coins)]
        elif amount == 0:
            memo[(amount, coins)] = 0
            return 0
        elif coins == ():
            memo[(amount, coins)] = float("inf")
            return float("inf")
        elif coins[0] > amount:
            ans = fast_change_helper(amount, coins[1:], memo)
            memo[(amount, coins)] = ans
            return ans
        else:
            useIt = 1 + fast_change_helper(amount - coins[0], coins, memo)
            loseIt = fast_change_helper(amount, coins[1:], memo)
            ans =  min(useIt, loseIt)
            memo[(amount, coins)] = ans
            return ans

    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})


# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123



print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
screen = Screen()
turtle = Turtle()
turtle.speed("fastest")
turtle.left(90)
sv_tree(128, 2)
screen.mainloop()
