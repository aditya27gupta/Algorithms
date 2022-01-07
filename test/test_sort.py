import pytest
from Sorting.bubble_sort import bubble_sort
from Sorting.insertion_sort import insertion_sort

test_data = [
    ([1, 2], [1, 2]),
    ([2, 1], [1, 2]),
    ([7, 8, 2, 5, 1, 5, 6, 1, 5, 8, 2, 4], [1, 1, 2, 2, 4, 5, 5, 5, 6, 7, 8, 8])
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_sort(arr, expected):
    assert bubble_sort(arr) == expected
    assert insertion_sort(arr) == expected
