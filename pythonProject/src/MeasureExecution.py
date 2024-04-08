import ListGenerator
import time

#
#
def measureexecution(func):
    # for number of times we want to measure:
    num_times = 100
    exectimes_lst = []

    # running the sort algorithm for numtimes
    for i in range(num_times):
        lst = []
        begin = time.time()  # record time beginning
        rand_lst = ListGenerator.randList()
        lst.append(len(rand_lst))
        func(ListGenerator.randList())
        end = time.time()  # record time ending
        lst.append(end - begin)
        exectimes_lst.append(lst)  # add lst with two values (size, time) for each

    avg = 0
    avg_size = 0
    kor = False  # set true if want individual information of each size/runtime

    # display individual results if turned on using bool kor, otherwise calculates average time and size
    for i in exectimes_lst:
        if kor:
            print(f"Input size: {i[0]} | Execution time: {i[1]}s\n")
        avg += i[1]
        avg_size += i[0]

    # find best/worst cases
    max_time = max(exectimes_lst, key=lambda x: x[1])
    min_time = min(exectimes_lst, key=lambda x: x[1])

    # display ultimate results
    print("\n")
    print("Sort Results: ".center(53))
    print(f"(Over {num_times} iterations)".center(52))
    print("-"*53)
    print(f"Average time: {avg / num_times:<12.10f} | Average size:    {avg_size / num_times:>6.2f}")
    print(f"Worst time:   {max_time[1]:<12.10f} | Size:             {max_time[0]:>6}")
    print(f"Best time:    {min_time[1]:<12.10f} | Size:             {min_time[0]:>6}")
    print("-" * 53)