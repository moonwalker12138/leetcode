#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (67.18%)
# Likes:    304
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 33.5K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 示例:
# 
# 输入: 4
# 输出: [
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        #
        available_rows = set(range(n))
        available_columns = set(range(n))
        available_main_diagonal = set(range(1-n, n))
        available_sub_diagonal = set(range(2*n-1))

        def backtrack(row, solution):
            if row == n:
                solutions.append(solution)
                return
            for col in range(n):
                main_diagnoal = row - col
                sub_diagnoal = row + col
                if col in available_columns and main_diagnoal in available_main_diagonal and sub_diagnoal in available_sub_diagonal:
                    # forward
                    available_columns.remove(col)
                    available_main_diagonal.remove(main_diagnoal)
                    available_sub_diagonal.remove(sub_diagnoal)
                    # 
                    backtrack(row+1, solution+[col])
                    # backward
                    available_columns.add(col)
                    available_main_diagonal.add(main_diagnoal)
                    available_sub_diagonal.add(sub_diagnoal)
        
        backtrack(0, [])
        # generate board
        for i, sol in enumerate(solutions):
            board = []
            for col in sol:
                string = '.' * col + 'Q' + '.' * (n-col-1)
                board.append(string)
            solutions[i] = board
        return solutions
    
if __name__ == "__main__":
    n = 4
    ans = Solution().solveNQueens(n)
    print(ans)
            
            
        
# @lc code=end

