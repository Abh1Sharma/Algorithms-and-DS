import time

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]
        mergeSort(left_half)
        mergeSort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Generate worst-case input array with size n
def generate_worst_case_array(n):
    arr = [i for i in range(n, 0, -1)]
    return arr

# Measure time for sorting the worst-case input array with size n
def measure_time_for_worst_case(n):
    arr = generate_worst_case_array(n)
    start_time = time.time()
    sorted_arr = mergeSort(arr)
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken

# Example usage
n = 1
time_taken = measure_time_for_worst_case(n)
print("Time taken for sorting an array with size", n, "in worst-case scenario:", time_taken, "seconds")


def short_bubble_sort(inputArray):
    swap = True
    n = len(inputArray)
    while swap:
        swap = False
        for i in range(n - 1):
            if inputArray[i] > inputArray[i + 1]:
                inputArray[i], inputArray[i + 1] = inputArray[i + 1], inputArray[i]
                swap = True
        n -= 1
    return inputArray
