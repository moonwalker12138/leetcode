#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (29.29%)
# Total Accepted:    219.1K
# Total Submissions: 742.8K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#
class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        max_product = nums[0]
        prev = {'min':nums[0],'max':nums[0]}
        for i in range(1,n):
            curr = {}
            if nums[i]>0:
                curr['max'] = max(nums[i],nums[i]*prev['max'])
                curr['min'] = min(nums[i],nums[i]*prev['min'])
            else:
                curr['max'] = max(nums[i],nums[i]*prev['min'])
                curr['min'] = min(nums[i],nums[i]*prev['max'])
            max_product = max(max_product,curr['max'])
            prev = curr
        return max_product
        
