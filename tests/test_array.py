import random
from Arrays.bubble_sort import bubble_sort, bubble_sort_better
from Arrays.selection_sort import selection_sort, selection_sort_better
from Arrays.insertion_sort import insertion_sort, insertion_sort_better


NUM_EXPERIMENTS = 10
ARRAY_SIZE = 200
sort_functions = [
    bubble_sort, bubble_sort_better, selection_sort, selection_sort_better,
    insertion_sort, insertion_sort_better
]


def test_sort() -> None:
    for func in sort_functions:
        for _ in range(NUM_EXPERIMENTS):
            array = [random.randint(1, ARRAY_SIZE * 2) for _ in range(ARRAY_SIZE)]
            sorted_array = func(array=array)
            assert sorted(array) == sorted_array
