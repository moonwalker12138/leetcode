#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (41.08%)
# Total Accepted:    169.5K
# Total Submissions: 411K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
class Solution:
    def numSquares(self, n: int) -> int:
        # dp = [0]
        # while len(dp) <= n:
        #     dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        # return dp[n]
        dp = [None]*(n+1)
        for i in range(1,len(dp)):
            if int(i**0.5)**2==i:
                dp[i] = 1
            else:
                dp[i] = min(dp[i-j*j] for j in range(1,int(i**0.5)+1)) + 1
        return dp[n]

if __name__=='__main__':
    solution = Solution()
    n = 28
    res = solution.numSquares(n)
    print(res)

# --solution--
