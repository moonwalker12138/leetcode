#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (38.24%)
# Likes:    198
# Dislikes: 0
# Total Accepted:    36.2K
# Total Submissions: 94.5K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
# 
# 
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 
# 
# 示例:
# 
# 现有矩阵 matrix 如下：
# 
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
# 
# 
# 给定 target = 5，返回 true。
# 
# 给定 target = 20，返回 false。
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # special case
        if not matrix: return False
        
        def search(matrix, border, target):
            row_start, row_end, col_start, col_end = border
            if row_start > row_end or col_start > col_end: return False
            if target < matrix[row_start][col_start] or target > matrix[row_end][col_end]: return False
            if row_start == row_end and col_start == col_end: return matrix[row_start][col_start] == target
            # devide-conquer
            row_mid = (row_start + row_end) // 2
            col_mid = (col_start + col_end) // 2
            borders = [
                (row_start, row_mid, col_start, col_mid),   # top left block
                (row_mid+1, row_end, col_start, col_mid),   # bottom left block
                (row_start, row_mid, col_mid+1, col_end),   # top right block
                (row_mid+1, row_end, col_mid+1, col_end)   # bottom right block
            ]
            for border in borders:
                ans = search(matrix, border, target)
                if ans:
                    return True
            return False

        return search(matrix, (0, len(matrix)-1, 0, len(matrix[0])-1), target)

if __name__ == "__main__":
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    ans = Solution().searchMatrix(matrix, target)
    print(ans)
# @lc code=end

