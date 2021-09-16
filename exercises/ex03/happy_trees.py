"""Drawing forests in a loop."""

__author__ = "730395347"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

word: int = int(input("Depth: "))

x: int = 0
concat: str = TREE 

while (x < int(word)):
    print(concat)
    concat += "" + TREE
    x = x + 1