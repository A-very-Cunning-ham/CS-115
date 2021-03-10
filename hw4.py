'''
Created on 3/9/21
@author: Avery Cunningham
Pledge: I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 4
'''


def pascal_row(n):
    """Given a row number n, return that row in Pascal's Triangle"""
    # it seemed very inefficient to use this function to assist pascal_triangle, since pascal_row would need to compute the whole triangle to return just the last row.
    # calling pascal_row from pascal_triangle recursively to build a triangle would needlessly recalculate the triangle n times.
    # to avoid this i switched the order of the calculation around and just grab the last row off the pascal triangle for n
    return pascal_triangle(n)[-1:][0]


def pascal_triangle(n):
    """Given an integer n, returns a list of lists containing the rows of Pascal's Triangle of the all the rows up to and including row n"""
    def pascal_triangle_tail(n, L):
        """Uses tail end recursion to compute the list of rows"""
        def adjacentSum(row):
            """Sums the adjacent numbers in a row"""
            if len(row) == 1:
                return []
            else:
                return [row[0] + row[1]] + adjacentSum(row[1:])

        if n == 0:
            return L
        else:
            return pascal_triangle_tail(n-1, L + [[1] + adjacentSum(L[-1:][0]) + [1]])

    return pascal_triangle_tail(n, [[1]])


def test_pascal_row():
    """run tests for pascal_row()"""
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(2) == [1, 2, 1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]


def test_pascal_triangle():
    """run tests for pascal_triangle()"""
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [
        1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]


test_pascal_row()
test_pascal_triangle()
