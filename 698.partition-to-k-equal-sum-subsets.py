#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (41.48%)
# Total Accepted:    37.2K
# Total Submissions: 89.5K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an array of integers nums and a positive integer k, find whether it's
# possible to divide this array into k non-empty subsets whose sums are all
# equal.
#
#
#
# Example 1:
#
#
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
#
#
#
#
# Note:
#
#
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.
#
#
#
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

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
