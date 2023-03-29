import csv
import time

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def measureInsertionSortTime(arrays):
    for arr in arrays:
        start_time = time.time()
        sorted_array = insertionSort(arr)
        end_time = time.time()
        print(f"Array of size {len(arr)} sorted in {end_time - start_time} seconds")

arrays = [
    list(range(10000, -1, -1)), # Worst case scenario
    [1, 2, 3, 4, 5], # Best case scenario
    [3, 1, 4, 2, 5], # Average case scenario
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], # Increasing size
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], # Decreasing size
]

measureInsertionSortTime(arrays)
