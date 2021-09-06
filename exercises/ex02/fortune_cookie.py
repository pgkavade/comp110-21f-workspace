"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730395347"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

# Begin your solution here...

num: int = (randint(1, 4))

print("Your fortune cookie says...")

if num == 1:
    print("You will reach your goals!")
else:
    if num == 2:
        print("You will get good grades!")
    else:
        if num == 3:
            print("Everything will work out in the end!")
        else:
            print("You will have a great life!")

print("Now, go spread positive vibes!")
