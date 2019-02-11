#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.35%)
# Total Accepted:    744.4K
# Total Submissions: 2.4M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        reminder = 0
        head = ListNode(0)
        current_node = head
        while l1 or l2:
            sum_value = 0
            if l1:
                sum_value += l1.val
                l1 = l1.next
            if l2:
                sum_value += l2.val
                l2 = l2.next

            current_node.val += sum_value % 10
            reminder = sum_value // 10
            if current_node.val // 10 > 0:
                reminder += current_node.val // 10
                current_node.val = current_node.val % 10

            if l1 or l2:
                current_node.next = ListNode(reminder)
                current_node = current_node.next
            else:
                if reminder > 0:
                    current_node.next = ListNode(reminder)

        return head
