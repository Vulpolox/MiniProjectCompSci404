import CountingSort
import QuickSort
import random
def merge(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    arr = [0] * (n1 + n2)

    i = 0
    j = 0
    k = 0

    #create array comparing elements of arr1 and arr2
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    #copy remaining elements
    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1

    return arr

def split(arr):
    size = len(arr)
    m = int(size / 2)
    return arr[:m], arr[m:]

def stupidSplit(arr):
    size = len(arr)
    m = int(size - 5)
    return arr[:m], arr[m:]

def selectionSort(arr):
    size = len(arr)
    for i in range(size):
        min = i
        for j in range(i + 1, size):
            if arr[j] < arr[min]:
                min = j
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp

    return arr

def bogoSort(arr):
    def isSorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                return False
        return True

    def shuffle(arr):
        n = len(arr)
        for i in range(0,n):
            r = random.randint(0, n - 1)
            arr[i], arr[r] = arr[r], arr[i]

    n = len(arr)
    while (isSorted(arr) == False):
        shuffle(arr)

    return arr

def GharibiSort(arr):
    arrT1, arrT2 = split(arr)
    arr1, arr2 = split(arrT1)
    arr3, arr4 = split(arrT2)
    arr5, arr6 = stupidSplit(arr4)

    arrA = CountingSort.count_sort(arr1)
    arrB = QuickSort.quick_sort(arr2)
    arrR = selectionSort(arr3)
    arrZ = QuickSort.quick_sort(arr5)
    arrL = bogoSort(arr6)
    arrC1 = merge(arrA, arrB)
    arrC2 = merge(arrR, arrZ)
    arrC3 = merge(arrL, arrC1)
    arrC3 = merge(arrC3, arrC2)

    return arrC3

# driver code

#arr = [3838, 328, 34, 29, 8, 238, 57, 9349, 6, 54, 15, 28, 345, 298]
#print("Unsorted array: ", arr)
#arr = GharibiSort(arr)

#arr1 = [5, 9, 23, 67, 238, 250, 694]
#arr2 = [3, 82, 2398, 3009]

#arr = merge(arr1, arr2)

#print("Sorted array: ", arr)

