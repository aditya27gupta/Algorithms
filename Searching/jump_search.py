from typing import List
from Searching.linear_search import  linear_search


def jump_search(arr: List, find_value: int):

    if len(arr) < 1:
        return None

    steps = int(len(arr) ** 0.5)
    i = 0

    while i < len(arr):
        if arr[i] == find_value:
            return i
        elif arr[i] > find_value:
            return linear_search(arr[i-steps: i], find_value)
        i += steps

    return None
