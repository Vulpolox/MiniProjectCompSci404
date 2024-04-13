import random
import time

random.seed(time.time())


# pre  -- takes a list
# post -- randomly picks an element from the list
#         and compares with rest of list to see if it is min;
#         if it is min, returns the index
def bogo_find_min(lst: list) -> int:

    while True:

        random_index = random.randint(0, len(lst) - 1)
        random_pick = lst[random_index]

        if random_pick == min(lst):
            return lst.index(random_pick)
        else:
            continue


# pre  -- takes a list and two integer indices
# post -- swaps the elements in the specified list at the specified indices
def swap(lst: list, i: int, j: int) -> None:
    lst[i], lst[j] = lst[j], lst[i]


def bogo_selection_sort(lst: list) -> None:
    for i in range(len(lst)-1):
        for j in range((i+1), len(lst)):
            pertinent_lst = lst[(i+1):]
            min_index = bogo_find_min(pertinent_lst) + i
            print(pertinent_lst)
            if lst[i] > lst[min_index]:
                swap(lst, i, min_index)


test_lst = [3, 2 ,1]
bogo_selection_sort(test_lst)
print(test_lst)