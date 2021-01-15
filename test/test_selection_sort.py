import unittest
from algos.selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    def test_quick(self):
        # test that input array is sorted in ascending order.
        data = [4, 1, 6, 2, 7, 0]
        sorted_list = sorted(data)
        selection_sort(data)
        self.assertListEqual(data, sorted_list, f"Array must be in ascending order. {data}")
