import CountingSort
import ListGenerator
import QuickSort
import MeasureExecution
import GharibiSort

if __name__ == '__main__':
    test_data = ListGenerator.get_data(100)  # test data -- contains 10 random

    print("                    Quick Sort Test\n                  -==================-\n")

    MeasureExecution.measure_execution(QuickSort.quick_sort, test_data)

    print("                    Counting Sort Test\n                   -==================-\n")

    MeasureExecution.measure_execution(CountingSort.count_sort, test_data)

    print("                    Gharibi Sort Test\n                   -==================-\n")

    MeasureExecution.measure_execution(GharibiSort.GharibiSort, test_data)