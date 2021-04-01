"""
Created on 4/1/21
@author:   Avery Cunningham
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 8
"""
# Demo of hmmm, the Harvey Mudd miniature machine
# D.Naumann 2015, rev Oct 2018

# When this file is loaded, it runs the program assigned
# to variable RunThis. Debug mode is controlled by 
# variable Mode. Read all the comments before trying it out.
# Remember to press F5 to run, after making changes.  

import sys
import importlib
# Also requires hmmmAssembler.py and hmmmSimulator.py to
# be available in the same directory as this file.


fibonacci = """
00 read r1 # read n from user
01 jeqzn r1 10 # halt the program if n = 0
02 setn r2 0 # set the first value in the sequence
03 setn r3 1 # set the second value in the sequence
04 write r2 # print the values in the sequence
05 copy r4 r3 # add another register to help with addition
06 add r3 r2 r3 # calculate the next value in the sequence
07 copy r2 r4 # assign the previous 2nd value in the sequence to the 1st position
08 addn r1 -1 # decrement the counter by 1
09 jgtzn r1 04 # jump to line 4 if the counter is greater than 0
10 halt # stop program execution
"""


# Set this variable to whichever program you want to execute
# when this file is loaded.
RunThis = fibonacci

# Choose whether to use debug mode; uncomment one of the following lines.
Mode = ['-n'] # not debug mode, 
# Mode = ['-d'] # debug mode
#Mode = []     # prompt for whether to enter debug mode


# When you press F5 in IDLE, the following code will
# load the assembler and simulator, then run them.
# You can interrupt with Ctrl-C; then re-start Python.

if __name__ == "__main__" : 
    import hmmmAssembler ; importlib.reload(hmmmAssembler)
    import hmmmSimulator ; importlib.reload(hmmmSimulator)
    hmmmAssembler.main(RunThis) # assemble input into machine code file out.b
    hmmmSimulator.main(Mode)    # run the machine code in out.b
