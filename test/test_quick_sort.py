import unittest
from algos.quick_sort import quick_sort


class TestQuick(unittest.TestCase):
    def test_quick(self):
        # test that input array is sorted in ascending order.
        data = [4, 1, 6, 2, 7, 0]
        sorted_list = sorted(data)
        quick_sort(data, 0, len(data) - 1)
        self.assertListEqual(data, sorted_list, f"Array must be in ascending order. {data}")