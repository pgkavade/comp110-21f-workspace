"""practicing the numeric operators, type conversions, and string concatenation"""

__author__ = "730395347"

left_hand: int = int(input("Left-hand side: "))
right_hand: int = int(input("Right-hand side: "))

exponent: int = left_hand ** right_hand
divison: float = (left_hand / right_hand)
integer_division: int = (left_hand // right_hand)
remainder: int = (left_hand % right_hand)

print(str(left_hand) + " ** " + str(right_hand) + " is " + str(exponent))
print(str(left_hand) + " / " + str(right_hand) + " is " + str(divison))
print(str(left_hand) + " // " + str(right_hand) + " is " + str(integer_division))
print(str(left_hand) + " % " + str(right_hand) + " is " + str(remainder))