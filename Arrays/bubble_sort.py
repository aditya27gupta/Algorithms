"""
Bubble Sort Algorithm:
    Go through the array, one value at a time.
    For each value, compare the value with the next value.
    If the value is higher than the next one, swap the values so that the highest value comes last.
    Go through the array as many times as there are values in the array.
"""


def bubble_sort(array: list[int]) -> list[int]:
    total_elements: int = len(array)
    for i in range(total_elements - 1):
        for j in range(total_elements - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def bubble_sort_better(array: list[int]) -> list[int]:
    total_elements: int = len(array)
    for i in range(total_elements - 1):
        swapped: bool = False
        for j in range(total_elements - 1 - i):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            break
    return array
