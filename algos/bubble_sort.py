def bubble_sort(array: list):
    """
    * time complexity: Worst case: O(n^2)
    * stability: Stable sorting algorithm since identical elements will not be swapped.
    :param array: Will accept an array of integers as input and sort them in place.
    :return: array of integers sorted in ascending order.
    """

    # We want to stop passing through the list
    # as soon as we pass through without swapping any elements
    has_swapped = True

    while(has_swapped):
        has_swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                # Since the left element is greater, swap
                array[i], array[i + 1] = array[i + 1], array[i]
                has_swapped = True