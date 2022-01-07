from typing import List


def bubble_sort(arr: List) -> List:
    i = 0
    while i < len(arr) - 1:
        change = False
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                change = True
                arr[j], arr[j+1] = arr[j+1], arr[j]

        if not change:
            break

    return arr
