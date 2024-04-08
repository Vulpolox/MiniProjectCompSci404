import ListGenerator
import time


# pre: take in a sorting algorithm and list of lists that contains random integers fo random sizes
# find and record time for each list
# determine averages
# post: display results
def measure_execution(func: staticmethod, random_lst: list) -> None:
    # for number of times we want to measure:
    exec_times_lst = []

    # running the sort algorithm for size of imported list of lists
    for i in random_lst:
        lst = []
        begin = time.time()  # record time beginning
        lst.append(len(i))
        func(i)
        end = time.time()  # record time ending
        lst.append(end - begin)
        exec_times_lst.append(lst)  # add lst with two values (size, time) for each

    avg = 0
    avg_size = 0
    kor = False  # set true if want individual information of each size/runtime

    # display individual results if turned on using bool kor, otherwise calculates average time and size
    for i in exec_times_lst:
        if kor:
            print(f"Input size: {i[0]} | Execution time: {i[1]}s\n")
        avg += i[1]
        avg_size += i[0]

    # find best/worst cases
    max_time = max(exec_times_lst, key=lambda x: x[1])
    min_time = min(exec_times_lst, key=lambda x: x[1])

    # display ultimate results
    print("\n")
    print("Sort Results: ".center(53))
    print(f"(Over {len(random_lst)} iterations)".center(52))
    print("-"*53)
    print(f"Average time: {avg / len(random_lst):<12.10f} | Average size:    {avg_size / len(random_lst):>6.2f}")
    print(f"Worst time:   {max_time[1]:<12.10f} | Size:             {max_time[0]:>6}")
    print(f"Best time:    {min_time[1]:<12.10f} | Size:             {min_time[0]:>6}")
    print("-" * 53)