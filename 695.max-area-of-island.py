#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (57.28%)
# Total Accepted:    86.2K
# Total Submissions: 149.6K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
# 
# Find the maximum area of an island in the given 2D array. (If there is no
# island, the maximum area is 0.)
# 
# Example 1:
# 
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# Given the above grid, return 6. Note the answer is not 11, because the island
# must be connected 4-directionally.
# 
# Example 2:
# 
# 
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# 
# Note: The length of each dimension in the given grid does not exceed 50.
# 
#
class Solution:
    def maxAreaOfIsland(self, grid):

        def dfs(row,column):
            if not (0<=row<rows and 0<=column<columns)\
                    or grid[row][column]==0\
                    or visited[row][column]:
                return 0
            visited[row][column] = True
            return 1 + dfs(row-1,column) + dfs(row+1,column) + dfs(row,column-1) + dfs(row,column+1)

        rows = len(grid)
        if rows==0:
            return 0
        columns = len(grid[0])
        visited = [[False]*columns for _ in range(rows)]
        max_area = 0

        for row in range(rows):
            for column in range(columns):
                if not visited[row][column] and grid[row][column]==1:
                    max_area = max(dfs(row,column),max_area)

        return max_area


        
