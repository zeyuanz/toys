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
import time


nums = [random.randint(0,10000) for i in range(100000)]
nums2 = copy.deepcopy(nums)

start = time.time()
quicksort(nums, 0, len(nums))
end = time.time()
quicksort_time = end - start

start = time.time()
nums2.sort()
end = time.time()
python_time = end - start

assert(nums == nums2)

print("Quicksort time: %.4f" %(quicksort_time))
print("Python sort time: %.4f" %(python_time))
