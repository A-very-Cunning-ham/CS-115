#
# life.py - Game of Life lab
#
# @author:   Avery Cunningham
# Pledge:    I pledge my honor that I have abided by the Stevens Honor System
#

import random
import sys


def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row


def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]  # What do you need to add a whole row here?
    return A


assert createBoard(5, 3) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


def printBoard(A):
    """
    this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')


# A = createBoard(5,3)
# printBoard(A)


def diagonalize(width, height):
    """
    creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A


assert diagonalize(7, 6) == [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0],
                             [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0],
                             [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0]]


def innerCells(width, height):
    """
    creates an empty board and then modifies it so it has all live cells
    except a one-cell-wide boarder of empty cells around the edge
    """
    A = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            A[row][col] = 1

    return A


assert innerCells(5, 5) == [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0],
                            [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]


def randomCells(width, height):
    """
    creates an empty board and then modifies it so it has all random cell values
    except a one-cell-wide boarder of empty cells around the edge
    """
    A = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            A[row][col] = random.choice([0, 1])

    return A


# A = randomCells(10, 10)
# printBoard(A)


def copy(A):
    """Make a deep of the given board array"""
    width = len(A[0])
    height = len(A)

    new = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            new[row][col] = A[row][col]
    return new


oldA = createBoard(2, 2)
assert oldA == [[0, 0], [0, 0]]
newA = copy(oldA)
assert newA == [[0, 0], [0, 0]]
oldA[0][0] = 1
assert oldA == [[1, 0], [0, 0]]
assert newA == [[0, 0], [0, 0]]


def innerReverse(A):
    """Creates a copy of A where all cell values are inverted except around the outer edge"""
    width = len(A[0])
    height = len(A)
    rev = copy(A)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if rev[row][col] == 1:
                rev[row][col] = 0
            else:
                rev[row][col] = 1
    # do i need to manually set the boarders to zero like this?
    for row in [0, height - 1]:
        for col in [0, width - 1]:
            rev[row][col] = 0

    return rev


# A = randomCells(8,8)
# printBoard(A)
# A2 = innerReverse(A)
# printBoard(A2)

# assert innerReverse(diagonalize(3,3)) == [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
# printBoard(innerReverse(diagonalize(6,6)))


def next_life_generation(A):
    """
    makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.
    """
    width = len(A[0])
    height = len(A)
    newA = copy(A)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            neighbors = 0 - A[row][col]

            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighbors += A[row + i][col + j]

            if neighbors < 2:
                newA[row][col] = 0
            elif neighbors > 3:
                newA[row][col] = 0
            elif neighbors == 3:
                newA[row][col] = 1
            else:
                newA[row][col] = A[row][col]
    return newA


A = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0]]
assert A == [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
A2 = next_life_generation(A)
printBoard(A2)

assert A2 == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0],
              [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
A3 = next_life_generation(A2)

assert A3 == [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
