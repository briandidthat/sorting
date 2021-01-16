from typing import List


def selection_sort(array: List[int]):
    """
    * paradigm: Comparison based incremental algo
    * in place: True. Selection sort does not create any copies of the array or its subarray.
    * stability: Unstable because it does not guarantee that identical elements wont be swapped.
    * time complexity: Best case: O(n^2), Average: O(n^2)
    :param array: unsorted array of integers.
    """
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
