from typing import List


def binary_search(arr: List, find_value: int):

    if len(arr) < 1:
        return None

    first, last = 0, len(arr) - 1

    while 0 <= first <= last < len(arr):
        print(first, last)

        mid = (first + last) // 2

        if arr[mid] == find_value:
            return mid

        elif arr[mid] < find_value:
            first = mid + 1

        elif arr[mid] > find_value:
            last = mid + 1

        print(first, last)

    return None
