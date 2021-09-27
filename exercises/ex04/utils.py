"""List utility functions."""

__author__ = "730395347"


# TODO: Implement your functions here.


def all(nums: list[int], match: int) -> bool:
    """Given a list of ints and an int, all should return a bool indicating whether or not all the ints in the list are the same as the given int."""
    i: int = 0
    x: int = 0
    if len(nums) == 0:
        return False
    else:
        while i < len(nums):
            if match == nums[i]:
                i += 1
                x += 1
            else:
                i += 1
        if x == len(nums):
            return True
        else:
            return False


def is_equal(nums: list[int], nums1: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists."""
    i: int = 0
    x: int = 0
    if len(nums) != len(nums1):
        return False
    else:
        while i < len(nums):
            if nums[i] == nums1[i]:
                i += 1
                x += 1
            else:
                i += 1
        if x == len(nums):
            return True
        else:
            return False


def max(nums: list[int]) -> int:
    """Return the largest in the List."""
    if len(nums) == 0:
        raise ValueError("max()arg is an empty List")
    else:
        i: int = nums[0]
        for x in nums:
            if (x > i):
                i = x   
        return i

 