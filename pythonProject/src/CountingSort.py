# Luke Hill's Counting Sort Algorithm
import ListGenerator
import time

# counting sort functions [call countsort(list) for sorted]:
# ------------------------------------------------------------
# pre: take in list
# post: return max of list
def findmax(lst: list) -> int:
    maximum = 0

    # for size of list, if larger find max
    for i in range(len(lst)):
        if lst[i] > maximum:
            maximum = lst[i]

    return maximum

# pre: take in an integer
# post: return empty list of size integer
def initializelist(ind: int) -> list:
    lst = []

    # for given size (max in count sort), create lst of proper size
    for i in range(ind+1):
        lst.append(0)

    return lst

# pre: take in unsorted list
# post: return sorted list
def countsort(lst: list) -> list:
    m = findmax(lst)  # max element in list
    countlst = initializelist(m)  # create lst of size max+1, filled with zeroes

    # add 1 to every corresponding index to a number
    for num in lst:
        countlst[num] += 1

    # from 1 to max+1, update cumulative sum across all elements (last will be size of original list)
    for i in range(1, m + 1):
        countlst[i] += countlst[i - 1]

    sortedlst = [0] * len(lst)  # initialize output list

    # for the elements of original list, use cumulative count to place elements into sorted list in the correct spot
    # countlst is decremented to keep track of what we've placed so far
    for num in lst:
        sortedlst[countlst[num] - 1] = num
        countlst[num] -= 1

    return sortedlst

# ------------------------------------------------------------
# runtime tracking functions:

def measureexecution():
    # for number of times we want to measure:
    numtimes = 100
    exectimeslst = []

    # running the sort algorithm for numtimes
    for i in range(numtimes):
        lst = []
        begin = time.time()  # record time beginning
        randlst = ListGenerator.randList()
        lst.append(len(randlst))
        countsort(ListGenerator.randList())
        end = time.time()  # record time ending
        lst.append(end - begin)
        exectimeslst.append(lst)  # add lst with two values (size, time) for each

    avg = 0
    avgsize = 0
    kor = False  # set true if want individual information of each size/runtime

    # display individual results if turned on using bool kor, otherwise calculates average time and size
    for i in exectimeslst:
        if kor:
            print(f"Input size: {i[0]} | Execution time: {i[1]}s\n")
        avg += i[1]
        avgsize += i[0]

    # find best/worst cases
    maxtime = max(exectimeslst, key=lambda x: x[1])
    mintime = min(exectimeslst, key=lambda x: x[1])

    # display ultimate results
    print("\n")
    print("Counting Sort Results: ".center(53))
    print(f"(Over {numtimes} iterations)".center(52))
    print("-"*53)
    print(f"Average time: {avg / numtimes:<12.10f} | Average size:    {avgsize / numtimes:>6.2f}")
    print(f"Worst time:   {maxtime[1]:<12.10f} | Size:             {maxtime[0]:>6}")
    print(f"Best time:    {mintime[1]:<12.10f} | Size:             {mintime[0]:>6}")
    print("-" * 53)
# -------------------------------------------------------------
measureexecution()

