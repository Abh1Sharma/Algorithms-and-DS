#Bubble sort O(n^2)
# insertion sort O(n^2)
# merge sort O(nlogn)

import sys
import csv
import time

def bubble_sort(inputArray):
    
    checkFlag = True
    arrSize = len(inputArray)
    for i in range arrSize:
        checkFlag = 0
        for j in range(0,arrSize-1-i):
            if inputArray[j] > inputArray[j+1]:
                temp = inputArray[j+1]
                inputArray[j+1] = inputArray[j]
                inputArray[j] = temp
                checkFlag = 1
        if checkFlag == 0:
            break
    
     
    return inputArray



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



if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        st = time.time()
        for row in csvreader:
            
            inputArray = [int(x) for x in row if x.isdigit()]
            if inputArray:
                sortedArray = bubble_sort(inputArray)
                # print(sortedArray)
            
            else:
                print("error")
        en = time.time()
        print(en - st)
            
