# written by Jack Keys

import statistics
import copy
import MeasureExectution


# pre  -- takes a list
# post -- sorts and returns the list
def quick_sort(lst: list) -> list:

    if len(lst) <= 1:                  # base case: list has less than 2 elements in it
        return lst

    pivot = select_pivot(lst)          # select a pivot
    lst_no_pivot = copy.deepcopy(lst)  # create deep copy of lst and set it to lst_no_pivot
    lst_no_pivot.remove(pivot)         # remove pivot from lst_no_pivot
    left = []                          # list for holding values less than pivot
    right = []                         # list for holding values greater than pivot

    for number in lst_no_pivot:

        if number <= pivot:            # if number is less than the pivot
            left.append(number)
        else:                          # if number is greater than the pivot
            right.append(number)

    return quick_sort(left) + [pivot] + quick_sort(right)  # recursive call


# pre  -- takes a list
# post -- returns the median between the first, the last,
#         and the middle element of the list (median of three)
def select_pivot(lst: list) -> int:
    possible_pivots = [lst[1], lst[len(lst) // 2], lst[-1]]
    return statistics.median(possible_pivots)