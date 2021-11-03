"""List utility functions part 2."""

__author__ = "730395347"

# Define your functions below


def only_evens(list1: list[int]):
    """Return a list containing only the elements of the input list that were even."""
    list2: list[int] = []
    i: int = 0
    if len(list1) == 0:
        return list2
    else:
        while i < (len(list1)):
            if (list1[i] % 2) == 0:
                list2.append(list1[i])
                i += 1
            else:
                i += 1
        return list2


def sub(list1: list[int], x: int, y: int):
    """Generates a List which is a subset of the given list, between the specified start index and the end index - 1."""
    list2: list[int] = []
    item: int = x
    
    if len(list1) == 0:
        return list2
    if x > len(list1):
        return list2
    if y < 0:
        return list2
    if y > len(list1):
        item: int = 0
    if x < 0:
        item: int = 0
    else:
        for item in list1:
            if x < y:
                list2.append(list1[x])
                x += 1
        return list2


def concat(list1: list[int], list2: list[int]):
    """Generates a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    list3: list[int] = []
    if len(list1) == 0 | len(list2) == 0:
        return list3
    if len(list2) == 0 | len(list1) == 0:
        return list3
    else:
        list3 = list1 + list2
        return list3 
