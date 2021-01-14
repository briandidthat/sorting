import unittest
from algos.bubble_sort import bubble_sort


class TestBubble(unittest.TestCase):
    def test_bubble(self):
        # test that the input array is sorted in ascending order
        data = [4, 1, 6, 2, 7, 0]
        sorted_list = sorted(data)
        bubble_sort(data)
        self.assertListEqual(data, sorted_list, f"Array must be in ascending order. {data}")
