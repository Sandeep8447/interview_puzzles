# Task:
#
# You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.
#
# Example:
#
# [34, -50, 42, 14, -5, 86]
#
# Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].
#
# Your solution should run in linear time.
#
# Here's a starting point:
#
# def max_subarray_sum(arr):
#   # Fill this in.
#
# print max_subarray_sum([34, -50, 42, 14, -5, 86])
# # 137
from typing import List, Optional


def max_subarray_sum(arr: List[int]) -> int:
    """Complexities of this method:

    - time complexity O(n) where *n* is a length of the input array *arr*
    - space complexity O(1)
    """

    if len(arr) == 0:
        return 0
    else:
        max_sum: Optional[int] = None
        current_max_sum: Optional[int] = None
        current_sum: Optional[int] = None
        for i in range(0, len(arr)):
            current_num: int = arr[i]
            current_sum = current_sum + current_num if current_sum else current_num
            if not current_max_sum:
                current_max_sum = current_sum
            if (current_max_sum >= 0 > current_sum) or (current_sum < current_max_sum < 0):
                current_sum = None
            else:
                current_max_sum = current_sum
            max_sum = max(max_sum, current_max_sum) if max_sum else current_max_sum
        return max_sum


print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137
print(max_subarray_sum([34, -50, 42, 14, -5, 86, -5]))
# 137
print(max_subarray_sum([-34, -50, -5]))
# -5
