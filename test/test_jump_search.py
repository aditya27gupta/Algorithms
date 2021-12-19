import pytest
from Searching.jump_search import jump_search


test_data = [
    ([], 1, None),
    ([1, 2, 4, 5, 7], 4, 2),
    ([None, 1, 2, 5, 6, 7, 3], 2, 2),
    ([None], 1, None)
]


@pytest.mark.parametrize("arr, find_val, expected", test_data)
def test_jump_search(arr, find_val, expected):
    assert jump_search(arr, find_val) == expected
