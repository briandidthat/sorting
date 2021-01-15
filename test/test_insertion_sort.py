import unittest
from algos.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_insert(self):
        data = [4, 1, 6, 2, 7, 0]
        sorted_list = sorted(data)
        insertion_sort(data)
        self.assertListEqual(data, sorted_list, f"Array must be in ascending order. {data}")
