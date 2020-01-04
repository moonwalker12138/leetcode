#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
# https://leetcode.com/problems/redundant-connection/description/
#
# algorithms
# Medium (51.85%)
# Likes:    911
# Dislikes: 215
# Total Accepted:    71.2K
# Total Submissions: 130K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 
# In this problem, a tree is an undirected graph that is connected and has no
# cycles.
# 
# The given input is a graph that started as a tree with N nodes (with distinct
# values 1, 2, ..., N), with one additional edge added.  The added edge has two
# different vertices chosen from 1 to N, and was not an edge that already
# existed.
# 
# The resulting graph is given as a 2D-array of edges.  Each element of edges
# is a pair [u, v] with u < v, that represents an undirected edge connecting
# nodes u and v.
# 
# Return an edge that can be removed so that the resulting graph is a tree of N
# nodes.  If there are multiple answers, return the answer that occurs last in
# the given 2D-array.  The answer edge [u, v] should be in the same format,
# with u < v.
# Example 1:
# 
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
# ⁠ 1
# ⁠/ \
# 2 - 3
# 
# 
# Example 2:
# 
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
# ⁠   |   |
# ⁠   4 - 3
# 
# 
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is
# the size of the input array.
# 
# 
# 
# 
# 
# Update (2017-09-26):
# We have overhauled the problem description + test cases and specified clearly
# the graph is an undirected graph. For the directed graph follow up please see
# Redundant Connection II). We apologize for any inconvenience caused.
# 
#

# @lc code=start
class UF:
    def __init__(self, N):
        self.pre = list(range(N))
    def find(self, x):
        r = x
        while self.pre[r]!=r:
            r = self.pre[r]
        cur = x
        while cur!=r:
            p = self.pre[cur]
            self.pre[cur] = r
            cur = p
        return r
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx!=fy:
            self.pre[fx] = fy
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for l,r in edges:
            nodes.add(l)
            nodes.add(r)
        uf = UF(len(nodes) + 1)
        ans = None
        for x,y in edges:
            fx, fy = uf.find(x), uf.find(y)
            if fx!=fy:
                uf.union(x,y)
            else:
                ans = [x,y]
        return ans
# @lc code=end

