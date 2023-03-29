import sys
import csv

def merge_sort(inputArray, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(inputArray, p, q)
        merge_sort(inputArray, q + 1, r)
        merge(inputArray, p, q, r)
    return inputArray

def merge(inputArray, p, q, r):
    n_one = q - p + 1
    n_two = r - q
    L = [0] * n_one
    R = [0] * n_two
    for i in range(n_one):
        L[i] = inputArray[p + i]
    for j in range(n_two):
        R[j] = inputArray[q + j + 1]
    L.append(10**1000) 
    # sentinels
    R.append(10**1000)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            inputArray[k] = L[i]
            i += 1
        else:
            inputArray[k] = R[j]
            j += 1
    return inputArray

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            inputArray = [int(x) for x in row if x.isdigit()]
            print(merge_sort(inputArray, 0, len(inputArray) - 1))
            
        else:
            print("error")
