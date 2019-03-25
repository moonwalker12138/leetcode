#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
# https://leetcode.com/problems/is-subsequence/description/
#
# algorithms
# Medium (46.27%)
# Total Accepted:    81.2K
# Total Submissions: 175.5K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# 
# Given a string s and a string t, check if s is subsequence of t.
# 
# 
# 
# You may assume that there is only lower case English letters in both s and t.
# t is potentially a very long (length ~= 500,000) string, and s is a short
# string (
# 
# 
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ace" is a
# subsequence of "abcde" while "aec" is not).
# 
# 
# Example 1:
# s = "abc", t = "ahbgdc"
# 
# 
# Return true.
# 
# 
# Example 2:
# s = "axc", t = "ahbgdc"
# 
# 
# Return false.
# 
# 
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you
# want to check one by one to see if T has its subsequence. In this scenario,
# how would you change your code?
# 
# Credits:Special thanks to @pbrother for adding this problem and creating all
# test cases.
#
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        import collections
        idx = collections.defaultdict(list)
        for i,c in enumerate(t):
            idx[c].append(i)
        cur = -1
        for c in s:
            if c not in idx: 
                return False
            for id in idx[c]:
                if id > cur:
                    cur = id
                    break
            else:
                return False
        return True

# --solution--
# idx: 遍历t，记录其中各个字符出现过的位置
# cur: 遍历s，判断是否存在按s中各字符升序的位置组合(即下面示例中的'1->2->6')

# s='abc'
# idx={
#         'a':[1,3],
#         'b':[2,4,5],
#         'c':[6,8],
#         ...
#         }

# tips: collections.defaultdict() 语法糖
