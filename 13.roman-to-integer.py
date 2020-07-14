#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start

"""Version 1"""
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_numberals = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         num = 0
#         # Scan every two characters
#         i = 0
#         while i < s.__len__():
#             if i == s.__len__() - 1:
#                 num += roman_numberals[s[i]]
#                 break

#             if roman_numberals[s[i]] < roman_numberals[s[i + 1]]:
#                 num += roman_numberals[s[i + 1]] - roman_numberals[s[i]]
#                 i = i + 2
#             else:
#                 num += roman_numberals[s[i]]
#                 i += 1

#         return num

"""Version 2"""
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_numberals = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         num = 0
#         # use more memory but save time for computing the length (2 times previously)
#         s_len = s.__len__()

#         for i in range(s_len - 1):
#             if roman_numberals[s[i]] < roman_numberals[s[i + 1]]:
#                 num -= roman_numberals[s[i]]
#             else:
#                 num += roman_numberals[s[i]]

#         num += roman_numberals[s[-1]]

#         return num

"""Version 3 (Best Solution)"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numberals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num = roman_numberals[s[-1]]

        s_len = s.__len__()

        for i in range(s_len - 1):
            num += (-roman_numberals[s[i]] if roman_numberals[s[i]]
                    < roman_numberals[s[i + 1]] else roman_numberals[s[i]])

        return num


# @lc code=end
