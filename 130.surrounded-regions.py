#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (22.23%)
# Total Accepted:    140.2K
# Total Submissions: 622.1K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#
class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i,j):
            if visited[i][j]:
                return
            visited[i][j] = True
            if board[i][j] == "O":
                to_flip.remove((i,j))
                if i-1 >= 0:
                    dfs(i-1,j)
                if i+1 < row:
                    dfs(i+1,j)
                if j-1 >= 0:
                    dfs(i,j-1)
                if j+1 < column:
                    dfs(i,j+1)
            # print("to_flip\n{}".format(to_flip))

            

        if not board:
            return 
        row,column = len(board), len(board[0])
        if row==1 or column==1:
            return

        to_flip = [(i,j) for i in range(row) for j in range(column) if board[i][j]=="O"]
        visited = [[False for j in range(column)] for i in range(row)]

        for i in range(row):
            dfs(i,0)
            dfs(i,column-1)
        for j in range(column):
            dfs(0,j)
            dfs(row-1,j)

        for i,j in to_flip:
            board[i][j] = "X"

if __name__=="__main__":
    solution = Solution()
    board = [["O","O"],["O","O"]]
    solution.solve(board)
