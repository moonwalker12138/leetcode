#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (39.81%)
# Total Accepted:    158K
# Total Submissions: 392.7K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
# 
#
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def dfs(s,path):
            if not s:
                res.append(path)
                return
            for i in range(1,len(s)+1):
                tmp = s[:i]
                if tmp == tmp[::-1]:
                    dfs(s[i:],path+[tmp])

        res = []
        dfs(s,[])
        return res
