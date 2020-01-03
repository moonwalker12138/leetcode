#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#
# https://leetcode.com/problems/minimum-height-trees/description/
#
# algorithms
# Medium (30.15%)
# Likes:    1356
# Dislikes: 81
# Total Accepted:    79.2K
# Total Submissions: 253.6K
# Testcase Example:  '4\n[[1,0],[1,2],[1,3]]'
#
# For an undirected graph with tree characteristics, we can choose any node as
# the root. The result graph is then a rooted tree. Among all possible rooted
# trees, those with minimum height are called minimum height trees (MHTs).
# Given such a graph, write a function to find all the MHTs and return a list
# of their root labels.
# 
# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be
# given the number n and a list of undirected edges (each edge is a pair of
# labels).
# 
# You can assume that no duplicate edges will appear in edges. Since all edges
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
# 
# Example 1 :
# 
# 
# Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
# 
# ⁠       0
# ⁠       |
# ⁠       1
# ⁠      / \
# ⁠     2   3 
# 
# Output: [1]
# 
# 
# Example 2 :
# 
# 
# Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
# 
# ⁠    0  1  2
# ⁠     \ | /
# ⁠       3
# ⁠       |
# ⁠       4
# ⁠       |
# ⁠       5 
# 
# Output: [3, 4]
# 
# Note:
# 
# 
# According to the definition of tree on Wikipedia: “a tree is an undirected
# graph in which any two vertices are connected by exactly one path. In other
# words, any connected graph without simple cycles is a tree.”
# The height of a rooted tree is the number of edges on the longest downward
# path between the root and a leaf.
# 
# 
#

# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1: return [0]
        degrees = [0] * n
        adj = [[] for _ in range(n)]
        for l,r in edges:
            adj[l].append(r)
            adj[r].append(l)
            degrees[l] += 1
            degrees[r] += 1
        
        from queue import Queue
        q = Queue()
        for i,degree in enumerate(degrees):
            if degree==1:
                q.put(i)
        
        ans = []
        while not q.empty():
            ans = []
            for _ in range(q.qsize()):
                cur = q.get()
                ans.append(cur)
                for i in adj[cur]:
                    degrees[i] -= 1
                    if degrees[i]==1:
                        q.put(i)
        return ans



        
# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

#         def dfs(i, adj, visited):
#             """calculate tree(i-th node as root) height
            
#             Args:
#                 i (int): node index
#                 adj (List[List[int]]): adjacency list
#                 visited (List[bool]): indicate whether i-th node is visited
            
#             Returns:
#                 [int]: tree height based on root i
#             """
#             visited[i] = True
#             candidates = [0]
#             for j in adj[i]:
#                 if not visited[j]:
#                     candidates.append(dfs(j, adj, visited))
#             height = 1 + max(candidates)
#             return height

#         # * consturct adjacency list
#         adj = [[] for _ in range(n)]
#         for l,r in edges:
#             adj[l].append(r)
#             adj[r].append(l)

#         heights = [0] * n
#         for i in range(n):
#             visited = [False for _ in range(n)]
#             heights[i] = dfs(i, adj, visited)
#         min_height = min(heights)
#         result = []
#         for i,height in enumerate(heights):
#             if height==min_height:
#                 result.append(i)
#         return result
        
# @lc code=end

