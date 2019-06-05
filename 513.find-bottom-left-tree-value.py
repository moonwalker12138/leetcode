#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (58.43%)
# Total Accepted:    71.7K
# Total Submissions: 122.8K
# Testcase Example:  '[2,1,3]'
#
# 
# Given a binary tree, find the leftmost value in the last row of the tree. 
# 
# 
# Example 1:
# 
# Input:
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# Output:
# 1
# 
# 
# 
# ⁠ Example 2: 
# 
# Input:
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   5   6
# ⁠      /
# ⁠     7
# 
# Output:
# 7
# 
# 
# 
# Note:
# You may assume the tree (i.e., the given root node) is not NULL.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        def dfs(root):
            height = 0
            val = root.val
            if root.left:
                height, val = dfs(root.left)
            if root.right:
                _height,_val = dfs(root.right)
                if _height>height:
                    height = _height
                    val = _val
            return height+1,val

        return dfs(root)[1]

