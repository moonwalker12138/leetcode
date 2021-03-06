#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (40.81%)
# Total Accepted:    296.5K
# Total Submissions: 726.3K
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# Example 2:
# 
# 
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# 
# 
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = nums.copy()
        if len(dp)==0:
            return 0
        for i in range(0,len(dp)):
            if i==0 or i==1:
                continue
            elif i==2:
                dp[i] += dp[i-2]
            else:
                dp[i] += max(dp[i-2],dp[i-3])
        return max(dp)

# --solution--
# 类似问题
#   53.maximum-subarray.py
#   121.best-time-to-buy-and-sell-stock.py
#
# dp[i]: 以i作为结束节点可获得的最大收益
# dp[i] = nums[i] if i==0 or i==1
#       = nums[i] + nums[i-2] if i==2
#       = nums[i] + max(dp[i-2],dp[i-3]) if i>2
