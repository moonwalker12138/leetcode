#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (51.61%)
# Total Accepted:    125.3K
# Total Submissions: 241.2K
# Testcase Example:  '3\n7'
#
# 
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# 
# Note:
# 
# 
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#
class Solution:
    def combinationSum3(self, k, n):
        res = []

        def dp(start,k,n,l):

            if k == 1:
                if start == n:
                    res.append(l + [n])
                    return
                else:
                    return

            l.append(start)
            for i in range(start+1,10):
                dp(i,k-1,n-start,l.copy())

        for i in range(1,10):
            dp(i,k,n,[])
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.combinationSum3(k=3,n=9)
    print(res)

