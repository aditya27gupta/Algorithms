import pytest
from Searching.binary_search import binary_search
from Searching.interpolation_search import interpolation_search
from Searching.jump_search import jump_search
from Searching.linear_search import linear_search


test_data = [
    ([], 1, None),
    ([1, 2, 4, 5, 7], 4, 2),
    ([1, 2, 5, 6, 7], 2, 1),
    ([1, 3], 2, None),
    ([1, 2], 1, 0),
    ([1, 2], 2, 1)
]


@pytest.mark.parametrize("arr, find_val, expected", test_data)
def test_search(arr, find_val, expected):
    assert binary_search(arr, find_val) == expected
    assert interpolation_search(arr, find_val) == expected
    assert jump_search(arr, find_val) == expected
    assert linear_search(arr, find_val) == expected
