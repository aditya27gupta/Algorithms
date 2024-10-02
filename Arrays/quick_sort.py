"""
Quick Sort Algorithm:
    Choose a value in the array to be the pivot element.
    Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
    Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
    Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.
"""

def pivot_element(array: list, high: int, low: int) -> int:
    pivot_value = array[high]
    pivot_index = low - 1
    
    for i in range(low, high):
        if array[i] < pivot_value:
            pivot_index += 1
            array[pivot_index], array[i] = array[i], array[pivot_index]
            
    array[pivot_index+1], array[high] = array[high], array[pivot_index + 1]
    return pivot_index + 1


def quick_sort(array: list, high: int = None, low: int = 0) -> list:
    if high is None:
        print(array)
        high = len(array) - 1
    if high > low:
        pivot_index = pivot_element(array=array, high=high, low=low)
        quick_sort(array=array, high=pivot_index-1, low=low)
        quick_sort(array=array, high=high, low=pivot_index+1)
    return array
