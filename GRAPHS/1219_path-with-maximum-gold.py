"""
LeetCode 1219: Path with Maximum Gold
URL: https://leetcode.com/problems/path-with-maximum-gold/
Difficulty: Medium
Category: Array, Backtracking, Matrix

Approach:
The algorithm uses Depth-First Search (DFS) with backtracking to explore all possible paths that collect gold.

Key Observation:
The crucial design is the use of a `visited` array which is reset after each DFS path exploration, ensuring that cells are not revisited within a single path but can be part of multiple distinct paths starting from different points.

Complexity:
- Time Complexity: O(N*M * 3^(N*M)) (The outer loops iterate N*M times, initiating a DFS from each cell. Each DFS explores paths of length up to N*M cells, with a branching factor of at most 3 (excluding the immediate previous cell) due to the visited array preventing cycles within a path.)
- Space Complexity: O(N*M) (This accounts for the `v` (visited) matrix and the maximum depth of the recursion stack, which can go up to N*M in the worst case.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        mx=0
        n=len(grid)
        m=len(grid[0])
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        v=[[0]*m for _ in range(n)]
        def dfs(r,c):
            if grid[r][c]==0:
                return 0
            mxt=0
            v[r][c]=1    
            for a in range(4):
                cr=r+dx[a]
                cc=c+dy[a]
                if 0<=cr<n and 0<=cc<m and v[cr][cc]==0 and grid[cr][cc]!=0:
                    mxt=max(mxt,dfs(cr,cc))   
            v[r][c]=0
            return grid[r][c]+mxt                  
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    mx=max(mx,dfs(i,j))
        return mx            