#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (40.90%)
# Total Accepted:    179K
# Total Submissions: 435.1K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted linked list: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        if not head:
            return None

        mid,left_head,right_head = self.findMiddle(head)
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(left_head)
        root.right = self.sortedListToBST(right_head)

        return root

    def findMiddle(self,head):
        """
        Two pointer approach for finding out the middle element of a linked list:
        slow_ptr moves one node at a time; fast_ptr moves two nodes at a time.
        By the time the fast_ptr reaches the end of the linked list,
        the slow_ptr would have reached the middle element of the linked list.
        """
        slow_ptr = head
        fast_ptr = head
        prev_ptr = None
        while fast_ptr and fast_ptr.next:
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        if prev_ptr:
            prev_ptr.next = None
        left_head = head if prev_ptr else None
        right_head = slow_ptr.next
        return slow_ptr,left_head,right_head
