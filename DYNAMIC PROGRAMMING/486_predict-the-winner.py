"""
LeetCode 486: Predict the Winner
URL: https://leetcode.com/problems/predict-the-winner/
Difficulty: Medium
Category: Array, Math, Dynamic Programming, Recursion, Minimax, Game Theory, Zero-Sum Game

Approach:
This solution uses a top-down dynamic programming approach with recursion and memoization, modeling the game as a minimax problem to determine the maximum score difference a player can achieve.

Key Observation:
The `@lru_cache` decorator is used to memoize the results of subproblems, significantly optimizing the recursive calls by avoiding recomputing previously solved states.

DP State:
dfs(l, r) represents the maximum score difference (current player's score - opponent's score) that the current player can achieve from the subarray nums[l:r+1].

DP Transition:
dp[l][r] = max(nums[l] - dp[l+1][r], nums[r] - dp[l][r-1]) where the current player chooses the move that maximizes their score advantage, subtracting the opponent's optimal score from the remaining subproblem.

Complexity:
- Time Complexity: O(N^2) (There are O(N^2) unique states for (l, r) as 'l' and 'r' can each range from 0 to N-1, and each state is computed in O(1) time after subproblems are resolved.)
- Space Complexity: O(N^2) (The `@lru_cache` stores the results for O(N^2) unique states, and the recursion stack depth can go up to O(N) in the worst case.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache
        def dfs(l,r):
            if l==r:
                return nums[l]
            left=nums[l]-dfs(l+1,r)
            right=nums[r]-dfs(l,r-1)
            return max(left,right)
        return dfs(0,len(nums)-1)>=0        