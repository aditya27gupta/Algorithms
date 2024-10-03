"""
Merge Sort Algorithm:
    Divide the unsorted array into two sub-arrays, half the size of the original.
    Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
    Merge two sub-arrays together by always putting the lowest value first.
    Keep merging until there are no sub-arrays left.
"""


def merge_sort(array: list[int]) -> list[int]:
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    sortedLeft = merge_sort(left)
    sortedRight = merge_sort(right)
    return merge_array(sortedLeft, sortedRight)


def merge_array(left: list[int], right: list[int]) -> list[int]:
    new_array = []
    idx1 = idx2 = 0

    while idx1 < len(left) and idx2 < len(right):
        if left[idx1] < right[idx2]:
            new_array.append(left[idx1])
            idx1 += 1
        else:
            new_array.append(right[idx2])
            idx2 += 1

    new_array += left[idx1:]
    new_array += right[idx2:]
    return new_array
