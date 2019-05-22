#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (42.84%)
# Total Accepted:    397.8K
# Total Submissions: 916.7K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# But the following [1,2,2,null,3,null,3] is not:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# # recursive
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         def isMirror(l,r):
#             if l==None and r==None:
#                 return True
#             if l==None or r==None:
#                 return False
#             return l.val==r.val and isMirror(l.left,r.right) and isMirror(l.right,r.left)

#         if root==None:
#             return True
#         return isMirror(root.left,root.right)

# iterative
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        import queue
        q = queue.Queue()
        q.put(root.left)
        q.put(root.right)
        while not q.empty():
            l = q.get()
            r = q.get()
            if l==None and r==None:
                continue
            if l==None or r==None or l.val!=r.val:
                return False
            q.put(l.left)
            q.put(r.right)
            q.put(l.right)
            q.put(r.left)
        return True
