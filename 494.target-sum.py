#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (45.26%)
# Total Accepted:    98.4K
# Total Submissions: 217K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 
# You are given a list of non-negative integers, a1, a2, ..., an, and a target,
# S. Now you have 2 symbols + and -. For each integer, you should choose one
# from + and - as its new symbol.
# ⁠
# 
# Find out how many ways to assign symbols to make sum of integers equal to
# target S.  
# 
# 
# Example 1:
# 
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# 
# 
# 
# Note:
# 
# The length of the given array is positive and will not exceed 20. 
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
# 
# 
#
class Solution:
    def findTargetSumWays(self, nums: list, S: int) -> int:
        max_layer = len(nums)
        memo = {}
        def dfs(layer,sum):
            if (layer,sum) not in memo:
                if layer==max_layer:
                    ways = 1 if sum==0 else 0
                else:
                    ways = dfs(layer+1,sum-nums[layer]) + dfs(layer+1,sum+nums[layer])
                memo[(layer,sum)] = ways
            return memo[(layer,sum)]

        return dfs(0,S)

if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,1,1]
    S = 3
    ans = solution.findTargetSumWays(nums,S)
    print(ans)

        
