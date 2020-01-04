#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (41.58%)
# Likes:    3772
# Dislikes: 137
# Total Accepted:    507.6K
# Total Submissions: 1.1M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
#
# Example 1:
#
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
#
# Example 2:
#
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
#
#

# @lc code=start
class UF:
    def __init__(self, N):
        self.pre = list(range(N))
    def find(self, x):
        # find root
        r = x
        while self.pre[r]!=r:
            r = self.pre[r]
        # compress path
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
# find-union solution
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if grid is None or len(grid)==0: return 0
#         def get_id(row, col):
#             return row * len(grid[0]) + col
#         # convert matrix to edges representing connected islands
#         edges = []
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j]=="0": continue
#                 cur_id = get_id(i ,j)
#                 # self loop
#                 edges.append((cur_id, cur_id))
#                 for dir in [[1,0], [0,1]]:
#                     x,y = i+dir[0], j+dir[1]
#                     if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=="1":
#                         edges.append((cur_id, get_id(x,y)))
#         # ? union-find init, too much memory usage
#         uf = UF(len(grid) * len(grid[0]))
#         for l,r in edges:
#             uf.union(l,r)
#         # count different root nodes
#         roots = set()
#         for l,r in edges:
#             roots.add(uf.find(l))
#             roots.add(uf.find(r))
#         ans = len(roots)
#         return ans

# dfs solution
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def dfs(i, j, grid):
#             grid[i][j] = "0"
#             for dir in [[1,0],[-1,0],[0,1],[0,-1]]:
#                 x,y = i+dir[0], j+dir[1]
#                 if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=="1":
#                     dfs(x, y, grid)

#         num = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j]=="1":
#                     dfs(i, j, grid)
#                     num += 1

#         return num

# bfs solution
from queue import Queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j, grid):
            q = Queue()
            q.put((i,j))
            grid[i][j] = "0"
            while not q.empty():
                l,r = q.get()
                for dir in [[1,0],[-1,0],[0,1],[0,-1]]:
                    x,y = l+dir[0], r+dir[1]
                    if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=="1":
                        q.put((x,y))
                        grid[x][y] = "0"

        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    bfs(i, j, grid)
                    num += 1
        return num

if __name__ == "__main__":
    grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
    ans = Solution().numIslands(grid)
    print(ans)


# @lc code=end

