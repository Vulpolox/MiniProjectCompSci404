# written by Jack Keys

import statistics

# pre  -- takes a list
# post -- sorts and returns the list
def quickSort(lst: list) -> list:

    if len(lst <= 1):        # base case: list has less than 2 elements in it
        return lst

    pivot = selectPivot(lst) # select a pivot
    lstNoPivot = lst.remove(pivot)
    left = []
    right = []

    for number in lstNoPivot:
        pass




# pre  -- takes a list
# post -- returns the median between the first, the last,
#         and the middle element of the list (median of three)
def selectPivot(lst: list) -> int:
    possiblePivots = [lst[1], lst[len(lst) // 2], lst[-1]]
    return statistics.median(possiblePivots)