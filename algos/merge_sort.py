from typing import List


def merge(array: List[int], left: int, right: int, middle: int):
    # make copies of both arrays we're trying to merge
    # the second parameter is non inclusive, so we must increase by 1
    left_copy = array[left: middle + 1]
    right_copy = array[middle + 1: right + 1]

    # Initial values for the variables that we use to keep track of where we are in the array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        # if our left array has the smaller element, put it in sorted part and then move forward
        # in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
        # opposite operation from the above
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1

        # Regardless of where we got our element from move forward in the sorted part
        sorted_index += 1

    # We ran otu of elements either in the left_copy or the right_copy so we will go through the remaining
    # elements and add them.
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1

    # Opposite operation from above
    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1


def merge_sort(array: List[int], left_index: int, right_index: int):
    """
    * paradigm: Divide and conquer algorithm that splits the array into smaller arrays.
    * in place: True. Quick sort does not create any copies of the array or its subarray.
    * stability: Stable since identical elements will not be swapped.
    * time complexity: Best Case: O(n log n) Logarithmic time, Worst Case: O(nlogn) Logarithmic time
    :param array: unsorted array of integers.
    :param left_index: initial lowest value of array, usually 0
    :param right_index: last element in array.
    """

    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)
