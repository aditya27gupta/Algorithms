from typing import List


def linear_search(arr: List, find_value: int):
    if len(arr) < 1:
        return None

    for idx, elem in enumerate(arr):
        if elem == find_value:
            return idx

    return None
