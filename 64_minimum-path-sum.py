"""
LeetCode 64: Minimum Path Sum
URL: https://leetcode.com/problems/minimum-path-sum/
Difficulty: Medium
Category: Array, Dynamic Programming, Matrix

Approach:
This implementation uses a top-down Dynamic Programming approach, employing Depth-First Search (DFS) with memoization to find the minimum path sum.

Key Observation:
Memoization is used to store the minimum path sum from any cell (i, j) to the bottom-right, preventing redundant computations for overlapping subproblems.

DP State:
dp[i][j] represents the minimum path sum from the current cell (i, j) to the target cell (m-1, n-1).

DP Transition:
dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1]), considering paths moving only down or right.

Complexity:
- Time Complexity: O(m * n) (Each cell (i, j) of the grid is visited and computed exactly once due to memoization, where m is the number of rows and n is the number of columns.)
- Space Complexity: O(m * n) (The space is primarily used for the `dp` table to store computed results for each cell, plus the recursion stack depth which can go up to O(m+n).)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.mn=float('inf')
        def dfs(i,j):
            if i>=m or j>=n:
                return float('inf')
            if i==m-1 and j==n-1:
                return grid[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]    
            down=grid[i][j]+dfs(i+1,j)
            right=grid[i][j]+dfs(i,j+1)
            dp[i][j]=min(down,right)  
            return dp[i][j] 
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*n for _ in range(m)]
        return dfs(0,0)
        
