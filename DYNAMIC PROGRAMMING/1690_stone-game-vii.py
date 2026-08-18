"""
LeetCode 1690: Stone Game VII
URL: https://leetcode.com/problems/stone-game-vii/
Difficulty: Medium
Category: Array, Math, Dynamic Programming, Minimax, Game Theory, Zero-Sum Game

Approach:
The solution employs a Dynamic Programming approach to solve a minimax game, where Alice aims to maximize her score difference against Bob, who plays optimally to minimize it. It builds up solutions for increasing subarray lengths.

Key Observation:
The problem exhibits optimal substructure and overlapping subproblems. A 1D DP array is used to optimize space, implicitly storing `dp[l][r]` values by leveraging the fact that current computations only depend on results from the previous subarray length.

DP State:
The `dp[l]` array element stores the maximum score difference (Alice's score - Bob's score) Alice can achieve from the subarray `stones[l...r]`, where `r` is implicitly `l + length - 1`. During computation for a given `length`, `dp` array elements refer to results from the `length-1` iteration.

DP Transition:
The recurrence relation is `dp[l] = max( (sum(stones[l+1...r]) - dp[l+1]), (sum(stones[l...r-1]) - dp[l]) )`. This formula represents Alice choosing between removing `stones[l]` (gaining `sum(stones[l+1...r])`, then facing Bob's optimal play on `stones[l+1...r]`) or removing `stones[r]` (gaining `sum(stones[l...r-1])`, then facing Bob's optimal play on `stones[l...r-1]`).

Complexity:
- Time Complexity: O(N^2) (The solution involves two nested loops: the outer loop iterates `N` times (for `length`) and the inner loop iterates up to `N` times (for `l`), resulting in a quadratic time complexity.)
- Space Complexity: O(N) (An `O(N)` prefix sum array (`p`) and an `O(N)` DP array (`dp`) are used to store intermediate results, making the overall space complexity linear with respect to the input size `N`.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        p=[0]
        for i in stones:
            p.append(p[-1]+i)  
        dp=[0]*len(stones)     
        for length in range(2,len(stones)+1):
            for l in range(len(stones)-length+1):
                r=l+length-1
                left=(p[r+1]-p[l+1])-dp[l+1]
                right=(p[r]-p[l])-dp[l]
                dp[l]=max(left,right)
        return dp[0]