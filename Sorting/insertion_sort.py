from typing import List


def insertion_sort(arr: List) -> List:

    for i in range(1, len(arr)):

        j = 0
        while j < i:
            if arr[j] > arr[i]:
                elem = arr.pop(i)
                arr.insert(j, elem)
                break
            j += 1

    return arr
