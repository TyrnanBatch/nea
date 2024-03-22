from sort_algorithm import SortingAlgorithm


class InsertionSort(SortingAlgorithm):
    @classmethod
    def sort(cls, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                cls.swap(arr, j + 1, j)  # Using cls.swap() to access the swap method
                j -= 1
            arr[j + 1] = key
        return arr
