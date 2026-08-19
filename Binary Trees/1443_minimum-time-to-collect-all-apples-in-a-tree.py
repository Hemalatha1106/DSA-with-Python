"""
LeetCode 1443: Minimum Time to Collect All Apples in a Tree
URL: https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
Difficulty: Medium
Category: Hash Table, Tree, Depth-First Search, Breadth-First Search, DP on Trees

Approach:
The implementation uses Depth-First Search (DFS) to traverse the tree, starting from the root node (0). It recursively calculates the minimum time needed for each subtree.

Key Observation:
Time is accumulated for a child's subtree only if that child node or any node within its subtree contains an apple, adding 2 units of time for traveling down to and back up from the child.

Complexity:
- Time Complexity: O(N) (Building the adjacency list takes O(E) time, and the DFS visits each node and edge exactly once, resulting in an O(N + E) complexity, which simplifies to O(N) for a tree.)
- Space Complexity: O(N) (The adjacency list uses O(N) space, and the recursion stack for DFS can go up to O(N) depth in the worst-case scenario (a skewed tree).)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        d=defaultdict(list)
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        def dfs(n,p):
            total=0
            for nei in d[n]:
                if nei==p:
                    continue
                childTime=dfs(nei,n)
                if childTime>0 or hasApple[nei]:
                    total+=childTime+2
            return total
        return dfs(0,-1)                
