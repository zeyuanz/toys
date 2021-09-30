#!/usr/local/bin/python3

def quicksort(nums, start, end):
    if end-start == 2:
        if nums[end-1] < nums[start]:
            nums[end-1], nums[start] = nums[start], nums[end-1]

    if end-start >= 3:
        base = nums[end-1]
        lo_idx = start
        for i in range(start, end-1):
            if nums[i] < base:
                nums[lo_idx], nums[i] = nums[i], nums[lo_idx]
                lo_idx += 1
        nums[end-1], nums[lo_idx] = nums[lo_idx], nums[end-1]
        quicksort(nums, start, lo_idx)
        quicksort(nums, lo_idx+1, end)

import random
import copy
import unittest

class TestSortMethod(unittest.TestCase):
    def test_10(self):
        for i in range(5):
            nums = [random.randint(0, 10) for i in range(10)]
            nums_test = copy.deepcopy(nums)

            quicksort(nums, 0, len(nums))
            nums_test.sort()
            self.assertEqual(nums, nums_test)

    def test_100(self):
        for i in range(5):
            nums = [random.randint(0, 100) for i in range(100)]
            nums_test = copy.deepcopy(nums)

            quicksort(nums, 0, len(nums))
            nums_test.sort()
            self.assertEqual(nums, nums_test)

    def test_1000(self):
        for i in range(5):
            nums = [random.randint(0, 1000) for i in range(1000)]
            nums_test = copy.deepcopy(nums)

            quicksort(nums, 0, len(nums))
            nums_test.sort()
            self.assertEqual(nums, nums_test)

    def test_10000(self):
        for i in range(5):
            nums = [random.randint(0, 10000) for i in range(10000)]
            nums_test = copy.deepcopy(nums)

            quicksort(nums, 0, len(nums))
            nums_test.sort()
            self.assertEqual(nums, nums_test)

    def test_100000(self):
        for i in range(5):
            nums = [random.randint(0, 100000) for i in range(100000)]
            nums_test = copy.deepcopy(nums)

            quicksort(nums, 0, len(nums))
            nums_test.sort()
            self.assertEqual(nums, nums_test)

if __name__ == '__main__':
    unittest.main()

