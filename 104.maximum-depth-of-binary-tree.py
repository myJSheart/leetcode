#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""Version 1"""
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0

#         max_depth = 1
#         max_left = 0
#         max_right = 0
#         if root.left:
#             max_left = self.maxDepth(root.left)
#         if root.right:
#             max_right = self.maxDepth(root.right)

#         if max_left > max_right:
#             max_depth += max_left
#         else:
#             max_depth += max_right

#         return max_depth

"""Version 2"""


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        max_left = self.maxDepth(root.left)
        max_right = self.maxDepth(root.right)

        if max_left > max_right:
            return max_left + 1

        return max_right + 1
# @lc code=end
