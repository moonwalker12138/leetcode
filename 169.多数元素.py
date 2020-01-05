#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (60.98%)
# Likes:    404
# Dislikes: 0
# Total Accepted:    96.7K
# Total Submissions: 158.5K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: 3
# 
# 示例 2:
# 
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 
# 
#

# @lc code=start
from typing import List
from collections import defaultdict
""" hash list """
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         d = defaultdict(int)
#         for n in nums:
#             d[n] += 1
#             if d[n] > len(nums)//2:
#                 return n

""" Boyer-Moore Voting Algorithm """
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for n in nums:
            if count==0:
                candidate = n
                count += 1
            else:
                if n==candidate:
                    count += 1
                else:
                    count -= 1
        return candidate

if __name__ == "__main__":
    nums = [1]
    ans = Solution().majorityElement(nums)
    print(ans)

        
# @lc code=end

