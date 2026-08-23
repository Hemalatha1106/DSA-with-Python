"""
LeetCode 3619: Count Islands With Total Value Divisible by K
URL: https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/
Difficulty: Medium
Category: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

Approach:
This implementation uses Breadth-First Search (BFS) to traverse and identify connected components (islands) of non-zero cells within the input grid.

Key Observation:
It employs a `visited` matrix to ensure each grid cell is processed exactly once, efficiently summing the values of all cells within an island during its single BFS traversal.

Complexity:
- Time Complexity: O(rows * cols) (Each cell in the grid is visited by the outer loops and enqueued in the BFS at most once, resulting in a linear scan of all grid elements.)
- Space Complexity: O(rows * cols) (A `visited` matrix of the same dimensions as the grid and the BFS queue, which can store up to all grid cells in the worst case, are allocated.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        res=0
        def bfs(r,c):
            s=grid[r][c]
            dx=[-1,0,1,0]
            dy=[0,1,0,-1]
            q=deque([(r,c)])
            while q:
                r,c=q.popleft()
                for i in range(4):
                    cr=r+dx[i]
                    cc=c+dy[i]
                    if 0<=cr<len(grid) and 0<=cc<len(grid[0]) and grid[cr][cc]!=0 and v[cr][cc]==0:
                        s+=grid[cr][cc]
                        q.append((cr,cc))
                        v[cr][cc]=1
            return s            
        v=[[0]*len(grid[0]) for _ in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]!=0 and v[r][c]==0:
                    v[r][c]=1
                    if bfs(r,c)%k==0:
                        res+=1
        return res                
        