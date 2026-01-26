from collections import deque
"""
So what is a border cell?

A cell is a border if ANY of these is true:

It is on the edge of the grid

OR it has at least one neighbor that is:

->outside the grid

->OR having a different color
"""
grid = [[1,1],[1,2]]
row = 0
col = 0
color = 3
n=len(grid)
m= len(grid[0])
visited=[[0]*m for _ in range(n)]
visited[row][col]=1
q=deque([(row,col)])
dx=[-1,0,1,0]
dy=[0,1,0,-1]
cur_clr=grid[row][col]
borders=[]
while q:
    is_border=False
    r,c=q.popleft()
    for i in range(4):
        cr=r+dx[i]
        cc=c+dy[i]
        if cr < 0 or cr >=n or cc <0 or cc>=m:#check 1
            is_border=True
        elif grid[cr][cc] != cur_clr:#check 2 if it is border cell
            is_border=True
        elif visited[cr][cc] !=1 and grid[cr][cc]==cur_clr:#check 3
            visited[cr][cc]=1
            q.append((cr,cc))
    if is_border:
        borders.append([r,c])  
for i,j in borders:
    grid[i][j]=color
print(grid)                          
