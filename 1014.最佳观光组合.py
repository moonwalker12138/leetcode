#
# @lc app=leetcode.cn id=1014 lang=python3
#
# [1014] 最佳观光组合
#
# https://leetcode-cn.com/problems/best-sightseeing-pair/description/
#
# algorithms
# Medium (46.24%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    2.8K
# Total Submissions: 6.1K
# Testcase Example:  '[8,1,5,2,6]'
#
# 给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
# 
# 一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
# 
# 返回一对观光景点能取得的最高分。
# 
# 
# 
# 示例：
# 
# 输入：[8,1,5,2,6]
# 输出：11
# 解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= A.length <= 50000
# 1 <= A[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        max_score = 0
        prev = A[0]
        for i in range(1, len(A)):
            score = A[i] - i + prev
            max_score = max(max_score, score)
            prev = max(prev, A[i] + i)
        return max_score
        
# @lc code=end

