"""
LeetCode 1406: Stone Game III
URL: https://leetcode.com/problems/stone-game-iii/
Difficulty: Hard
Category: Array, Math, Dynamic Programming, Minimax, Game Theory, Zero-Sum Game

Approach:
This implementation uses a top-down dynamic programming approach with memoization to solve the game, determining the optimal score difference Alice can achieve by playing optimally.

Key Observation:
Precomputing suffix sums allows for O(1) calculation of stone values taken in each turn, while the `@cache` decorator memoizes results for each game state to prevent redundant computations.

DP State:
dp[i] (represented by `dfs(i)`) is the maximum possible score difference (current player's score - opponent's score) that the current player can achieve when starting the game from `stoneValue[i]` onwards.

DP Transition:
dp[i] = max( (s[i] - s[i+x]) - dp[i+x] ) for x in {1, 2, 3}, where `s[i] - s[i+x]` is the sum of stones the current player takes and `dp[i+x]` is the next player's optimal score difference from the remaining stones.

Complexity:
- Time Complexity: O(N) (The suffix sum array is computed in O(N), and the recursive `dfs` function explores N distinct states, with each state requiring a constant number of operations due to the fixed lookahead (1, 2, or 3 stones).)
- Space Complexity: O(N) (O(N) space is used for storing the precomputed suffix sums and O(N) for the memoization table (cache) and the recursion stack, where N is the number of stones.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        s=[]
        sm=0
        for i in stoneValue[::-1]:
            sm+=i
            s.append(sm)
        s.reverse() 
        s.append(0)   
        @cache
        def dfs(i):
            if i>=len(stoneValue):
                return 0
            mx=float('-inf')
            for x in range(1,4):
                if i+x<=len(stoneValue):
                    b=dfs(i+x)
                    a=(s[i]-s[i+x])-b
                    mx=max(mx,a)
            return mx
        res=dfs(0)
        if res>0:
            return "Alice"
        elif res==0:
            return "Tie"
        return "Bob"                
