"""Finding duplicate letters in a word."""

__author__ = "730395347"

word: str = input("Enter a word: ")

num: int = 0
count: int = 0
x: int = 0
condition: bool = False

while (num < len(word)):
    while (count < len(word)):
        if(word[num] == word[count]):
            x = x + 1
            if x > 1:
                condition = True
        count = count + 1
    count = 0
    x = 0
    num = num + 1
if condition is True:
    print("Found duplicate: True")
if condition is False:
    print("Found duplicate: False")
