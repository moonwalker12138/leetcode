#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#
# https://leetcode.com/problems/out-of-boundary-paths/description/
#
# algorithms
# Medium (31.36%)
# Total Accepted:    16.2K
# Total Submissions: 51.3K
# Testcase Example:  '2\n2\n2\n0\n0'
#
# There is an m by n grid with a ball. Given the start coordinate (i,j) of the
# ball, you can move the ball to adjacent cell or cross the grid boundary in
# four directions (up, down, left, right). However, you can at most move N
# times. Find out the number of paths to move the ball out of grid boundary.
# The answer may be very large, return it after mod 109 + 7.
# 
# 
# 
# Example 1:
# 
# 
# Input: m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:
# 
# 
# 
# Example 2:
# 
# 
# Input: m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# 
# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].
# 
# 
#
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        memo = {}

        def helper(N,i,j):
            key = (i,j,N)
            if key in memo.keys():
                return memo[key]
            if i not in range(0,m) or j not in range(0,n):  # out of boundary
                return 1
            elif N <= 0:    # within boundary but have no chance to move the ball
                return 0
            else:
                memo[key] = helper(N-1,i-1,j)+helper(N-1,i+1,j)+helper(N-1,i,j-1)+helper(N-1,i,j+1)
                return memo[key]

        return helper(N,i,j) % (10**9 +7)

if __name__=='__main__':
    solution = Solution()
    res = solution.findPaths(2,2,2,0,0)
    print(res)
