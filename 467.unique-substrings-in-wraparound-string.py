#
# @lc app=leetcode id=467 lang=python3
#
# [467] Unique Substrings in Wraparound String
#
# https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/
#
# algorithms
# Medium (33.49%)
# Total Accepted:    17.2K
# Total Submissions: 51.4K
# Testcase Example:  '"a"'
#
# Consider the string s to be the infinite wraparound string of
# "abcdefghijklmnopqrstuvwxyz", so s will look like this:
# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
# 
# Now we have another string p. Your job is to find out how many unique
# non-empty substrings of p are present in s. In particular, your input is the
# string p and you need to output the number of different non-empty substrings
# of p in the string s.
# 
# Note: p consists of only lowercase English letters and the size of p might be
# over 10000.
# 
# Example 1:
# 
# Input: "a"
# Output: 1
# 
# Explanation: Only the substring "a" of string "a" is in the string s.
# 
# 
# 
# Example 2:
# 
# Input: "cac"
# Output: 2
# Explanation: There are two substrings "a", "c" of string "cac" in the string
# s.
# 
# 
# 
# Example 3:
# 
# Input: "zab"
# Output: 6
# Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of
# string "zab" in the string s.
# 
# 
#
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        count = [0]*26
        maxCur = 0
        for i in range(len(p)):
            if i==0 or ((ord(p[i])-ord(p[i-1])) not in [1,-25]):
                maxCur = 1
            else:
                maxCur += 1
            index = ord(p[i]) - ord('a')
            count[index] = max(count[index],maxCur)
        return sum(count)
        
