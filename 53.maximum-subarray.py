#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (42.96%)
# Total Accepted:    478.7K
# Total Submissions: 1.1M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums.copy() 
        for i in range(1,len(dp)):
            if dp[i-1]<=0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)

# --solution--
# dp[i] means the maximum subarray ending with nums[i]
# dp[i] = nums[i] if dp[i-1]<=0
#       = nums[i] + dp[i-1] if dp[i-1]>0
