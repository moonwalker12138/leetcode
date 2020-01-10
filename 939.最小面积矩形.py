#
# @lc app=leetcode.cn id=939 lang=python3
#
# [939] 最小面积矩形
#
# https://leetcode-cn.com/problems/minimum-area-rectangle/description/
#
# algorithms
# Medium (42.25%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    1.4K
# Total Submissions: 3.2K
# Testcase Example:  '[[1,1],[1,3],[3,1],[3,3],[2,2]]'
#
# 给定在 xy 平面上的一组点，确定由这些点组成的矩形的最小面积，其中矩形的边平行于 x 轴和 y 轴。
# 
# 如果没有任何矩形，就返回 0。
# 
# 
# 
# 示例 1：
# 
# 输入：[[1,1],[1,3],[3,1],[3,3],[2,2]]
# 输出：4
# 
# 
# 示例 2：
# 
# 输入：[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# 所有的点都是不同的。
# 
# 
#

# @lc code=start
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        S = set(map(tuple, points))
        min_area = float('inf')
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2:
                    # if [x1, y2] in points and [x2, y1] in points:
                    if (x1, y2) in S and (x2, y1) in S:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        min_area = min(min_area, area)
        if min_area == float('inf'):
            min_area = 0
        return min_area
                    
# @lc code=end

