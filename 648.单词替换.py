#
# @lc app=leetcode.cn id=648 lang=python3
#
# [648] 单词替换
#
# https://leetcode-cn.com/problems/replace-words/description/
#
# algorithms
# Medium (53.21%)
# Likes:    42
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 6.3K
# Testcase Example:  '["cat", "bat", "rat"]\n"the cattle was rattled by the battery"'
#
# 在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为
# 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。
# 
# 现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。
# 
# 你需要输出替换之后的句子。
# 
# 示例 1:
# 
# 
# 输入: dict(词典) = ["cat", "bat", "rat"]
# sentence(句子) = "the cattle was rattled by the battery"
# 输出: "the cat was rat by the bat"
# 
# 
# 注:
# 
# 
# 输入只包含小写字母。
# 1 <= 字典单词数 <=1000
# 1 <=  句中词语数 <= 1000
# 1 <= 词根长度 <= 100
# 1 <= 句中词语长度 <= 1000
# 
# 
#

# @lc code=start
from collections import defaultdict

""" hierarchical hash table
runtime beats 92.91%
memory usage beats 30.61%
"""
# class Solution:
#     def replaceWords(self, dict: List[str], sentence: str) -> str:
#         roots = defaultdict(set)
#         for word in dict:
#             roots[len(word)].add(word)
#         roots = [(length, roots[length]) for length in sorted(roots.keys())]
#         sent = []
#         for word in sentence.split():
#             for length, root in roots:
#                 if len(word) >= length and word[:length] in root:
#                     sent.append(word[:length])
#                     break
#             else:
#                 sent.append(word)
#         sent = ' '.join(sent)
#         return sent

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        rootset = set(dict)
        sentence = sentence.split()
        for i, word in enumerate(sentence):
            for j in range(1, len(word)):
                if word[:j] in rootset:
                    sentence[i] = word[:j]
                    break
        return ' '.join(sentence)
            
# @lc code=end

