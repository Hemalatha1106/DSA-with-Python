"""
LeetCode 935: Knight Dialer
URL: https://leetcode.com/problems/knight-dialer/
Difficulty: Medium
Category: Dynamic Programming

Approach:
This implementation uses dynamic programming with top-down recursion and memoization to count all possible valid knight dialer sequences.

Key Observation:
Memoization, facilitated by `@lru_cache`, is crucial for efficiency by storing and reusing the results of previously computed subproblems.

DP State:
The state `dfs(i, j, n)` represents the number of valid knight dialer sequences of length `n+1` that can be formed, starting from the keypad digit at `(i, j)` and making `n` subsequent moves.

DP Transition:
The transition `dfs(i, j, n) = sum(dfs(cr, cc, n-1))` for all 8 valid knight moves `(cr, cc)` from `(i, j)`, where `cr` and `cc` are within bounds and not '*' or '#', with results taken modulo `10^9+7`. The base case is `dfs(i, j, 0) = 1` for any valid digit.

Complexity:
- Time Complexity: O(N) (The number of unique states for the `dfs` function is proportional to `4 * 3 * N`, and each state computation involves a constant number of operations (8 recursive calls).)
- Space Complexity: O(N) (The `lru_cache` stores the results for `4 * 3 * N` distinct states, each consuming constant memory.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def knightDialer(self, n: int) -> int:
        d=[[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
        dx=[-2,-1,1,2,2,1,-1,-2]
        dy=[1,2,2,1,-1,-2,-2,-1]
        @lru_cache(None)
        def dfs(i,j,n):
            if i<0 or i>=4 or j<0 or j>=3:
                return 0
            if n==0:
                return 1
            v=0
            for a in range(8):
                cr=i+dx[a]
                cc=j+dy[a]
                if cr>=0 and cr<4 and cc>=0 and cc<3 and d[cr][cc] not in ["*","#"]:
                    v=(v+dfs(cr,cc,n-1))%mod 
            return v
        mod=10**9+7
        res=0
        for i in range(4):
            for j in range(3):
                if d[i][j] not in ["*","#"]:
                    res=(res+dfs(i,j,n-1))%mod
        return res%mod