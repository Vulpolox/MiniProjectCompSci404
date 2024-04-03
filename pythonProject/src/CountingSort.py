# Luke Hill's Counting Sort Algorithm

def findmax(arr: list) -> list:
    maximum = 0
    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum

def initializelist(ind: int) -> list:
    fill = 0
    arr = []
    for i in range(ind):
        arr.append(fill)
    return arr

print(findmax([1, 4 , 6 ,9]))