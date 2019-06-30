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
        rows = len(grid)
        if rows==0:
            return 0
        columns = len(grid[0])
        visited = [[False]*columns for _ in range(rows)]
        max_area = 0

        def dfs(row,column):
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            coordinates = [(row+x,column+y) for x,y in directions]
            area = 1
            for r,c in coordinates:
                if 0<=r<rows and 0<=c<columns and grid[r][c]==1 and not visited[r][c]:
                    visited[r][c] = True
                    area += dfs(r,c)
            return area


        for row in range(rows):
            for column in range(columns):
                if visited[row][column]:
                    continue
                visited[row][column] = True
                if grid[row][column]==0:
                    continue
                else:
                    area = dfs(row,column)
                    max_area = area if area>max_area else max_area

        return max_area


        
