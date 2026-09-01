"""
LeetCode 516: Longest Palindromic Subsequence
URL: https://leetcode.com/problems/longest-palindromic-subsequence/
Difficulty: Medium
Category: String, Dynamic Programming

Approach:
This solution employs top-down dynamic programming with memoization to determine the length of the longest palindromic subsequence.

Key Observation:
The `@cache` decorator efficiently stores the results of already computed subproblems `recur(i, j)`, preventing redundant calculations and optimizing performance.

DP State:
dp[i][j] represents the length of the longest palindromic subsequence within the substring `s[i...j]`.

DP Transition:
If `s[i] == s[j]`, `dp[i][j] = 2 + dp[i+1][j-1]`; otherwise, `dp[i][j] = max(dp[i+1][j], dp[i][j-1])`, with base cases `dp[i][i] = 1` and `dp[i][j] = 0` for `i > j`.

Complexity:
- Time Complexity: O(N^2) (The solution computes each of the O(N^2) unique `(i, j)` states once, with each computation involving constant time operations.)
- Space Complexity: O(N^2) (The memoization table, managed by `@cache`, stores results for all O(N^2) possible `(i, j)` states.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def recur(i,j):
            if i>j:
                return 0
            if i==j:
                return 1
            if s[i]==s[j]:
                return 2+recur(i+1,j-1)
            return max(recur(i+1,j),recur(i,j-1))
        return recur(0,len(s)-1)                