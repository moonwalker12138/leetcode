#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#
# https://leetcode.com/problems/can-i-win/description/
#
# algorithms
# Medium (26.94%)
# Total Accepted:    33.3K
# Total Submissions: 123.7K
# Testcase Example:  '10\n11'
#
# In the "100 game," two players take turns adding, to a running total, any
# integer from 1..10. The player who first causes the running total to reach or
# exceed 100 wins. 
# 
# What if we change the game so that players cannot re-use integers? 
# 
# For example, two players might take turns drawing from a common pool of
# numbers of 1..15 without replacement until they reach a total >= 100.
# 
# Given an integer maxChoosableInteger and another integer desiredTotal,
# determine if the first player to move can force a win, assuming both players
# play optimally. 
# 
# You can always assume that maxChoosableInteger will not be larger than 20 and
# desiredTotal will not be larger than 300.
# 
# 
# Example
# 
# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
# 
# Output:
# false
# 
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from
# 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >=
# desiredTotal.
# Same with other integers chosen by the first player, the second player will
# always win.
# 
# 
#
class Solution:

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (1 + maxChoosableInteger) * maxChoosableInteger/2 < desiredTotal:
            return False
        self.memo = {}
        return self.helper(list(range(1,maxChoosableInteger+1)),desiredTotal)

    def helper(self,nums,total):
        hash = str(nums)
        if hash in self.memo:
            return self.memo[hash]
        if nums[-1] >= total:
            return True
        for i in range(len(nums)):
            opponentWin = self.helper(nums[:i]+nums[i+1:], total-nums[i])
            if not opponentWin:
                self.memo[hash] = True
                return self.memo[hash]
        self.memo[hash] = False 
        return self.memo[hash]


if __name__=='__main__':
    solution = Solution()
    maxChoosableInteger = 10
    desiredTotal = 11
    print(solution.canIWin(maxChoosableInteger,desiredTotal))



