#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#
# https://leetcode.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (37.33%)
# Total Accepted:    152.6K
# Total Submissions: 405.5K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list using insertion sort.
# 
# 
# 
# 
# 
# A graphical example of insertion sort. The partial sorted list (black)
# initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and
# inserted in-place into the sorted list
# 
# 
# 
# 
# 
# Algorithm of Insertion Sort:
# 
# 
# Insertion sort iterates, consuming one input element each repetition, and
# growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data,
# finds the location it belongs within the sorted list, and inserts it
# there.
# It repeats until no input elements remain.
# 
# 
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
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        if head is None:
            return None

        prev = head
        curr = head.next

        while curr:
            if curr.val<head.val:
                prev.next = curr.next
                curr.next = head
                head = curr
                curr = prev.next
            elif curr.val>=prev.val:
                prev = prev.next
                curr = curr.next
            else:
                cursor = head
                while cursor:
                    if cursor.val<=curr.val<cursor.next.val:
                        prev.next = curr.next
                        curr.next = cursor.next
                        cursor.next = curr
                        curr = prev.next
                        break
                    else:
                        cursor = cursor.next

        return head

def create(li):
    if len(li)==0:
        return None
    head = ListNode(li[0])
    curr = head
    for val in li[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def display(head):
    curr = head
    li = []
    while curr:
        li.append(curr.val)
        curr = curr.next
    return li


if __name__ == '__main__':
    solution = Solution()
    head = create([4,2,1,3])
    solution.insertionSortList(head)


