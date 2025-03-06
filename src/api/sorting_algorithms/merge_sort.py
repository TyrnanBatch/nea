from .sort_algorithm import SortingAlgorithm


class MergeSort(SortingAlgorithm):
    @classmethod
    def sort(cls, data):
        def _merge_and_track_stages(arr, left, mid, right, stages):
            left_half = arr[left:mid + 1]
            right_half = arr[mid + 1:right + 1]

            i = j = 0
            k = left

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

            stages.append(arr.copy())

        def _merge_sort(arr, left, right, stages):
            if left < right:
                mid = (left + right) // 2
                _merge_sort(arr, left, mid, stages)
                _merge_sort(arr, mid + 1, right, stages)
                _merge_and_track_stages(arr, left, mid, right, stages)

        stages = [data.copy()]
        _merge_sort(data, 0, len(data) - 1, stages)
        return stages