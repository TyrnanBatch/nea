from sort_algorithm import SortingAlgorithm


class BubbleSort(SortingAlgorithm):
    @classmethod
    def sort(cls, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    cls.swap(data, j, j + 1)
        return data
