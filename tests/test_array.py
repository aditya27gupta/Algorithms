import random
from typing import List, Callable
from Arrays.bubble_sort import bubble_sort, bubble_sort_better
from Arrays.selection_sort import selection_sort, selection_sort_better
from Arrays.insertion_sort import insertion_sort, insertion_sort_better
from Arrays.quick_sort import quick_sort
from Arrays.counting_sort import counting_sort
from Arrays.radix_sort import radix_sort
from Arrays.merge_sort import merge_sort
from Arrays.linear_search import linear_search
from Arrays.binary_search import binary_search


NUM_EXPERIMENTS = 10
ARRAY_SIZE = 10
sort_functions: List[Callable[[list[int]], list[int]]] = [
    bubble_sort,
    bubble_sort_better,
    selection_sort,
    selection_sort_better,
    insertion_sort,
    insertion_sort_better,
    quick_sort,
    radix_sort,
    merge_sort,
]

search_functions: List[Callable[[list[int], int], int]] = [linear_search, binary_search]


def test_sort() -> None:
    for func in sort_functions:
        for _ in range(NUM_EXPERIMENTS):
            array = [random.randint(1, ARRAY_SIZE * 2) for _ in range(ARRAY_SIZE)]
            sorted_array = func(array)
            assert sorted(array) == sorted_array


def test_search() -> None:
    for func in search_functions:
        for _ in range(NUM_EXPERIMENTS):
            array = sorted(
                [random.randint(1, ARRAY_SIZE * 2) for _ in range(ARRAY_SIZE)]
            )
            element_to_find = random.randint(1, ARRAY_SIZE * 2)
            idx = func(array, element_to_find)
            correct_idx = (
                array.index(element_to_find) if element_to_find in array else -1
            )
            assert idx == correct_idx
