#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (36.86%)
# Total Accepted:    129.4K
# Total Submissions: 350.8K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# Example:
# 
# Given nums = [-2, 0, 3, -5, 2, -1]
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# 
# 
# Note:
# 
# You may assume that the array does not change.
# There are many calls to sumRange function.
# 
# 
#
class NumArray:

    def __init__(self, nums: List[int]):
       self.len = len(nums)
       self.memo = nums.copy()
       for i in range(1,len(nums)):
           self.memo[i] += self.memo[i-1]

    def sumRange(self, i: int, j: int) -> int:
        if i==0:
            return self.memo[j]
        else:
            return self.memo[j] - self.memo[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# --solution--
# correct: dp[i,j] = dp[i,j-1] + dp[j,j]
# wrong: dp[i,j] = dp[0,j] + dp[0,i-1]

