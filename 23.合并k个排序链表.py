#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (48.27%)
# Likes:    440
# Dislikes: 0
# Total Accepted:    64.6K
# Total Submissions: 133.8K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return
        return self.merge(lists, 0, len(lists)-1)

    def merge(self, lists: List[ListNode], left: int, right: int) -> ListNode:
        if left==right:
            return lists[left]
        mid = (left + right) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.merge2Lists(l1, l2)

    def merge2Lists(self, l1:ListNode, l2:ListNode) -> ListNode:
        """ two pointers """
        head = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return head.next

if __name__ == "__main__":
    def generate_list(l:List[int]) -> ListNode:
        head = cur = ListNode(0)
        for i in l:
            cur.next = ListNode(i)
            cur = cur.next
        return head.next
    def to_list(l:ListNode):
        nodes = []
        while l:
            nodes.append(l.val)
            l = l.next
        return nodes


    l1 = generate_list([1,3,5,7,9])
    l2 = generate_list([2,4,6,8,10])
    l3 = Solution().merge2Lists(l1, l2)
    print(to_list(l3))


# @lc code=end

