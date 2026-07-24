"""
LeetCode 62: Unique Paths
URL: https://leetcode.com/problems/unique-paths/
Difficulty: Medium
Category: Math, Dynamic Programming, Combinatorics

Approach:
This implementation uses a recursive Depth-First Search (DFS) approach to explore paths from the start to the end cell.

Key Observation:
Memoization is used to store the results of subproblems in a DP table, preventing redundant calculations and optimizing the recursive DFS.

DP State:
dp[i][j] represents the number of unique paths from the current cell (i, j) to the destination cell (m-1, n-1).

DP Transition:
dp[i][j] = dfs(i+1, j) + dfs(i, j+1), with base cases: 0 if out of bounds (i>=m or j>=n), and 1 if at the target (i==m-1 and j==n-1).

Complexity:
- Time Complexity: O(m * n) (Each of the m*n states (i, j) in the DP table is computed exactly once due to memoization, and each computation takes constant time.)
- Space Complexity: O(m * n) (The dp table requires O(m*n) space to store the results for all possible (i, j) subproblems.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i,j):
            if i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1   
            if dp[i][j]!=-1:
                return dp[i][j]     
            down=dfs(i+1,j)
            right=dfs(i,j+1)
            dp[i][j]=down+right
            return dp[i][j]
        dp=[[-1]*n for _ in range(m)]
        return dfs(0,0)    