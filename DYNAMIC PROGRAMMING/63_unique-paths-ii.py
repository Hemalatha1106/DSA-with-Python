"""
LeetCode 63: Unique Paths II
URL: https://leetcode.com/problems/unique-paths-ii/
Difficulty: Medium
Category: Array, Dynamic Programming, Matrix

Approach:
The implementation uses a recursive Depth-First Search (DFS) approach to explore all possible paths from the start to the end cell, counting valid unique paths.

Key Observation:
Memoization is employed using a 2D DP table to store the results of subproblems, preventing redundant computations and drastically improving efficiency.

DP State:
dp[i][j] represents the number of unique paths from the current cell (i, j) to the bottom-right target cell (m-1, n-1).

DP Transition:
dp[i][j] = dfs(i+1, j) + dfs(i, j+1), which sums the unique paths from moving down to (i+1, j) and moving right to (i, j+1), while handling base cases for obstacles, boundaries, and the target.

Complexity:
- Time Complexity: O(m * n) (Each cell (state) in the m x n grid is visited and computed exactly once due to memoization, and each computation takes constant time.)
- Space Complexity: O(m * n) (The space complexity is dominated by the m x n DP table used for memoization and the recursion stack depth which can go up to O(m + n) in the worst case.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dfs(i,j):
            if i>=m or j>=n:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]    
            down=dfs(i+1,j)
            right=dfs(i,j+1)
            dp[i][j]=down+right
            return dp[i][j]
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[-1]*n for _ in range(m)]
        return dfs(0,0)                