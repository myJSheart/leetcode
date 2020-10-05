#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> str:
        stack = ''
        longest_palindrome = ''

        i = 2
        x = y = -1
        flag = False
        while i < s.__len__():
            if not flag:
                if s[i] == s[i - 1]:
                    x = i - 1
                    y = i
                elif s[i] == s[i - 2]:
                    x = i - 2
                    y = i
                flag = True

        return longest_palindrome

# @lc code=end
