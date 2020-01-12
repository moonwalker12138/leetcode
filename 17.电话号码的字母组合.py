#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (51.83%)
# Likes:    536
# Dislikes: 0
# Total Accepted:    68.6K
# Total Submissions: 132K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 示例:
# 
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
# 
#

# @lc code=start
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        d = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        N = len(digits)
        ans = []
        def recurse(index, string):
            if index == N:
                ans.append(string)
                return
            digit = digits[index]
            for letter in d[digit]:
                recurse(index+1, string+letter)
        recurse(0, '')
        return ans
if __name__ == "__main__":
    digits = "23"
    ans = Solution().letterCombinations(digits)
    print(ans)
                
        
# @lc code=end

