"""
LeetCode 1631: Path With Minimum Effort
URL: https://leetcode.com/problems/path-with-minimum-effort/
Difficulty: Medium
Category: Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix, Dijkstra's Algorithm

Approach:
This solution employs Dijkstra's algorithm, adapted to find the path from the top-left to the bottom-right cell such that the maximum absolute difference in heights along any segment of the path is minimized.

Key Observation:
Instead of summing edge weights, the algorithm redefines the 'cost' to reach a cell as the maximum effort encountered on the path, updating it with `max(current_path_effort, effort_of_next_segment)` and prioritizing cells with lower maximum efforts using a min-priority queue.

Complexity:
- Time Complexity: O(N * M * log(N * M)) (Each cell (N*M vertices) can be added to the priority queue multiple times, but extracted once, with each push/pop operation taking O(log(N*M)) time, multiplied by 4 neighbor explorations for each cell.)
- Space Complexity: O(N * M) (The `cost` matrix stores the minimum effort to reach each cell, and the priority queue can store up to all N*M cells in the worst case.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n=len(heights)
        m=len(heights[0])
        cost=[[float('inf')]*m for _ in range(n)]
        cost[0][0]=0
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        pq=[(0,0,0)]
        while pq:
            cur,r,c=heapq.heappop(pq)
            if r==n-1 and c==m-1:
                return cur
            for i in range(4):
                cr=r+dx[i]
                cc=c+dy[i]
                if 0<=cr<n and 0<=cc<m:
                    mx=max(cur,abs(heights[r][c]-heights[cr][cc]))
                    if mx<cost[cr][cc]:
                        cost[cr][cc]=mx
                        heapq.heappush(pq,(mx,cr,cc))
