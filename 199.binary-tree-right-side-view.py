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

class Tree:
    def __init__(self,nodes):
        self.root = TreeNode(next(nodes))
        q = queue.Queue()
        q.put(self.root)
        layer = 0
        while not q.empty():
            layer_nodes = [q.get() for _ in range(pow(2,layer))]
            for node in layer_nodes:
                node.left = next(nodes)

import queue


class Solution:
    def rightSideView(self, root):
        layer = 0
        output = []
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            layer_nodes = [q.get() for _ in range(pow(2,layer))]
            if not any(layer_nodes):
                break
            for node in layer_nodes:
                if node:
                    q.put(node.left)
                    q.put(node.right)
                else:
                    q.put(None)
                    q.put(None)
            for node in layer_nodes[::-1]:
                if node:
                    output.append(node.val)
                    break
            layer += 1
        return output

if __name__ == '__main__':
    solution = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    ans = solution.rightSideView(root)
    print(ans)
