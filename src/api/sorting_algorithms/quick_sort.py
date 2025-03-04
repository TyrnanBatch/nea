from .sort_algorithm import SortingAlgorithm

class QuickSort(SortingAlgorithm):
    @classmethod
    def sort(cls, data):
        stages = [data.copy()]
        cls._quicksort(data, 0, len(data) - 1, stages)
        return stages

    @staticmethod
    def _quicksort(data, low, high, stages):
        if low < high:
            pivot_index = QuickSort._partition(data, low, high, stages)
            QuickSort._quicksort(data, low, pivot_index - 1, stages)
            QuickSort._quicksort(data, pivot_index + 1, high, stages)

    @staticmethod
    def _partition(data, low, high, stages):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if data[j] < pivot:
                i += 1
                QuickSort.swap(data, i, j)
                stages.append(data.copy())
        QuickSort.swap(data, i + 1, high)
        stages.append(data.copy())
        return i + 1