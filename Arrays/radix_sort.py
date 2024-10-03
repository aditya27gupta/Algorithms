"""
Radix Sort Algorithm:
    An array with non negative integers that needs to be sorted.
    A two dimensional array with index 0 to 9 to hold values with the current radix in focus.
    A loop that takes values from the unsorted array and places them in the correct position in the two dimensional radix array.
    A loop that puts values back into the initial array from the radix array.
    An outer loop that runs as many times as there are digits in the highest value.
"""


def radix_sort(array: list[int]) -> list[int]:
    max_len: int = max([len(str(num)) for num in array])
    divider: int = 1

    for i in range(max_len):
        radixArray: list[list[int]] = [[] for _ in range(10)]
        while array:
            val = array.pop(0)
            index = (val // divider) % 10
            radixArray[index].append(val)
        for radi in radixArray:
            array += radi
        divider *= 10

    return array


myArray = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(myArray)
