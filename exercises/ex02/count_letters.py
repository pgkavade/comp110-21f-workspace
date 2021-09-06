"""Counting letters in a string."""

__author__ = "730395347"


# Begin your solution here...

letter: str = input("What letter do you want to seach for?: ")
word: str = input("Enter a word: ")
num: int = 0
find: str = word[num]
count: int = 0

while (num < len(word)):
    if(letter == word[num]):
        count = count + 1
    num = num + 1
print("Count: " + str(count))