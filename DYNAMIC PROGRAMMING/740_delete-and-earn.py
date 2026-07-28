"""
LeetCode 740: Delete and Earn
URL: https://leetcode.com/problems/delete-and-earn/
Difficulty: Medium
Category: Array, Hash Table, Dynamic Programming

Approach:
This solution employs a top-down dynamic programming approach with memoization to find the maximum points achievable.

Key Observation:
It first pre-calculates the total points for each number value using a `defaultdict`, then uses `@lru_cache` to memoize the recursive DP function calls, preventing redundant computations.

DP State:
dp(n) represents the maximum points obtainable by considering numbers from `n` up to `mx` (the maximum value in the input array).

DP Transition:
dp(n) = max(d[n] + dp(n+2), dp(n+1)) where `d[n]` is the total points for picking all instances of `n` (proceeding to `n+2` after picking `n`) versus not picking `n` (proceeding to `n+1`).

Complexity:
- Time Complexity: O(N log N + M) (Sorting the input `nums` takes `O(N log N)`, populating the `defaultdict` takes `O(N)`, and the memoized DP function computes at most `M` states (where `M` is the maximum value in `nums`), each in `O(1)` time.)
- Space Complexity: O(N + M) (The `defaultdict` stores up to `N` unique number sums, and `lru_cache` stores `M` DP states along with the recursion stack, contributing `O(M)` space.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        mx=nums[-1]
        d=defaultdict(int)
        for i in nums:
            d[i]+=i
        @lru_cache(None)    
        def dp(n):
            if n>mx:
                return 0
            pick=d[n]+dp(n+2)
            notpick=dp(n+1)
            return max(pick,notpick)
        return dp(nums[0])        

