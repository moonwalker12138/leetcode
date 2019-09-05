#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (37.30%)
# Total Accepted:    176.6K
# Total Submissions: 461.2K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# Example:
# 
# 
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
# 
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = ListNode(None)
        curr_before = before
        after = ListNode(None)
        curr_after = after

        curr = head
        while curr:
            if curr.val < x:
                curr_before.next = curr
                curr_before = curr
            else:
                curr_after.next = curr
                curr_after = curr
            _ = curr
            curr = curr.next
            _.next = None

        before = before.next
        after = after.next

        if before:
            curr_before.next = after
            return before
        else:
            return after



