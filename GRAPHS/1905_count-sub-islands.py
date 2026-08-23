"""
LeetCode 1905: Count Sub Islands
URL: https://leetcode.com/problems/count-sub-islands/
Difficulty: Medium
Category: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

Approach:
The algorithm iterates through `grid2` and uses Breadth-First Search (BFS) to explore each unvisited island.

Key Observation:
During the BFS traversal of an island in `grid2`, the algorithm verifies that every visited land cell in `grid2` also corresponds to a land cell in `grid1`; if any cell in `grid2` is land but not in `grid1`, the entire island is disqualified.

Complexity:
- Time Complexity: O(N * M) (Each cell in `grid2` is visited at most once by the main loop and the BFS traversal, performing constant work per cell.)
- Space Complexity: O(N * M) (The `v` (visited) array and the BFS queue can store up to N*M elements in the worst-case scenario.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n=len(grid1)
        m=len(grid1[0])
        v=[[0]*m for _ in range(n)]
        def bfs(r,c):
            q=deque([(r,c)])
            f=True
            while q:
                r,c=q.popleft()
                dx=[-1,0,1,0]
                dy=[0,1,0,-1]
                if grid1[r][c]==0:
                    f=False
                for i in range(4):            
                    cr=dx[i]+r
                    cc=dy[i]+c
                    if 0<=cr<n and 0<=cc<m and grid2[cr][cc]==1 and v[cr][cc]==0:
                            q.append((cr,cc))
                            v[cr][cc]=1                                      
            return f              
        v=[[0]*m for _ in range(n)]
        res=0
        for r in range(n):
            for c in range(m):
                if grid2[r][c]==1 and v[r][c]==0:
                    v[r][c]=1
                    if bfs(r,c):
                        res+=1
        return res                                   
