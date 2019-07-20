#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (50.15%)
# Total Accepted:    96.1K
# Total Submissions: 190.3K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
# 
# 
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1, stack2 = [],[]

        curr = l1
        while curr:
            stack1.append(curr.val)
            curr = curr.next

        curr = l2
        while curr:
            stack2.append(curr.val)
            curr = curr.next

        carry = 0
        head = None
        while len(stack1)>0 or len(stack2)>0:
            val = carry
            if len(stack1)>0:
                val += stack1.pop()
            if len(stack2)>0:
                val += stack2.pop()
            carry,val = divmod(val,10)
            curr = ListNode(val)
            curr.next = head
            head = curr

        if carry>0:
            curr = ListNode(carry)
            curr.next = head
            head = curr


        return head

