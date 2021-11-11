"""Utility functions."""

__author__ = "730395347"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], row: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first `N` rows of data for each column."""
    result: dict[str, list[str]] = {}
    
    for column in column_table:
        values: list[str] = []
        value: int = 0
        while value < row:
            values.append(column_table[column][value])
            value = value + 1
        result[column] = values
    return result


def select(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}

    for value in names:
        result[value] = column_table[value]

    return result 


def concat(column_table: dict[str, list[str]], column_table1: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}

    for column in column_table:
        result[column] = column_table[column]
    
    for column in column_table1:
        if column in result:
            for value in column_table1[column]:
                result[column].append(value)
        else:
            result[column] = column_table1[column]

    return result 


def count(values: list[str]) -> dict[str, int]:
    """Produce a dict where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    result: dict[str, int] = {} 

    for value in values:
        if value in result:
            result[value] = result[value] + 1 
        else:
            result[value] = 1
    
    return result 