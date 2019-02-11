#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (41.43%)
# Total Accepted:    496.5K
# Total Submissions: 1.2M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Could you solve it without converting the integer to a string?
# 
#
class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        if x < 0:
            return False

        start_position = 1
        end_position = 1
        while x // 10**(end_position - 1) >= 10:
            end_position += 1

        while start_position < end_position:
            front = (x % 10**start_position) // 10**(start_position - 1)
            end = (x % 10**end_position) // 10**(end_position - 1)

            if front != end:
                return False
            start_position += 1
            end_position -= 1

        return True
