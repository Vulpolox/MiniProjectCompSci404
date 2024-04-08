# Luke Hill's Counting Sort Algorithm
import MeasureExectution
import time

# counting sort functions [call countsort(list) for sorted]:
# ------------------------------------------------------------
# pre: take in list
# post: return max of list
def find_max(lst: list) -> int:
    maximum = 0

    # for size of list, if larger find max
    for i in range(len(lst)):
        if lst[i] > maximum:
            maximum = lst[i]

    return maximum

# pre: take in an integer
# post: return empty list of size integer
def initialize_list(ind: int) -> list:
    lst = []

    # for given size (max in count sort), create lst of proper size
    for i in range(ind+1):
        lst.append(0)

    return lst

# pre: take in unsorted list
# post: return sorted list
def count_sort(lst: list) -> list:
    m = find_max(lst)  # max element in list
    count_lst = initialize_list(m)  # create lst of size max+1, filled with zeroes

    # add 1 to every corresponding index to a number
    for num in lst:
        count_lst[num] += 1

    # from 1 to max+1, update cumulative sum across all elements (last will be size of original list)
    for i in range(1, m + 1):
        count_lst[i] += count_lst[i - 1]

    sorted_lst = [0] * len(lst)  # initialize output list

    # for the elements of original list, use cumulative count to place elements into sorted list in the correct spot
    # countlst is decremented to keep track of what we've placed so far
    for num in lst:
        sorted_lst[count_lst[num] - 1] = num
        count_lst[num] -= 1

    return sorted_lst

MeasureExectution.measureexecution(count_sort)

