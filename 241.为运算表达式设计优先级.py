#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#
# https://leetcode-cn.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (69.88%)
# Likes:    101
# Dislikes: 0
# Total Accepted:    5.8K
# Total Submissions: 8.2K
# Testcase Example:  '"2-1-1"'
#
# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及
# * 。
# 
# 示例 1:
# 
# 输入: "2-1-1"
# 输出: [0, 2]
# 解释: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# 
# 示例 2:
# 
# 输入: "2*3-4*5"
# 输出: [-34, -14, -10, -10, 10]
# 解释: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# 
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        operators = []
        for i,c in enumerate(input):
            if c in '+-*':
                operators.append(i)
        if not operators:
            return [int(input)]

        def compute(opd1, opd2, opt):
            if opt == '+':
                return opd1 + opd2
            elif opt == '-':
                return opd1 - opd2
            elif opt == '*':
                return opd1 * opd2

        ans = []
        for op in operators:
            # devide-conquer
            left_ans = self.diffWaysToCompute(input[:op])
            right_ans = self.diffWaysToCompute(input[op+1:])
            for opd1 in left_ans:
                for opd2 in right_ans:
                    ans.append(compute(opd1, opd2, input[op]))
        return ans

# @lc code=end

