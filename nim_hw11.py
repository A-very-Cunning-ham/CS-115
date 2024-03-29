# nim template DNaumann (2018), for assignment nim_hw11.txt 
"""
Created on 4/28/21
@author:   Avery Cunningham
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - HW 11
"""

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:

            print("You win, good job!")

            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:

            print("Better luck next time, I win this one")

            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles
    
    num_piles = -1
    while num_piles < 1:
        num_piles = int(input("Enter how many piles do you want to play with: "))

    piles = [0]*num_piles

    for i in range(num_piles):
        choice = -1
        while choice < 1:
            choice = int(input(f"Enter how many pieces you want in pile #{i}: "))
        piles[i] = choice
        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles

    for idx, val in enumerate(piles):
        print(f"pile {idx} = {val}")


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles

    choice = -1

    while choice not in range(len(piles)):
        choice = int(input(f"Enter which pile you choose: "))

    return choice


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles

    choice = -1

    while choice not in range(1, piles[pnum]+1):
        choice = int(input(f"Enter how many to remove: "))
        
    return choice



def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles 

    nim_sum = 0

    for val in piles:
        nim_sum = nim_sum^val
    
    return nim_sum


def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles 

    nim_sum = game_nim_sum()
    pile_sums = []
    for idx, val in enumerate(piles):
        pile_sum = val^nim_sum
        if pile_sum < val:
            return(idx, val-pile_sum)

    for idx, val in enumerate(piles):
        if val > 0:
            return(idx, 1)


def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles

    print("It's my turn now, watch out")
    opt = opt_play()
    print(f"I remove {opt[1]} from pile {opt[0]}")
    piles[opt[0]] -= opt[1]


#   start playing automatically
if __name__ == "__main__" : play_nim()
