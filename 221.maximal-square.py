#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (32.38%)
# Total Accepted:    120.6K
# Total Submissions: 372.3K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
# 
#
class Solution:
    def maximalSquare(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if i!=0 and j!=0 and matrix[i][j]!=0:
                    matrix[i][j] = min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j])+1
        area = 0 if len(matrix)==0 else max(map(max,matrix))**2
        return area
