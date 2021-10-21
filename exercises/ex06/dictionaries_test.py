"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730395347"

from exercises.ex06.dictionaries import invert, favorite_color, count


def test_check_invert() -> None:
    """Returns dictionary with inverted key and values."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_one_value() -> None:
    """Check to see if the invert functions works with one key and value."""
    assert invert({'a': 'z'}) == {'z': 'a'}


def test_color() -> None:
    """Checks to see if fav color works with only one key and value."""
    assert favorite_color({"Marc": "yellow"}) == "yellow"


def test_empty_list() -> None:
    """Returns empty dictionary if list is empty."""
    xs: list[str] = []
    assert count(xs) == {}


def test_check_color() -> None:
    """Checks to see if favorite_color works."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_check_count() -> None:
    """Checks to see if the count function works."""
    assert count(["a", "a", "a", "a", "b", "b", "c", "b", "c"]) == {'a': 4, 'b': 3, 'c': 2}


def test_check_same_count() -> None:
    """Checks to see if the count function works when numerous values have the same count."""
    assert count(["a", "a", "a", "c", "b", "b", "c", "b", "c"]) == {'a': 3, 'b': 3, 'c': 3}


def test_check_same_color() -> None:
    """Checks to see if favorite_color works when two colors have the same frequency."""
    assert favorite_color({"Marc": "yellow", "Ezri": "yellow", "Kris": "blue", "Preethi": "blue"}) == "yellow"


def test_two_invert() -> None:
    """Check to see if the invert functions works with two keys and values."""
    assert invert({'a': 'z', 'c': 'd'}) == {'z': 'a', 'd': 'c'}


    
