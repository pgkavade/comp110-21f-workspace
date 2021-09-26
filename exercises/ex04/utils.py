"""List utility functions."""

__author__ = "730395347"


# TODO: Implement your functions here.


def all(match: int, nums: list[int]) -> bool:
    """Given a list of ints and an int, all should return a bool indicating whether or not all the ints in the list are the same as the given int."""
    i: int = 0
    x: int = 0
    while i < len(nums):
        if match == nums:
            i += 1
            x += 1
        else:
            i += 1
    if x == 3:
        return True
    else:
        return False


def isequal(nums: list[int], nums1: list[int]) -> bool:
    i: int = 0
    x: int = 0
    while i < len(nums):
        if nums[i] == nums1[i]:
            i += 1
            x += 1
        else:
            i += 1
    if x == 3:
        return True
    else:
        return False


def max(nums: list[int]) -> int:
    if len(nums) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        i: int = 0
        x: int = 0
        while i < len(nums):
            if x < nums[i]:
                x == nums[i]
            i += 1
    return i


nums: list[int] = [1, 2, 3]
nums1: list[int] = [1, 2, 3]
match: int = 3
print(all(match, nums))
print(isequal(nums, nums1))
print(max(nums))
