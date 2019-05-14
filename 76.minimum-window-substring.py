#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (30.01%)
# Total Accepted:    227.6K
# Total Submissions: 747.2K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# Example:
# 
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# 
# Note:
# 
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
# 
#
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: 
            return ""

        from collections import Counter
        t_counts = Counter(t) # dict {char:num} of t
        required = len(t_counts) # num of unique characters in t

        window_counts = {} # dict {char:num} of present window 
        formed = 0 # num of unique characters in present window

        l,r = 0,0 # left pointer & right pointer
        ans = float("inf"),None,None # tuple of the form (window length,left pointer,right pointer)

        while r<len(s):
            # append the character at the position pointed by the 'right pointer' to the window
            char = s[r]
            window_counts[char] = window_counts.get(char,0)+1
            if char in t and window_counts[char]==t_counts[char]:
                formed += 1
            # move left pointer forward in order to contract the window
            while l<=r and required==formed: 
                # save the smallest window until now
                if r-l+1<ans[0]:
                    ans = (r-l+1, l, r)

                # remove the character at the position pointed by the 'left pointer' from the window
                char = s[l]
                window_counts[char] -= 1
                if char in t and window_counts[char]<t_counts[char]:
                    formed -= 1
                l += 1
            # move right pointer forward in order to expand the window
            r += 1 

        return "" if ans[0]==float("inf") else s[ans[1]:ans[2]+1]
