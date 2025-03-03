from .sort_algorithm import SortingAlgorithm

class InsertionSort(SortingAlgorithm):
    @classmethod
    def sort(cls, data):
        stages = [data.copy()]
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
            stages.append(data.copy())
        return stages