from typing import List


def partition(array: List[int], start: int, end: int):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high -= 1

        # Opposite direction process of the one above
        while low <= high and array[low] <= pivot:
            low += 1

        # We either found a value for both high and low that is out of order and must be swapped.
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            # or low is higher than high, in which case we must exit the loop.
            break
    # final swap before returning high
    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array: List[int], start: int, end: int):
    """
    * algo type: divide and conquer algorithm that splits the array into smaller arrays.
    * in place: True. Quick sort does not create any copies of the array or its subarray.
    * stability: Unstable since it does not guarantee that identical elemets will not be swapped.
    * time complexity: Best Case: O(n log n), Worst Case: O(n^2) Quadratic time
    :param array: unsorted array of integers
    :param start: initial lowest value of array, usually 0
    :param end: last element in array
    """
    # if start is greater than or equal to the length of array, we have nothing to sort
    if start >= end:
        return

    pi = partition(array, start, end)
    quick_sort(array, start, pi - 1)
    quick_sort(array, pi + 1, end)
