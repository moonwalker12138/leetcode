#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (34.56%)
# Total Accepted:    44.7K
# Total Submissions: 129.1K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies:
# 
# Si % Sj = 0 or Sj % Si = 0.
# 
# If there are multiple solutions, return any subset is fine.
# 
# Example 1:
# 
# 
# 
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,4,8]
# Output: [1,2,4,8]
# 
# 
# 
#
class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums = sorted(nums)
        cnt = [1] * len(nums)
        parent = [-1] * len(nums)
        for i in range(1,len(nums)):
            prev = {cnt[j]:j for j in range(0,i) if nums[i] % nums[j] == 0}
            if prev:
                cnt[i] += max(prev)
                parent[i] = prev[max(prev)]
        res= []
        idx = cnt.index(max(cnt))
        while idx>=0:
            res.append(nums[idx])
            idx = parent[idx]
        return res

if __name__=='__main__':
    solution = Solution()
    nums = [3,4,16,8]
    res = solution.largestDivisibleSubset(nums)
    print(res)
