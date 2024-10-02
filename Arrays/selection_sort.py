"""
Selection Sort Algorithm:
    An array with values to sort.
    An inner loop that goes through the array, finds the lowest value, and moves it to the front of the array. This loop must loop through one less value each time it runs.
    An outer loop that controls how many times the inner loop must run. For an array with n
    values, this outer loop must run n−1 times.
"""

def selection_sort(array: list) -> list:
    total_elements: int = len(array)
    for i in range(total_elements - 1):
        minIndex = i
        for j in range(i+1, total_elements):
            if array[j] < array[minIndex]:
                minIndex = j
        minval = array.pop(minIndex)
        array.insert(i, minval)
    return array

def selection_sort_better(array: list) -> list:
    total_elements: int = len(array)
    for i in range(total_elements - 1):
        minIndex = i
        for j in range(i+1, total_elements):
            if array[j] < array[minIndex]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    return array


array = [1, 4, 9, 2, 8, 3, 0]
print(selection_sort(array=array))
print(selection_sort_better(array=array))
