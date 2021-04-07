# mandelbrot.py
# Lab 9
#
# Name:

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:


def mult(c, n):
    """Returns c*n but does the calculation using addition"""
    result = 0
    for _ in range(n):
        result += c
    return result


assert mult(6, 7) == 42
assert mult(1.5, 28) == 42.0


def update(c, n):
    """update starts with z=0 and runs z = z**2 + c for a total of n times. It returns the final z."""
    z = 0
    for _ in range(n):
        z = z**2 + c
    return z


assert update(1, 3) == 5
assert update(-1, 3) == -1
assert update(-1, 10) == 0
print("This should be a big number: ", update(1, 10))


def inMSet(c, n):
    """
    inMSet takes in
        c for the update step of z = z**2+c
        n, the maximum number of times to run that step
    Then, it should return
        False as soon as abs(z) gets larger than 2
        True if abs(z) never gets larger than 2 (for n iterations)
    """
    z = 0
    for _ in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True


c = 0 + 0j  # this one is in the set
assert inMSet(c, 25) == True

c = 3 + 4j  # this one is NOT in the set
assert inMSet(c, 25) == False

c = 0.3 + -0.5j  # this one is also in the set
assert inMSet(c, 25) == True

c = -0.7 + 0.3j  # this one is NOT in the set
assert inMSet(c, 25) == False

c = 0.42 + 0.2j
assert inMSet(c, 25) == True  # this one seems to be in the set
assert inMSet(c, 50) == False  # but it turns out that it's not!


def weWantThisPixel(col, row):
    """ a function that returns True if we want
    the pixel at col, row and False otherwise
    """
    if col % 10 == 0 or row % 10 == 0:
        return True
    else:
        return False


def test():
    """ a function to demonstrate how
    to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()


def scale(pix, pixMax, floatMin, floatMax):
    """
    scale takes in
        pix, the CURRENT pixel column (or row)
        pixMax, the total # of pixel columns
        floatMin, the min floating-point value
        floatMax, the max floating-point value
    scale returns the floating-point value that
        corresponds to pix
    """
    return (1.0 * pix / pixMax) * (floatMax - floatMin) + floatMin


assert scale(100, 200, -2.0, 1.0) == -0.5  # halfway from -2 to 1
assert scale(100, 200, -1.5, 1.5) == 0.0  # halfway from -1.5 to 1.5
assert scale(100, 300, -2.0, 1.0) == -1.0  # 1/3 of the way from -2 to 1
assert scale(25, 300, -2.0, 1.0) == -1.75
# assert scale(299, 300, -2.0, 1.0) == 0.99  # your exact value may differ slightly


def mset():
    """ creates a 300x200 image of the Mandelbrot set"""

    width = 600
    height = 400
    image = PNGImage(width, height)
    n = 25
    # create a loop in order to draw some pixels

    for col in range(width):
        x = scale(col, width, -2.0, 1.0)
        for row in range(height):
            y = scale(row, height, -1.0, 1.0)
            c = x + y * 1j
            
            if inMSet(c, n) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()


mset()