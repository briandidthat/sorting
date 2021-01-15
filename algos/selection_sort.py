from typing import List


def selection_sort(array: List[int]):
    # i indicates how many items have been sorted, len of array - 1
    for i in range(len(array) - 1):
        # to find the minimum value of the unsorted segment we first assume that
        # the first element is the smallest.
        min_index = i

        # we then loop the the remaining elements
        for j in range(i + 1, len(array)):
            # if j < element at min index, update min_index
            if array[j] < array[min_index]:
                min_index = j

        # After finding the lowest item of the unsorted segment, swap with first element of unsorted segment
        array[i], array[min_index] = array[min_index], array[i]
