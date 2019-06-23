#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (48.00%)
# Total Accepted:    172.2K
# Total Submissions: 357K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import queue


class Solution:
    def rightSideView(self, root):
        output = []

        def dfs(node,depth):
            if not node:
                return
            if depth==len(output):
                output.append(node.val)
            dfs(node.right,depth+1)
            dfs(node.left,depth+1)

        dfs(root,0)
        return output

if __name__ == '__main__':
    solution = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    ans = solution.rightSideView(root)
    print(ans)
