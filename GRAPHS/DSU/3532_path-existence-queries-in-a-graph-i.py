"""
LeetCode 3532: Path Existence Queries in a Graph I
URL: https://leetcode.com/problems/path-existence-queries-in-a-graph-i/
Difficulty: Medium
Category: Array, Hash Table, Binary Search, Union-Find, Graph Theory

Approach:
This implementation uses the Disjoint Set Union (DSU) data structure to efficiently manage connected components. It processes the input `nums` array to establish connections between adjacent indices `i` and `i+1` based on a specific value difference constraint, then uses DSU to answer path existence queries.

Key Observation:
The core efficiency comes from the Union-Find algorithm's optimizations, specifically path compression during the `find` operation and union by rank during the `union` operation, which collectively provide nearly constant time for set operations.

Complexity:
- Time Complexity: O((N + M) * alpha(N)) (Initialization takes O(N). Building connections involves N-1 union operations, each O(alpha(N)). Processing M queries involves two find operations per query, each O(alpha(N)).)
- Space Complexity: O(N + M) (O(N) space is used for the parent (`p`) and rank arrays, and O(M) space is used for storing the results of the queries.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        rank=[0]*n
        p=list(range(n))
        def find(n):
            if p[n]!=n:
                p[n]=find(p[n])
            return p[n]
        def union(u,v):
            uu=find(u)
            uv=find(v)
            if uu==uv:
                return False
            elif rank[uu]>rank[uv]:
                p[uv]=uu
            elif rank[uv]>rank[uu]:
                p[uu]=uv
            else:
                p[uv]=uu
                rank[uu]+=1
            return True
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]<=maxDiff:
                union(i,i+1)
        res=[]
        for i,j in queries:
            if find(i)==find(j):
                res.append(True)
            else:
                res.append(False)
        return res            