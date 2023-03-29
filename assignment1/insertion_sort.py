
# insertion sort O(n^2)
# merge sort O(nlogn)
#Bubble sort O(n^2)
import csv
import sys

def insertion_sort(inputArray):
    for j in range(1, len(inputArray)):
        key = inputArray[j]
        # print(key)
        i = j-1
        while i >= 0 and inputArray[i] > key :
                inputArray[i + 1] = inputArray[i]
                i = i- 1
        inputArray[i + 1] = key
    return inputArray

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            inputArray = [int(x) for x in row if x.isdigit()]
            print(i)
            print(insertion_sort(inputArray))
        else:
            print("error")
