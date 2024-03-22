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
    def sort(cls, data):
        if len(data) <= 1:
            return [data]

        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        left_stages = cls.sort(left)
        right_stages = cls.sort(right)
        stages = []

        for i, r in zip(left_stages, right_stages):
            merged = cls.merge(i, r)
            stages.append(merged)
        stages.extend(left_stages[len(right_stages):])
        stages.extend(right_stages[len(left_stages):])

        return stages
