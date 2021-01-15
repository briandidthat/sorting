from typing import List


def insertion_sort(array: List[int]):
    """
    * paradigm: Incremental algorithm (simple sorting)
    * in place: True. Quick sort does not create any copies of the array or its subarray.
    * stability: Stable since identical elements will not be swapped.
    * time complexity: Best Case: O(n) Linear, Average: O(n^2) Quadratic
    :param array: unsorted array of integers.
    """
    # we start from 1 since the first element is trivially sorted
    for index in range(1, len(array)):
        current_value = array[index]
        current_position = index

        # as long as we havent reached the beginning and there is an element in our sorted array larger
        # larger than the one we are trying to insert - move the element to the right.
        while current_position > 0 and array[current_position - 1] > current_value:
            array[current_position] = array[current_position - 1]
            current_position -= 1
        # at this point we have either reached the beginning of the array or we have found an element in the array
        # smaller than the one we are trying to insert at index current position - 1 [left]. In either case, we insert
        # the element to current position
        array[current_position] = current_value
