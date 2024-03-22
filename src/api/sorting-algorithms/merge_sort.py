from sort_algorithm import SortingAlgorithm


class MergeSort(SortingAlgorithm):
    @staticmethod
    def merge(left, right):
        result = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result

    @classmethod
    def sort(cls, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = cls.sort(left)
        right = cls.sort(right)

        return cls.merge(left, right)
