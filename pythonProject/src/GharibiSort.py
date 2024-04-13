
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
    arr1, arr2 = split(arr)
    arrL = bogoSort(arr1)
    #print("bogo: ", arrL)
    arrR = selectionSort(arr2)
    #print("selection: ", arrR)
    arrC = merge(arrL, arrR)

    return arrC

# driver code

arr = [3838, 328, 34, 29, 8, 238, 57, 9349, 6, 54, 15, 28, 345, 298]
print("Unsorted array: ", arr)
arr = GharibiSort(arr)

#arr1 = [5, 9, 23, 67, 238, 250, 694]
#arr2 = [3, 82, 2398, 3009]

#arr = merge(arr1, arr2)

print("Sorted array: ", arr)

