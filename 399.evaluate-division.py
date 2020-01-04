#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (47.57%)
# Likes:    1738
# Dislikes: 133
# Total Accepted:    104.5K
# Total Submissions: 210.7K
# Testcase Example:  '[["a","b"],["b","c"]]\n[2.0,3.0]\n[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# Equations are given in the format A / B = k, where A and B are variables
# represented as strings, and k is a real number (floating point number). Given
# some queries, return the answers. If the answer does not exist, return -1.0.
# 
# Example:
# Given  a / b = 2.0, b / c = 3.0.
# queries are:  a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
# 
# The input is:  vector<pair<string, string>> equations, vector<double>&
# values, vector<pair<string, string>> queries , where equations.size() ==
# values.size(), and the values are positive. This represents the equations.
# Return  vector<double>.
# 
# According to the example above:
# 
# 
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]
# ]. 
# 
# 
# 
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.
# 
#

# @lc code=start
from collections import defaultdict
from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # construct wighted undirected graph
        weights = {}
        adj = defaultdict(list)
        for (l,r),w in zip(equations, values):
            weights[(l,r)] = w
            weights[(r,l)] = 1.0 / w
            weights[(l,l)] = 1.0
            weights[(r,r)] = 1.0
            adj[l].append(r)
            adj[r].append(l)
        visited = {i:False for i in adj}
        
        def dfs(l, r, visited):
            if (l,r) not in weights:
                visited[l] = True
                for m in adj[l]:
                    if not visited[m]:
                        tmp = dfs(m, r, visited)
                        if tmp != -1.0:
                            weights[(l,r)] = weights[(l,m)] * tmp
                            break
                else:
                    weights[(l,r)] = -1.0
            return weights[(l,r)]

        ans = []
        for l,r in queries:
            ans.append(dfs(l,r,visited.copy()))
        return ans

if __name__ == "__main__":
    args = [
        [["a","b"],["b","c"]],
        [2.0,3.0],
        [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    ]
    ans = Solution().calcEquation(*args)
    print(ans)
        
# @lc code=end

