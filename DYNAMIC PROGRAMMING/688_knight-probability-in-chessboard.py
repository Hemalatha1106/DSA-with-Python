"""
LeetCode 688: Knight Probability in Chessboard
URL: https://leetcode.com/problems/knight-probability-in-chessboard/
Difficulty: Medium
Category: Dynamic Programming

Approach:
This solution uses a top-down dynamic programming approach with memoization to calculate the probability of a knight remaining on the chessboard after a specified number of moves.

Key Observation:
The `@lru_cache` decorator efficiently memoizes the results of the recursive `dfs` function, preventing redundant computations for identical (row, column, moves_left) states.

DP State:
dpState[i][j][k] (represented by `dfs(i, j, k)`) stores the probability that a knight, starting at position (i, j) with 'k' moves remaining, stays on the chessboard for all 'k' moves.

DP Transition:
The transition `dfs(i, j, k) = (1/8) * SUM(dfs(i + dx_m, j + dy_m, k - 1))` is applied for all 8 possible knight moves 'm', considering base cases where `k=0` (probability 1) or `(i,j)` is out of bounds (probability 0).

Complexity:
- Time Complexity: O(N^2 * K) (There are N*N*K unique states (i, j, k) to compute, and each state's calculation involves a constant number of operations (8 recursive calls, effectively O(1) due to memoization).)
- Space Complexity: O(N^2 * K) (The memoization cache stores the results for each of the N*N*K possible states (row, column, moves remaining), each holding a float value.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dx=[-2,-1,1,2,2,1,-1,-2]
        dy=[1,2,2,1,-1,-2,-2,-1]
        @lru_cache(None)
        def dfs(i,j,k):
            if i<0 or i>=n or j<0 or j>=n:
                return 0
            if k==0:
                return 1
            p=0
            for ind in range(8):
                p+=dfs(i+dx[ind],j+dy[ind],k-1)
            return p/8
        return dfs(row,column,k)    