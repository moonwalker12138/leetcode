#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (46.42%)
# Total Accepted:    450K
# Total Submissions: 969K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
# 
# Note that you cannot sell a stock before you buy one.
# 
# Example 1:
# 
# 
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# 
# 
# Example 2:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0: 
            return 0
        min_buying = prices[0]  # 当前节点之前最小的buying price
        max_profit = 0  # 全局可获得的最大利润
        for i in range(1,len(prices)):
            profit = prices[i] - min_buying # 以当前节点作为selling price可获得的最大利润
            if prices[i]<min_buying: 
                min_buying = prices[i]  # 更新min_buying
            if profit>max_profit:
                max_profit = profit # 更新max_profit
        return max_profit
        
