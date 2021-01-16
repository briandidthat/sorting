from typing import List


def counting_sort(array: List[int], k: int):
    """
    :param array: unsorted array of integers.
    :param k: maximum number in array
    :return:
    """

    counter = [0] * (k + 1)
    for i in array:
        counter[i] += 1

    ndx = 0
    for j in range(len(counter)):
        while 0 < counter[j]:
            array[ndx] = j
            ndx += 1
            counter[j] -= 1
