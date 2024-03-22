from sort_algorithm import SortingAlgorithm


class InsertionSort(SortingAlgorithm):
    @classmethod
    def sort(cls, data):
        stages = [data.copy()]
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                cls.swap(data, j + 1, j)
                stages.append(data.copy())
                j -= 1
            data[j + 1] = key
        return stages
