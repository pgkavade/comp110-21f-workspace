"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730395347"


def test_check_evens() -> None:
    """Returns even number in list."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_empty_list() -> None:
    """Returns empty list if list is empty."""
    xs: list[int] = []
    assert only_evens(xs) == []
    assert sub(xs, 1, 2) == []
    assert concat(xs, xs) == []


def test_concat_numbers() -> None:
    """Concats the numbers together."""
    xs: list[int] = [1, 2, 3]
    assert concat(xs, xs) == [1, 2, 3, 1, 2, 3]


def test_sub() -> None:
    """Test to see if the sub function works."""
    xs: list[int] = [1, 2, 3]
    assert sub(xs, 0, 1) == [1]


def test_check_evens_multiple() -> None:
    """Checks to see if only_evens can return multiple even numbers in a list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(xs) == [2, 4]


def test_concat_many_numbers() -> None:
    """Concats the numbers together with lists of different lengths."""
    xs: list[int] = [1, 2, 3]
    list1: list[int] = [1, 2, 3, 4, 5]
    assert concat(xs, list1) == [1, 2, 3, 1, 2, 3, 4, 5]


def test_sub_negative() -> None:
    """Test to see if the sub function works with negative numbers."""
    xs: list[int] = [1, 2, 3]
    assert sub(xs, -1, 1) == []
