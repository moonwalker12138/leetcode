#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (35.44%)
# Total Accepted:    198.3K
# Total Submissions: 542K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
# 
# Example 1:
# 
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# 
# Example 2:
# 
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # dummyHead
        dummyHead = ListNode(0)
        dummyHead.next = head
        # length
        length = 0
        cur = head
        while cur!=None:
            length += 1
            cur = cur.next
        # iteration
        size = 1
        while size<length:
            cur = dummyHead.next
            tail = dummyHead
            while cur:
                l = cur
                r = self.cut(cur,size)
                cur = self.cut(r,size)
                tail.next = self.merge(l,r)
                while tail.next!=None:
                    tail = tail.next
            size *= 2

        return dummyHead.next

    def cut(self,head,n):
        p = head
        for _ in range(n-1):
            if p!=None:
                p = p.next
            else:
                break
        if p==None:
            return None
        next = p.next
        p.next = None
        return next

    def merge(self, l, r):
        dummyHead = ListNode(0)
        cur = dummyHead
        while l != None and r != None:
            if l.val < r.val:
                cur.next = l
                l = l.next
                cur = cur.next
            else:
                cur.next = r
                r = r.next
                cur = cur.next
        if l != None:
            cur.next = l
        if r != None:
            cur.next = r
        return dummyHead.next


# recursive
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         return None if head is None else self.mergeSort(head)
#
#     def mergeSort(self, head):
#         if head.next is None:
#             return head
#         pre = None
#         slow, fast = head,head
#         while fast != None and fast.next != None:
#             pre = slow
#             slow = slow.next
#             fast = fast.next.next
#         pre.next = None
#         l = self.mergeSort(head)
#         r = self.mergeSort(slow)
#         return self.merge(l, r)
#
#     def merge(self, l, r):
#         dummyHead = ListNode(0)
#         cur = dummyHead
#         while l != None and r != None:
#             if l.val < r.val:
#                 cur.next = l
#                 l = l.next
#                 cur = cur.next
#             else:
#                 cur.next = r
#                 r = r.next
#                 cur = cur.next
#         if l != None:
#             cur.next = l
#         if r != None:
#             cur.next = r
#         return dummyHead.next

