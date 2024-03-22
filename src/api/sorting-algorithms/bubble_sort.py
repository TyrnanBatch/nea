from sort_algorithm import SortingAlgorithm


class BubbleSort(SortingAlgorithm):
    @classmethod
    def sort(cls, data):
        stages = [data.copy()]  # Initialize arr with the initial data
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    cls.swap(data, j, j + 1)
                    stages.append(data.copy())  # Append a copy of the current state to arr
        return stages
