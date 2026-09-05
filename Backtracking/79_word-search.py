"""
LeetCode 79: Word Search
URL: https://leetcode.com/problems/word-search/
Difficulty: Medium
Category: Array, String, Backtracking, Depth-First Search, Matrix

Approach:
This implementation uses Depth-First Search (DFS) with backtracking to explore all possible paths on the board that could form the target word.

Key Observation:
A `visited` matrix tracks cells used in the current path, preventing cycles and ensuring each cell is used at most once for a given word instance, while backtracking (unmarking cells) allows exploration of alternative paths.

Complexity:
- Time Complexity: O(M * N * 3^L) (The algorithm iterates through each of the M*N cells as a potential starting point. For each starting point, the DFS explores paths of length L, with at most 3 unvisited neighbors at each step (after the first step), leading to a complexity proportional to 3^L for each starting cell.)
- Space Complexity: O(M * N + L) (The space complexity is dominated by the `visited` matrix of size M*N, plus the recursion stack depth which can go up to L (the length of the word).)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r,c,ind):
            if ind==len(word):
                return True
            v[r][c]=1
            dx=[-1,0,1,0]
            dy=[0,1,0,-1]
            for i in range(4):
                cr=dx[i]+r
                cc=dy[i]+c
                if 0<=cr<len(board) and 0<=cc<len(board[0]) and v[cr][cc]==0 and board[cr][cc]==word[ind]:    
                    if dfs(cr,cc,ind+1):
                        return True
            v[r][c]=0
            return False
        v=[[0]*len(board[0]) for _ in range(len(board))]
        for j in range(len(board)):
            for k in range(len(board[0])):
                if board[j][k]==word[0]:
                    if dfs(j,k,1):
                        return True
        return False                                