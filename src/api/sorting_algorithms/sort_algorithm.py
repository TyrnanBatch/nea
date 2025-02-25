
class SortingAlgorithm:
    @staticmethod
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def check(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    @classmethod
    def sort(cls, data):
        raise NotImplementedError("sort method must be implemented in subclasses")
