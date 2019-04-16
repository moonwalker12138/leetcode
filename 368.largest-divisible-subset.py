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
        dp = {} # dp --> {num:(len,parent)} 表示以num为最大数的子集的最大长度为len,上一节点为parent,若当前节点为根节点则parent==None
        for num in sorted(nums):
            _ = [(v[0]+1,k) for k,v in dp.items() if num % k == 0] # _: 能够容纳num的子集集合
            dp[num] = max(_,key=lambda x:x[0],default=(1,None)) # default: 已有子集无法容纳num,num构成一个新的子集
        key, _ = max(dp.items(),key=lambda x:x[1][0],default=(None,None))   # default: nums(dp)可能为空,此时key==None
        ans = []
        # while: 根据链表找到所有节点
        while key:
            ans.append(key)
            key = dp[key][1]
        return ans



    # def largestDivisibleSubset(self, nums):
    #     if not nums:
    #         return []
    #     nums = sorted(nums)
    #     cnt = [1] * len(nums)
    #     parent = [-1] * len(nums)
    #     for i in range(1,len(nums)):
    #         prev = {cnt[j]:j for j in range(0,i) if nums[i] % nums[j] == 0}
    #         if prev:
    #             cnt[i] += max(prev)
    #             parent[i] = prev[max(prev)]
    #     res= []
    #     idx = cnt.index(max(cnt))
    #     while idx>=0:
    #         res.append(nums[idx])
    #         idx = parent[idx]
    #     return res


if __name__=='__main__':
    solution = Solution()
    nums = [3,4,16,8]
    res = solution.largestDivisibleSubset(nums)
    print(res)
