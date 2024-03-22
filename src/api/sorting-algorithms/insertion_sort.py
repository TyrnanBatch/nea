from sort_algorithm import SortingAlgorithm


class InsertionSort(SortingAlgorithm):
    @classmethod
    def sort(cls, data):
        stages = [data.copy()]  # Initialize stages array with the initial data
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                cls.swap(data, j + 1, j)
                stages.append(data.copy())  # Append a copy of the current state to stages
                j -= 1
            data[j + 1] = key
        return stages
