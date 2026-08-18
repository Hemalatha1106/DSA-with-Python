"""
LeetCode 877: Stone Game
URL: https://leetcode.com/problems/stone-game/
Difficulty: Medium
Category: Array, Math, Dynamic Programming, Minimax, Game Theory, Zero-Sum Game

Approach:
This solution employs a recursive top-down dynamic programming approach with memoization to simulate optimal play in a minimax game.

Key Observation:
The `@lru_cache` decorator memoizes the results of overlapping subproblems, efficiently transforming the exponential complexity of a naive recursion into a polynomial time solution.

DP State:
dp[l][r] represents the maximum score difference (current player's score minus opponent's score) achievable from the sub-array of piles from index 'l' to 'r' (inclusive).

DP Transition:
dp[l][r] = max(piles[l] - dp[l+1][r], piles[r] - dp[l][r-1]); Base case: dp[l][l] = piles[l].

Complexity:
- Time Complexity: O(N^2) (There are O(N^2) unique states (l, r), and each state is computed once in constant time due to memoization.)
- Space Complexity: O(N^2) (The memoization cache stores results for O(N^2) unique (l, r) states, contributing the dominant factor to space usage.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dfs(l,r):
            if l==r:
                return piles[l]
            left=piles[l]-dfs(l+1,r)
            right=piles[r]-dfs(l,r-1)
            return max(left,right)
        return dfs(0,len(piles)-1)>0
