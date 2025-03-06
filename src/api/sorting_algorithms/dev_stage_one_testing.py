from src.api.sorting_algorithms import BubbleSort, InsertionSort, MergeSort
from src.api.sorting_algorithms.quick_sort import QuickSort


def test_for_data_being_sorted():
    data_to_be_sorted = [14, 463, 124, 42, 253, 14, 426, 36, 531, 36, 759, 634, 53, 463, 57, 46, 14, 1, 232, 453, 7]

    stages = BubbleSort.sort(data_to_be_sorted)

    print(stages[0], stages[len(stages) - 1])


def test_for_data_being_progressively_sorted():
    data_to_be_sorted = [134, 25, 435, 68, 461, 56, 8, 2463, 424, 5632, 58, 34, 53, 3, 57, 6]

    stages = BubbleSort.sort(data_to_be_sorted)

    print(stages)


def test_for_multiple_algorithms_sorting_data_progressively():
    data_to_be_sorted = [134, 25, 435, 68, 461, 56, 8, 235, 1426, 4, 643, 643, 16, 3, 143, 5143, 565, 3423, 436, 42,
                         4136, 351, 31]

    stages_bubble = BubbleSort.sort(data_to_be_sorted)
    stages_insertion = InsertionSort.sort(data_to_be_sorted)

    print(stages_bubble)
    print(stages_insertion)


def test_for_bubble_sort():
    data_to_be_sorted = [523, 463, 54, 648, 264, 531, 426, 573, 6, 635, 52, 523, 46]

    stages = BubbleSort.sort(data_to_be_sorted)

    print(stages)


def test_for_insertion_sort():
    data_to_be_sorted = [523, 463, 54, 648, 264, 531, 426, 573, 6, 635, 52, 523, 46]

    stages = InsertionSort.sort(data_to_be_sorted)

    print(stages)


def test_for_merge_sort():
    data_to_be_sorted = [635, 86, 3, 4, 65, 56, 758, 3568, 683, 7583, 635, 36, 56643, 265, 3652]

    stages = MergeSort.sort(data_to_be_sorted)

    print(stages)


def test_for_quick_sort():
    data_to_be_sorted = [523, 463, 54, 648, 264, 531, 426, 573, 6, 635, 52, 523, 46]

    stages = QuickSort.sort(data_to_be_sorted)

    print(stages)
