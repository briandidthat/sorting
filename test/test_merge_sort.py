import unittest
from algos.merge_sort import merge_sort


class TestMerge(unittest.TestCase):
    def test_merge(self):
        # test that input array is sorted in ascending order.
        data = [4, 1, 6, 2, 7, 0]
        sorted_list = sorted(data)
        merge_sort(data, 0, len(data) - 1)
        self.assertListEqual(data, sorted_list, f"Array must be in ascending order. {data}")
