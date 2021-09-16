"""An exercise in remainders and boolean logic."""

__author__ = "730395347"


# Begin your solution here...

num: int = int(input("Enter an int: "))
two: int = num % 2
seven: int = num % 7

if ((seven != 0) & (two != 0)):
    print("CAROLINA")
else:
    if ((seven == 0) & (two == 0)):
        print("TAR HEELS")
    else:
        if (two == 0):
            print("TAR")
        if (seven == 0):
            print("HEELS")   
