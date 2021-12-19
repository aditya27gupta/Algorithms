import pytest
from Searching.linear_search import linear_search


test_data = [
    ([], 1, None),
    ([4, 1, 5, 7, 2], 1, 1),
    ([None, 1, 6, 2, 5, 7, 3], 2, 3),
    ([None], 1, None)
]


@pytest.mark.parametrize("arr, find_val, expected", test_data)
def test_linear_search(arr, find_val, expected):
    assert linear_search(arr, find_val) == expected
