#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (37.91%)
# Total Accepted:    298.7K
# Total Submissions: 742.1K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#
class Solution:
    def canFinish(self, numcourses: int, prerequisites: List[List[int]]) -> int:
        in_degrees = [0] * numcourses
        adj = [set() for _ in range(numcourses)]
        for next, prev in prerequisites:
            in_degrees[next] += 1
            adj[prev].add(next)
        from queue import Queue
        q = Queue()
        for i, in_degree in enumerate(in_degrees):
            if in_degree==0:
                q.put(i)
        while not q.empty():
            c = q.get()
            numcourses -= 1
            for i in adj[c]:
                in_degrees[i] -= 1
                if in_degrees[i]==0:
                    q.put(i)
        return numcourses==0
