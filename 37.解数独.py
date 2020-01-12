#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
# https://leetcode-cn.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (58.53%)
# Likes:    287
# Dislikes: 0
# Total Accepted:    16.5K
# Total Submissions: 28.1K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# 编写一个程序，通过已填充的空格来解决数独问题。
# 
# 一个数独的解法需遵循如下规则：
# 
# 
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 
# 
# 空白格用 '.' 表示。
# 
# 
# 
# 一个数独。
# 
# 
# 
# 答案被标成红色。
# 
# Note:
# 
# 
# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。
# 
# 
#

# @lc code=start
from typing import List
""" 
6/6 cases passed (904 ms)
Your runtime beats 5.9 % of python3 submissions
Your memory usage beats 23.04 % of python3 submissions (13.3 MB)
"""
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # calculate block id according to (i,j)
        block_id = "i // 3 * 3 + j // 3"
        # record available digits
        rows = [set(range(1,10)) for _ in range(9)]
        columns = [set(range(1,10)) for _ in range(9)]
        blocks = [set(range(1,10)) for _ in range(9)]
        # record empty position
        unsolved = []
        # traverse board
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur != '.':
                    cur = int(cur)
                    rows[i].remove(cur)
                    columns[j].remove(cur)
                    blocks[i//3*3+j//3].remove(cur)
                else:
                    unsolved.append((i,j))
        # 
        def backtracking(index):
            if index == len(unsolved):
                return True
            i, j = unsolved[index]
            # generate candidates(digits available) for unsolved (i,j)
            candidates = rows[i] & columns[j] & blocks[i//3*3+j//3]
            if len(candidates) == 0:
                return False
            for candidate in candidates:
                # forward
                rows[i].remove(candidate)
                columns[j].remove(candidate)
                blocks[i//3*3+j//3].remove(candidate)
                if backtracking(index+1):
                    board[i][j] = str(candidate)
                    return True
                else:
                    # backward
                    rows[i].add(candidate)
                    columns[j].add(candidate)
                    blocks[i//3*3+j//3].add(candidate)
        
        backtracking(0)
        return 


        
# @lc code=end

