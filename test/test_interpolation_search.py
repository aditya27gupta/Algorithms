import pytest
from Searching.interpolation_search import interpolation_search


test_data = [
    ([], 1, None),
    ([1, 2, 4, 5, 7], 4, 2),
    ([1, 2, 5, 6, 7, 3], 2, 1),
    ([1, 3], 2, None),
    ([1, 2], 1, 0),
    ([1, 2], 2, 1)
]


@pytest.mark.parametrize("arr, find_val, expected", test_data)
def test_jump_search(arr, find_val, expected):
    assert interpolation_search(arr, find_val) == expected
