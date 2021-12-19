from typing import List


def interpolation_search(arr: List, find_value: int):

    if len(arr) < 1:
        return None

    first, last = 0, len(arr) - 1

    while 0 <= first < last < len(arr):

        pos = int(first + ((find_value - arr[first]) * (last - first) / (arr[last] - arr[first])))

        if len(arr) <= pos:
            return None

        elif arr[pos] == find_value:
            return pos

        elif arr[pos] < find_value:
            first = pos + 1

        elif arr[pos] > find_value:
            last = pos - 1

    return None
