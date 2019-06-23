#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (57.80%)
# Total Accepted:    65.3K
# Total Submissions: 112.8K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# You need to find the largest value in each row of a binary tree.
# 
# Example:
# 
# Input: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \  
# ⁠     5   3   9 
# 
# Output: [1, 3, 9]
# 
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        output = []

        def dfs(node,depth):
            if not node:
                return
            if depth==len(output):
                output.append(node.val)
            else:
                output[depth] = output[depth] if output[depth]>=node.val else node.val
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)

        dfs(root,0)
        return output

