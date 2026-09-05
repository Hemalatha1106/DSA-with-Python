"""
LeetCode 22: Generate Parentheses
URL: https://leetcode.com/problems/generate-parentheses/
Difficulty: Medium
Category: String, Dynamic Programming, Backtracking, Bracket Sequences

Approach:
The solution employs a backtracking (Depth-First Search) approach to generate all valid parenthesis sequences by incrementally building strings.

Key Observation:
It prunes the search space by stopping paths where the number of open parentheses exceeds `n` or where the number of closing parentheses exceeds the number of open parentheses at any intermediate step.

Complexity:
- Time Complexity: O(4^n / sqrt(n)) (The number of valid parenthesis sequences is given by the Nth Catalan number, C_n, which grows approximately as 4^n / (n * sqrt(n)). Each string operation (concatenation) inside the recursion takes O(n) time, resulting in a total time complexity proportional to C_n * n.)
- Space Complexity: O(4^n / sqrt(n)) (The recursion stack depth is O(n), and the result list stores C_n strings, each of length O(n), making the total space complexity dominated by storing the results.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(c,s):
            if len(s)==n*2:
                if c==n:
                    res.append(s)
                return
            if len(s)-c>c:
                return     
            if c<n:    
                addo=dfs(c+1,s+"(")    
            addc=dfs(c,s+")")
        dfs(0,"")
        return res        