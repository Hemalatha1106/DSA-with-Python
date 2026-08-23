"""
LeetCode 79: Word Search
URL: https://leetcode.com/problems/word-search/
Difficulty: Medium
Category: Array, String, Backtracking, Depth-First Search, Matrix

Approach:
This solution employs a Depth-First Search (DFS) algorithm combined with backtracking to explore all possible paths in the matrix that could form the target word.

Key Observation:
A 2D `visited` matrix `v` tracks cells used in the current path to prevent reuse, and the crucial backtracking step (`v[r][c]=0`) unmarks cells after a path segment is explored, allowing them to be part of alternative paths.

Complexity:
- Time Complexity: O(M * N * 4^L) (The algorithm iterates through M*N starting cells; from each, a DFS explores paths up to length L, with a maximum of 4 branching choices at each step, forming a recursion tree bounded by 4^L operations.)
- Space Complexity: O(M * N) (The space complexity is dominated by the `visited` matrix of size M*N, with additional O(L) space for the recursion call stack, where L is the length of the word.)
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