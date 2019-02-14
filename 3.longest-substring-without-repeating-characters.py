#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (26.02%)
# Total Accepted:    736.8K
# Total Submissions: 2.8M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        if s.__len__() == 0:
            return 0

        substring_start = 0
        substring_end = 1
        current_length = 1
        for i in range(1, s.__len__()):
            if s[i] in s[substring_start: substring_end]:
                if current_length < substring_end - substring_start:
                    current_length = substring_end - substring_start
                substring_start = substring_start + s[substring_start: substring_end].index(s[i]) + 1
                substring_end = i + 1
            else:
                substring_end += 1

        if current_length < substring_end - substring_start:
            current_length = substring_end - substring_start

        return current_length
