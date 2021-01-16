import unittest
from algos.counting_sort import counting_sort


class TestCountingSort(unittest.TestCase):
    def test_insert(self):
        data = [4, 1, 6, 2, 7, 0, 21, 5]
        maximum = max(data)
        sorted_list = sorted(data)
        counting_sort(data, maximum)
        self.assertListEqual(data, sorted_list, f"Array must be in ascending order. {data}")