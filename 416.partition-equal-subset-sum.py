#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (40.01%)
# Total Accepted:    78.6K
# Total Submissions: 195.9K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
# 
# Note:
# 
# 
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1, 5, 11, 5]
# 
# Output: true
# 
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1, 2, 3, 5]
# 
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
# 
# 
#
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        k = 2
        target, remainder = divmod(sum(nums), k)
        if remainder: return False

        def search(groups):
            if not nums: return True
            num = nums.pop()
            for i,group in enumerate(groups):
                if group+num<=target:
                    groups[i] += num
                    if search(groups): return True
                    groups[i] -= num
            nums.append(num)
            return False

        groups = [0] * k
        nums.sort()
        return search(groups)
