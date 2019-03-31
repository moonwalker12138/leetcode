#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (45.64%)
# Total Accepted:    54.7K
# Total Submissions: 119.4K
# Testcase Example:  '"bbbab"'
#
# 
# Given a string s, find the longest palindromic subsequence's length in s. You
# may assume that the maximum length of s is 1000.
# 
# 
# Example 1:
# Input: 
# 
# "bbbab"
# 
# Output: 
# 
# 4
# 
# One possible longest palindromic subsequence is "bbbb".
# 
# 
# Example 2:
# Input:
# 
# "cbbd"
# 
# Output:
# 
# 2
# 
# One possible longest palindromic subsequence is "bb".
# 
#
## top-down DP 
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:

#         def helper(i,j):
#             if dp[i][j]: return dp[i][j]
#             if s[i] == s[j]:
#                 if j - i == 1:
#                     dp[i][j] = 2
#                 else:
#                     dp[i][j] = helper(i+1,j-1) + 2
#             else:
#                 dp[i][j] = max(helper(i,j-1), helper(i+1,j))
#             return dp[i][j]

#         n = len(s)
#         dp = [[None if i!=j else 1 for j in range(n)] for i in range(n)]
#         return helper(0,n-1)
    
# bottom-up DP
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[None if i!=j else 1 for j in range(n)] for i in range(n)]
        for i in list(range(n))[::-1]:
            for j in range(i+1,n):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][n-1]

