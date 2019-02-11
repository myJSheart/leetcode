#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.05%)
# Total Accepted:    593.3K
# Total Submissions: 2.4M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.
# 
#
class Solution:
    def reverse(self, x: 'int') -> 'int':
        str_int = str(x)
        if x < 0:
            str_int = str_int[1:]
        reversed_str = ''
        for i in range(str_int.__len__()):
            reversed_str = str_int[i] + reversed_str
        reversed_int = int(reversed_str)
        if x < 0:
            reversed_int = -reversed_int
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        return reversed_int
