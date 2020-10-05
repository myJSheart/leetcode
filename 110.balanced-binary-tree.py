#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Version 1
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        if abs(self.count_height(root.left) - self.count_height(root.right)) > 1:
            return False

        is_left_balanced = self.isBalanced(root.left)
        is_right_balanced = self.isBalanced(root.right)

        return is_left_balanced & is_right_balanced

    def count_height(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_height = self.count_height(root.left)
        right_height = self.count_height(root.right)

        if left_height > right_height:
            return left_height + 1

        return right_height + 1
# @lc code=end
