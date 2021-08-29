"""practicing relaional operators."""

__author__ = "730395347"

left_hand: int = int(input("Left-hand side: "))
right_hand: int = int(input("Right-hand side: "))

less_than: bool = left_hand < right_hand
at_least: bool = left_hand >= right_hand
equal: bool = left_hand == right_hand
not_equal: bool = left_hand != right_hand

print(str(left_hand) + " < " + str(right_hand) + " is " + str(less_than))
print(str(left_hand) + " >= " + str(right_hand) + " is " + str(at_least))
print(str(left_hand) + " == " + str(right_hand) + " is " + str(equal))
print(str(left_hand) + " != " + str(right_hand) + " is " + str(not_equal))