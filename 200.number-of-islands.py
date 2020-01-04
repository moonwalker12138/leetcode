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
""" union-find solution """
class UnionFind:
    def __init__(self, grid):
        row, col = len(grid), len(grid[0])
        self.parent = [None] * (row * col)
        self.rank = [1] * (row * col)
        self._size = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    self.parent[i*col+j] = i*col+j
                    self._size += 1

    def find(self, x):
        """ find with path compression """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """ union with rank """
        root_x, root_y = self.find(x), self.find(y)
        if root_x!=root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1
            self._size -= 1

    @property
    def size(self):
        return self._size

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid)==0: return 0
        uf = UnionFind(grid)

        def get_id(row, col):
            return row * len(grid[0]) + col

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    cur_id = get_id(i,j)
                    for dir in [[1,0], [0,1], [-1,0], [0,-1]]:
                        x,y = i+dir[0], j+dir[1]
                        if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=="1":
                            uf.union(cur_id, get_id(x,y))

        return uf.size

""" dfs solution """
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

""" bfs solution """
# from queue import Queue
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def bfs(i, j, grid):
#             q = Queue()
#             q.put((i,j))
#             grid[i][j] = "0"
#             while not q.empty():
#                 l,r = q.get()
#                 for dir in [[1,0],[-1,0],[0,1],[0,-1]]:
#                     x,y = l+dir[0], r+dir[1]
#                     if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=="1":
#                         q.put((x,y))
#                         grid[x][y] = "0"

#         num = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j]=="1":
#                     bfs(i, j, grid)
#                     num += 1
#         return num

if __name__ == "__main__":
    grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
    ans = Solution().numIslands(grid)
    print(ans)


# @lc code=end

