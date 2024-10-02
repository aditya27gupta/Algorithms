"""
Insertion Sort Algorithm:
    Take the first value from the unsorted part of the array.
    Move the value into the correct place in the sorted part of the array.
    Go through the unsorted part of the array again as many times as there are values.
"""


def insertion_sort(array: list[int]) -> list[int]:
    total_elements: int = len(array)
    for i in range(1, total_elements):
        insert_index = i
        current_value = array.pop(i)
        for j in range(i - 1, -1, -1):
            if array[j] > current_value:
                insert_index = j
        array.insert(insert_index, current_value)
    return array


def insertion_sort_better(array: list[int]) -> list[int]:
    total_elements: int = len(array)
    for i in range(1, total_elements):
        insert_index = i
        current_value = array[i]
        for j in range(i - 1, -1, -1):
            if array[j] > current_value:
                array[j + 1] = array[j]
                insert_index = j
            else:
                break
        array[insert_index] = current_value
    return array
