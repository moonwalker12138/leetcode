# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (36.85%)
# Total Accepted:    44.1K
# Total Submissions: 117.6K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.
# 
# Note:
# 
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# 
# 
# Example:
# 
# Given the following 5x5 matrix:
# 
# ⁠ Pacific ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
# 
# Return:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).
# 
# 
#
class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix:
            return []
        row, column = len(matrix), len(matrix[0])
        pacific_visited = [[False for j in range(column)] for i in range(row)]
        atlantic_visited = [[False for j in range(column)] for i in range(row)]

        def dfs(i, j, visited):
            visited[i][j] = True
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dir in directions:
                x, y = i + dir[0], j + dir[1]
                if x >= 0 and x < row and y >= 0 and y < column and not visited[x][y] and matrix[x][y] >= matrix[i][j]:
                    dfs(x, y, visited)

        for j in range(column):
            dfs(0, j, pacific_visited)
            dfs(row - 1, j, atlantic_visited)

        for i in range(row):
            dfs(i, 0, pacific_visited)
            dfs(i, column - 1, atlantic_visited)

        res = [[i, j] for i in range(row) for j in range(column) if pacific_visited[i][j] and atlantic_visited[i][j]]
        return res


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    res = solution.pacificAtlantic(matrix)
    print(res)

