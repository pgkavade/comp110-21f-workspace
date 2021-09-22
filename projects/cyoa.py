
"""Number guessing game!"""

__author__ = "730395347"

from random import randint

levelOneRules: str = "LEVEL 1 asks you to guess an integer between a range of 1 and 5. As you finish the level, you gain 1 point. "
levelTwoRules: str = "LEVEL 2 asks you to guess an integer between a range of 1 and 10. As you finish the level, you gain 5 point. "
levelThreeRules: str = "LEVEL 3 mutliplies your score by a random number. The game ends and this is your final score."
correct: str = ", you guessed correctly! "
player: str = "" 
points: int = 0
smile: str = '\U0001F600'
again: str = '\U0001F914'
total: str = " points in total! "
won: str = " won "
bye: str = ", we are sorry to see you go! "
numPoints: str = "Number of points won in this level: "
incorrect: str = ", you guessed incorrectly! Try again! "
guessFive: str = ", guess a number from 1 to 5 (Press 0 to quit the game.) "
guessTen: str = ", guess a number from 1 to 10 (Press 0 to quit the game.) "
randNum: str = "random number was: "


def main() -> None:
    """Main function, basically starts the game off!"""
    global points
    greet()
    x: int = 0
    while (x != 1):
        pick: int = int(input("Pick a level (Enter 0 to quit the game)! (Enter either 1 or 2) "))
        if (pick == 1):
            levelOne()
        if (pick == 2):
            levelTwo()
        if (pick == 0):
            print(f'{player}{won}{str(points)}{total}')
            x = 1
    pick1: int = int(input("SECRET LEVEL 3: Do you want to see if you can increase your score? (Enter 0 to quit the game)! (Enter either 1 for yes or 2 for no)"))
    if (pick1 == 1):
        increaseScore(points)
    if (pick1 == 2):
        print(f'{player}{won}{str(points)}{total}')
    if (pick1 == 0):
        print(f'{player}{bye}')
        print(f'{player}{won}{str(points)}{total}')


def greet() -> None:
    """Greets the player and establishes a name!"""
    print("Welcome to the number guessing game! ")
    print("~~~~~~~~~THE RULES~~~~~~~~~")
    print("You have three levels")
    print("As the user, you are able to pick the level you want to start at. Level 3 is the last level! ")
    print("")
    print(levelOneRules)
    print("")
    print(levelTwoRules)
    print("")
    print(levelThreeRules)
    print("")
    global player
    player = input("What is your name? ")


def levelOne() -> None:
    """Level one of the game, player can earn up to one point if they guess the number correctly!"""
    global player
    global points
    print("Welcome to Level 1! Here is a refreser on the rules. ")
    print(levelOneRules)
    point1: int = 0
    x: int = 0
    num = randint(1, 5)
    while (x != 1):
        guess: int = int(input(f'{player}{guessFive}'))
        if (guess == num):
            point1 = point1 + 1
            print(f'{player}{correct}')
            print(f'{numPoints}{str(point1)}')
            x = 1
        if (guess == 0):
            print(f'{player}{bye}')
            print(f'{player}{won}{str(points)}{total}{smile}')
        if ((guess != num) & (guess != 0)):
            print(f'{player}{incorrect}{again}')
    points = points + point1
    print(f'{player}{won}{str(points)}{total}{smile}')


def levelTwo() -> None:
    """Level two of the game, player can earn up to five points when they guess the number correctly!"""
    global player
    global points
    print("Welcome to Level 2! Here is a refreser on the rules. ")
    print(levelTwoRules)
    point1: int = 0
    x: int = 0
    num = randint(1, 10)
    while (x != 1):
        guess: int = int(input(f'{player}{guessTen}'))
        if (guess == num):
            point1 = point1 + 5
            print(f'{player}{correct}')
            print(f'{numPoints}{str(point1)}')
            x = 1
        if (guess == 0):
            print(f'{player}{bye}')
            print(f'{player}{won}{str(points)}{total}{smile}')
        if ((guess != num) & (guess != 0)):
            print(f'{player}{incorrect}{again}')
    points = points + point1
    print(f'{player}{won}{str(points)}{total}{smile}')


def increaseScore(points: int) -> int:
    """Seceret level 3, player can multiply thier score by a number ranging from 1 to 1000!"""
    global player
    print("Welcome to Level 3! ")
    print(levelThreeRules)
    pick: int = int(input("To randomly generate a number, enter 1. To quit the game, enter 0! "))
    if (pick == 1):
        num = randint(1, 1000)
        print(f'{randNum}{str(num)}')
        points = points * num 
        print(f'{player}{won}{str(points)}{total}{smile}')
    if (pick == 0):
        print(f'{player}{bye}')
        print(f'{player}{won}{str(points)}{total}{smile}')
    return(points)


if __name__ == "__main__":
    main()
