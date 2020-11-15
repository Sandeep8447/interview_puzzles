# Task:
#
# The Fibonacci sequence is the integer sequence defined by the recurrence relation: F(n) = F(n-1) + F(n-2), where
# F(0) = 0 and F(1) = 1. In other words, the nth Fibonacci number is the sum of the prior two Fibonacci numbers. Below
# are the first few values of the sequence:
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
#
# Given a number n, print the n-th Fibonacci Number.
# Examples:
# Input: n = 3
# Output: 2
#
# Input: n = 7
# Output: 13
# Here's a starting point:
#
# class Solution():
#   def fibonacci(self, n):
#     # fill this in.
#
# n = 9
# print(Solution().fibonacci(n))
# # 34


class Solution:
    @staticmethod
    def calculate_xth_fibonacci_number(x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            fibonacci_number_n_minus_2: int = 0
            fibonacci_number_n_minus_1: int = 1
            for n in range(2, x + 1):
                current_fibonacci_number: int = fibonacci_number_n_minus_2 + fibonacci_number_n_minus_1
                fibonacci_number_n_minus_2 = fibonacci_number_n_minus_1
                fibonacci_number_n_minus_1 = current_fibonacci_number
            return fibonacci_number_n_minus_1
