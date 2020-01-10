#
# @lc app=leetcode.cn id=282 lang=python3
#
# [282] 给表达式添加运算符
#
# https://leetcode-cn.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (31.01%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    1.5K
# Total Submissions: 4.8K
# Testcase Example:  '"123"\n6'
#
# 给定一个仅包含数字 0-9 的字符串和一个目标值，在数字之间添加二元运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。
# 
# 示例 1:
# 
# 输入: num = "123", target = 6
# 输出: ["1+2+3", "1*2*3"] 
# 
# 
# 示例 2:
# 
# 输入: num = "232", target = 8
# 输出: ["2*3+2", "2+3*2"]
# 
# 示例 3:
# 
# 输入: num = "105", target = 5
# 输出: ["1*0+5","10-5"]
# 
# 示例 4:
# 
# 输入: num = "00", target = 0
# 输出: ["0+0", "0-0", "0*0"]
# 
# 
# 示例 5:
# 
# 输入: num = "3456237490", target = 9191
# 输出: []
# 
# 
#

# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        answers = []
        
        def recurse(num:int, prev_opd:int, value:int, string:list):
            if len(num) == 0 and value == target:
                answers.append(string)
            for i in range(1, len(num)+1):
                # skip num strating with '0', such as '05'
                if i > 1 and num[0] == '0':
                    continue
                cur_opd = int(num[:i])
                if string == '':
                    recurse(num[i:], cur_opd, cur_opd, num[:i])
                else:
                    recurse(num[i:], cur_opd, value + cur_opd, string + '+' + num[:i])
                    recurse(num[i:], -cur_opd, value - cur_opd, string + '-' + num[:i])
                    recurse(num[i:], prev_opd * cur_opd, value - prev_opd + prev_opd * cur_opd, string + '*' + num[:i])
        recurse(num, 0, 0, '') 
        return answers
        
# @lc code=end
