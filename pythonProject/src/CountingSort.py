# Luke Hill's Counting Sort Algorithm

# pre: take in list
# post: return max of list
def findmax(arr: list) -> int:
    maximum = 0
    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum

# pre: take in an integer
# post: return empty list of size integer
def initializelist(ind: int) -> list:
    fill = 0
    arr = []
    for i in range(ind+1):
        arr.append(fill)
    return arr

# pre: take in unsorted list
# post: return
def countsort(arr: list) -> list:
    m = findmax(arr)
    countArray = initializelist(arr)
    # count the number of occurences of each number at respective index

    # temp return
    return arr

print(countsort([1, 4 , 6 ,9]))
