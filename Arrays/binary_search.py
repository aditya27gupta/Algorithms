"""
Binary Search Algorithm:
    Check the value in the center of the array.
    If the target value is lower, search the left half of the array. If the target value is higher, search the right half.
    Continue step 1 and 2 for the new reduced part of the array until the target value is found or until the search area is empty.
    If the value is found, return the target value index. If the target value is not found, return -1.
"""


def binary_search(
    array: list[int], element_to_find: int, low: int = 0, high: int | None = None
) -> int:

    if high is None:
        high = len(array)

    if low < high:
        mid = (low + high) // 2
        if element_to_find == array[mid]:
            return mid
        elif element_to_find < array[mid]:
            high = mid
        else:
            low = mid + 1

        return binary_search(array, element_to_find, low, high)

    return -1
