"""
Linear Search Algorithm:
    Go through the array value by value from the start.
    Compare each value to check if it is equal to the value we are looking for.
    If the value is found, return the index of that value.
    If the end of the array is reached and the value is not found, return -1 to indicate that the value was not found.
"""


def linear_search(array: list[int], element_to_find: int) -> int:

    for idx, element in enumerate(array):
        if element == element_to_find:
            return idx

    return -1
