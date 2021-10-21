"""Practice with dictionaries."""

__author__ = "730395347"

# Define your functions below


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values."""
    dict2: dict[str, str] = {}
    condition: bool = False
    x: int = 0
    for key in dict1:
        for count in dict1:
            if(dict1[key] == dict1[count]):
                x = x + 1
                if x > 1:
                    condition = True
        count = 0
        x = 0
    if condition is True:
        raise KeyError("Repeated key values")
    if condition is False:
        dict2 = {value: key for key, value in dict1.items()}
        return dict2


def favorite_color(dict1: dict[str, str]) -> str:
    """Returns a str which is the color that appears most frequently."""
    dict2 = list(dict1.values())
    return(max(set(dict2), key=dict2.count))


def count(list1: list[str]) -> dict[str, int]:
    """Dictionary where each value associated is the count of the number of times that value appeared in the input list."""
    dict1 = {}
    for i in list1:
        dict1[i] = count.get(i, 0) + 1
    return dict1
