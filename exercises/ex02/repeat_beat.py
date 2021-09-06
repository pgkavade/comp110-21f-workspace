"""Repeating a beat in a loop."""

__author__ = "730395347"


# Begin your solution here...

beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
i: int = 0
concat: str = beat

if repeat > 0:
    while (i < (repeat - 1)):
        i = i + 1
        concat += " " + beat
    print(concat)
else:
    print("No beat. . .")
