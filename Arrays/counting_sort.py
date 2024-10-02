"""
Counting Sort Algorithm:
    Create a new array for counting how many there are of the different values.
    Go through the array that needs to be sorted.
    For each value, count it by increasing the counting array at the corresponding index.
    After counting the values, go through the counting array to create the sorted array.
    For each count in the counting array, create the correct number of elements, with values that correspond to the counting array index.
"""

def counting_sort(array: list) -> list:
    count_array = [0] * (max(array) + 1)
    new_array = []

    for val in array:
        count_array[val] += 1

    for idx, val in enumerate(count_array):
        if val != 0:
            new_array += [idx] * val

    return new_array
